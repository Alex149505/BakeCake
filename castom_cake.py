from keyboards import get_tier_keyboard, get_shape_keyboard, get_topping_keyboard, get_berries_keyboard, get_decor_keyboard, get_main_menu
from utils import user_data, save_order_to_data

def start_custom_cake(bot, call):
    chat_id = call.message.chat.id
    bot.send_message(chat_id, "Выберите количество уровней:", reply_markup=get_tier_keyboard())

def handle_custom_cake_callback(bot, call, user_data):
    chat_id = call.message.chat.id
    data = call.data

    if chat_id not in user_data:
        user_data[chat_id] = {}

    # Выбор уровня
    if data.startswith("tier_"):
        user_data[chat_id]["tier"] = data.replace("tier_", "")
        bot.send_message(chat_id, "Выберите форму торта:", reply_markup=get_shape_keyboard())

    # Выбор формы
    elif data.startswith("shape_"):
        user_data[chat_id]["shape"] = data.replace("shape_", "")
        bot.send_message(chat_id, "Выберите топпинг:", reply_markup=get_topping_keyboard())

    # Выбор топпинга
    elif data.startswith("topping_"):
        user_data[chat_id]["topping"] = data.replace("topping_", "")
        bot.send_message(chat_id, "Выберите ягоды:", reply_markup=get_berries_keyboard())

    # Выбор ягод
    elif data.startswith("berry_"):
        user_data[chat_id]["berries"] = data.replace("berry_", "")
        bot.send_message(chat_id, "Выберите декор:", reply_markup=get_decor_keyboard())

    # Добавление надписи
    elif data == "add_writing":
        user_data[chat_id]["waiting_for_text"] = True
        bot.send_message(chat_id, "Введите надпись для торта:")

    # Декор без надписи
    elif data in ["marzipan", "pecan", "huzlenut", "meringue", "pistachios", "without_decor"]:
        user_data[chat_id]["decor"] = data
        confirm_custom_order(bot, chat_id)

    elif data == "back_to_main":
        bot.send_message(chat_id, "Вы вернулись в главное меню:", reply_markup=get_main_menu())

def handle_custom_cake_text(bot, message, user_data):
    chat_id = message.chat.id
    if chat_id in user_data and user_data[chat_id].get("waiting_for_text"):
        user_data[chat_id]["writing"] = message.text
        user_data[chat_id]["waiting_for_text"] = False
        bot.send_message(chat_id, f"Надпись добавлена: {message.text}")
        # После надписи показать выбор декора
        bot.send_message(chat_id, "Теперь выберите декор:", reply_markup=get_decor_keyboard())

def confirm_custom_order(bot, chat_id):
    order = user_data.get(chat_id, {})
    description = f"Ваш кастомный торт:\n" \
                  f"- Уровень: {order.get('tier','-')}\n" \
                  f"- Форма: {order.get('shape','-')}\n" \
                  f"- Топпинг: {order.get('topping','-')}\n" \
                  f"- Ягоды: {order.get('berries','-')}\n" \
                  f"- Декор: {order.get('decor','-')}\n" \
                  f"- Надпись: {order.get('writing','-')}\n"
    order["status"] = "Ожидает"
    save_order_to_data(chat_id, order)
    bot.send_message(chat_id, f"{description}\nЗаказ успешно оформлен! ✅", reply_markup=get_main_menu())
    # Очистка временных данных
    user_data.pop(chat_id, None) 