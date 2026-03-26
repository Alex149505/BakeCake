import telebot
from telebot import types

TOKEN = "5111"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Каталог тортов", callback_data="catalog")
    btn2 = types.InlineKeyboardButton("Создать свой торт", callback_data="custom")
    btn3 = types.InlineKeyboardButton("Мои заказы", callback_data="orders")

    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)

    bot.send_message(
        message.chat.id,
        "Привет! 👋\n\n"
        "Я — BakeCake Bot 🎂\n"
        "Помогу выбрать торт, собрать свой вариант и оформить заказ.\n\n"
        "Выбери, с чего хочешь начать:",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):

    if call.data == "catalog":
        bot.send_message(call.message.chat.id, " в разработке.")

    elif call.data == "orders":
        bot.send_message(call.message.chat.id, " в разработке.")

    elif call.data == "custom":
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("1", callback_data="tier_1")
        btn2 = types.InlineKeyboardButton("2", callback_data="tier_2")
        btn3 = types.InlineKeyboardButton("3", callback_data="tier_3")

        markup.row(btn1, btn2, btn3)

        bot.send_message(
            call.message.chat.id,
            "Выберите количество уровней:",
            reply_markup=markup
        )

    elif call.data in ["tier_1", "tier_2", "tier_3"]:
        markup = types.InlineKeyboardMarkup()

        btn1 = types.InlineKeyboardButton("Круг", callback_data="shape_round")
        btn2 = types.InlineKeyboardButton("Квадрат", callback_data="shape_square")
        btn3 = types.InlineKeyboardButton("Овал", callback_data="shape_oval")

        markup.row(btn1, btn2)
        markup.row(btn3)

        bot.send_message(
            call.message.chat.id,
            "Выберите форму торта:",
            reply_markup=markup
        )



if __name__ == '__main__':
    print("Бот запущен")
    bot.infinity_polling()
