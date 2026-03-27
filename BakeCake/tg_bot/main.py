import telebot
from keyboards import get_main_menu, get_tier_keyboard, get_shape_keyboard, get_topping_keyboard, get_berries_keyboard, get_decor_keyboard


TOKEN = ""
bot = telebot.TeleBot(TOKEN)

user_data = {}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "Привет! 👋\n\n"
        "Я — BakeCake Bot 🎂\n"
        "Помогу выбрать торт, собрать свой вариант и оформить заказ.\n\n"
        "Выбери, с чего хочешь начать:",
        reply_markup=get_main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):

    if call.data == "catalog":
        bot.send_message(call.message.chat.id, " в разработке.")

    elif call.data == "orders":
        bot.send_message(call.message.chat.id, " в разработке.")

    elif call.data == "custom":
        bot.send_message(
            call.message.chat.id,
            "Выберите количество уровней:",
            reply_markup=get_tier_keyboard()
        )

    elif call.data in ["tier_1", "tier_2", "tier_3"]:
        bot.send_message(
            call.message.chat.id,
            "Выберите форму торта:",
            reply_markup=get_shape_keyboard()
        )

    elif call.data in ["shape_round", "shape_square", "shape_oval"]:
        bot.send_message(
            call.message.chat.id,
            "Выберите топпинг:",
            reply_markup=get_topping_keyboard()
        )
    elif call.data in ["topping_blueberry", "topping_strawberry", "topping_maple", "topping_caramel",
                       "topping_milk_chocolate", "topping_white_sauce", "topping_none"]:
        bot.send_message(
            call.message.chat.id,
            "Выберите ягоды:",
            reply_markup=get_berries_keyboard()
        )

    elif call.data in ["strawberry", "blackberry", "raspberry", "dewberry",
                       "berries_none"]:
        bot.send_message(
            call.message.chat.id,
            "Выберите декор:",
            reply_markup=get_decor_keyboard()
        )
    elif call.data == "add_writing":
        chat_id = call.message.chat.id

        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]["waiting_for_text"] = True

        bot.send_message(chat_id, "Введите надпись для торта:")


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id

    if chat_id in user_data and user_data[chat_id].get("waiting_for_text"):

        user_data[chat_id]["writing"] = message.text

        user_data[chat_id]["waiting_for_text"] = False

        bot.send_message(chat_id, f"Надпись добавлена: {message.text}")


if __name__ == '__main__':
    print("Бот запущен")
    bot.infinity_polling()
