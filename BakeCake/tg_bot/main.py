import telebot
from keyboards import get_main_menu
from castom_cake import start_custom_cake, handle_custom_cake_callback, handle_custom_cake_text


TOKEN = "8514556368:AAFVQieUv8qI-ykkjtU8CtbMVzLA5VVz3go"
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
        start_custom_cake(bot, call)

    else:
        handle_custom_cake_callback(bot, call, user_data)


@bot.message_handler(func=lambda message: True)
def handle_text(message):
    handle_custom_cake_text(bot, message, user_data)


if __name__ == '__main__':
    print("Бот запущен")
    bot.infinity_polling()
