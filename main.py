import telebot
from telebot import types
from keyboards import get_main_menu
from castom_cake import start_custom_cake, handle_custom_cake_callback, handle_custom_cake_text
from ready_cakes import READY_CAKES, show_ready_cakes
from utils import user_data, save_order_to_data, get_user_orders, load_data, save_data

TOKEN = '8618387233:AAGbNhVJi3y95nQa6c8NCpKcrK6HGe-bevI'
bot = telebot.TeleBot(TOKEN)

# ID админов
ADMINS = [123456789]  # <-- сюда ваш Telegram ID

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
        btn_accept = types.InlineKeyboardButton("✅ Принять", callback_data="accept_agreement")
        btn_cancel = types.InlineKeyboardButton("❌ Отменить", callback_data="cancel_agreement")
        markup.add(btn_accept, btn_cancel)
        bot.send_message(chat_id, USER_AGREEMENT_TEXT, reply_markup=markup)
    else:
        bot.send_message(chat_id, "Выберите действие:", reply_markup=get_main_menu())

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    chat_id = call.message.chat.id
    data = call.data

    # Согласие
    if data == "cancel_agreement":
        bot.send_message(chat_id, "Процесс отменен.")
        return
    if data == "accept_agreement":
        agreement_accepted.add(chat_id)
        bot.send_message(chat_id, "Спасибо! Выберите действие:", reply_markup=get_main_menu())
        return
    if chat_id not in agreement_accepted:
        bot.answer_callback_query(call.id, "Сначала примите соглашение.")
        return

    # Главное меню
    if data == "catalog":
        show_ready_cakes(bot, chat_id)
    elif data == "orders":
        orders = get_user_orders(chat_id)
        if orders:
            for idx, order in enumerate(orders, 1):
                status = order.get("status", "Ожидает")
                cake = order.get("cake", "Торт")
                bot.send_message(chat_id, f"Заказ {idx} - {status}:\n{cake}\nЦена: {order.get('price', 0)}₽")
        else:
            bot.send_message(chat_id, "У вас нет заказов.")
    elif data == "custom":
        start_custom_cake(bot, call)
    elif data.startswith("order_ready_"):
        cake_name = data.replace("order_ready_", "")
        order = {"cake": cake_name, "price": next(c["price"] for c in READY_CAKES if c["name"] == cake_name), "status": "Ожидает"}
        save_order_to_data(chat_id, order)
        bot.send_message(chat_id, f"Заказ на {cake_name} успешно оформлен! ✅", reply_markup=get_main_menu())
    elif data == "back_to_main":
        bot.send_message(chat_id, "Вы вернулись в главное меню:", reply_markup=get_main_menu())
    elif data.startswith("admin_order_"):
        if chat_id not in ADMINS:
            bot.send_message(chat_id, "У вас нет доступа к этой функции!")
            return
        order_key = int(data.split("_")[-1])
        send_admin_order_actions(chat_id, order_key)
    elif data.startswith("set_status_"):
        if chat_id not in ADMINS:
            bot.send_message(chat_id, "У вас нет доступа!")
            return
        _, order_key, status = data.split("_")
        order_key = int(order_key)
        set_order_status(order_key, status)
    else:
        handle_custom_cake_callback(bot, call, user_data)

@bot.message_handler(commands=["admin"])
def admin_panel(message):
    chat_id = message.chat.id
    if chat_id not in ADMINS:
        bot.send_message(chat_id, "У вас нет доступа к админке!")
        return
    data = load_data()
    users = data.get("users", {})
    if not users:
        bot.send_message(chat_id, "Нет заказов.")
        return
    for user_id, info in users.items():
        orders = info.get("orders", [])
        for idx, order in enumerate(orders):
            status = order.get("status", "Ожидает")
            cake = order.get("cake", "Торт")
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton("Ожидает", callback_data=f"set_status_{idx}_Ожидает")
            btn2 = types.InlineKeyboardButton("В процессе", callback_data=f"set_status_{idx}_В процессе")
            btn3 = types.InlineKeyboardButton("Доставлен", callback_data=f"set_status_{idx}_Доставлен")
            markup.row(btn1, btn2, btn3)
            bot.send_message(chat_id, f"Пользователь {user_id} - Заказ {idx+1}: {cake} ({status})", reply_markup=markup)

def send_admin_order_actions(chat_id, order_key):
    bot.send_message(chat_id, f"Вы можете изменить статус заказа {order_key}.")

def set_order_status(order_idx, new_status):
    data = load_data()
    for user_id, info in data.get("users", {}).items():
        orders = info.get("orders", [])
        if order_idx < len(orders):
            orders[order_idx]["status"] = new_status
            user_chat_id = int(user_id)
            bot.send_message(user_chat_id, f"Статус вашего заказа обновлен: {new_status}")
            save_data(data)
            return

@bot.message_handler(func=lambda message: True)
def handle_text(message):
    handle_custom_cake_text(bot, message, user_data)

if __name__ == "__main__":
    print("Бот запущен")
    bot.infinity_polling()