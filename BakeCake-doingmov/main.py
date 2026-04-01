import telebot
from telebot import types
from keyboards import get_main_menu
from castom_cake import start_custom_cake, handle_custom_cake_callback, handle_custom_cake_text
from ready_cakes import show_ready_cakes
from utils import save_order_to_data, get_user_orders, get_ready_cakes, custom_cake_state

TOKEN = '8618387233:AAGbNhVJi3y95nQa6c8NCpKcrK6HGe-bevI'
bot = telebot.TeleBot(TOKEN)

agreement_accepted = set()

USER_AGREEMENT_TEXT = (
    "📄 Пользовательское соглашение BakeCake Bot\n\n"
    "1. Используя бота, вы соглашаетесь с обработкой ваших данных.\n"
    "2. Ваши данные будут использоваться только для оформления заказов.\n"
    "3. Бот не передает ваши данные третьим лицам.\n"
    "4. Оплата заказов производится при доставке (наличные/карта).\n\n"
    "Нажмите 'Принять', чтобы продолжить или 'Отменить', чтобы отменить процесс."
)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    chat_id = message.chat.id
    if chat_id not in agreement_accepted:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("✅ Принять", callback_data="accept_agreement"))
        markup.add(types.InlineKeyboardButton("❌ Отменить", callback_data="cancel_agreement"))
        bot.send_message(chat_id, USER_AGREEMENT_TEXT, reply_markup=markup)
    else:
        bot.send_message(chat_id, "Выберите действие:", reply_markup=get_main_menu())

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    data = call.data

    if data == "cancel_agreement":
        bot.send_message(chat_id, "Процесс отменен.")
        return
    if data == "accept_agreement":
        agreement_accepted.add(chat_id)
        bot.send_message(chat_id, "Соглашение принято ✅", reply_markup=get_main_menu())
        return
    if chat_id not in agreement_accepted:
        bot.answer_callback_query(call.id, "Сначала примите соглашение.")
        return

    if data == "catalog":
        show_ready_cakes(bot, chat_id)
    elif data == "orders":
        orders = get_user_orders(chat_id)
        if not orders:
            bot.send_message(chat_id, "У вас нет заказов.", reply_markup=get_main_menu())
        else:
            for i, order in enumerate(orders, 1):
                bot.send_message(chat_id, f"Заказ {i}:\n{order}", reply_markup=get_main_menu())
    elif data == "custom":
        start_custom_cake(bot, call)
    elif data.startswith("order_ready_"):
        cake_name = data.replace("order_ready_", "")
        cake = next((c for c in get_ready_cakes() if c["name"] == cake_name), None)
        if cake:
            order = {"cake": cake_name, "price": cake["price"], "status": "Новый"}
            save_order_to_data(chat_id, order)
            bot.send_message(chat_id, f"Заказ на {cake_name} успешно оформлен! ✅", reply_markup=get_main_menu())
    else:
        handle_custom_cake_callback(bot, call, custom_cake_state)

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    handle_custom_cake_text(bot, message, custom_cake_state)

if __name__ == "__main__":
    print("Бот запущен")
    bot.infinity_polling()