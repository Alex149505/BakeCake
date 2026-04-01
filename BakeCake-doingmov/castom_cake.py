from keyboards import get_tier_keyboard, get_shape_keyboard, get_topping_keyboard, get_berries_keyboard, get_decor_keyboard
from utils import save_order_to_data

def start_custom_cake(bot, call):
    bot.send_message(call.message.chat.id, "Выберите количество уровней:", reply_markup=get_tier_keyboard())

def handle_custom_cake_callback(bot, call, state):
    chat_id = call.message.chat.id
    if chat_id not in state:
        state[chat_id] = {}

    if call.data.startswith("tier_"):
        state[chat_id]["tier"] = call.data
        bot.send_message(chat_id, "Выберите форму торта:", reply_markup=get_shape_keyboard())
    elif call.data.startswith("shape_"):
        state[chat_id]["shape"] = call.data
        bot.send_message(chat_id, "Выберите топпинг:", reply_markup=get_topping_keyboard())
    elif call.data.startswith("topping_"):
        state[chat_id]["topping"] = call.data
        bot.send_message(chat_id, "Выберите ягоды:", reply_markup=get_berries_keyboard())
    elif call.data.startswith("berry_"):
        state[chat_id]["berries"] = call.data
        bot.send_message(chat_id, "Выберите декор:", reply_markup=get_decor_keyboard())
    elif call.data in ["marzipan", "pecan", "hazelnut", "meringue", "pistachios", "without_decor"]:
        state[chat_id]["decor"] = call.data
        bot.send_message(chat_id, "Введите ваш телефон:")
        state[chat_id]["next_step"] = "phone"
    elif call.data == "add_writing":
        state[chat_id]["next_step"] = "writing"
        bot.send_message(chat_id, "Введите надпись для торта:")
    elif call.data == "main_menu":
        from keyboards import get_main_menu
        bot.send_message(chat_id, "Главное меню:", reply_markup=get_main_menu())

def handle_custom_cake_text(bot, message, state):
    chat_id = message.chat.id
    if chat_id not in state:
        state[chat_id] = {}

    step = state[chat_id].get("next_step")

    if step == "writing":
        state[chat_id]["writing"] = message.text
        bot.send_message(chat_id, "Надпись добавлена ✅")
        bot.send_message(chat_id, "Выберите декор:", reply_markup=get_decor_keyboard())
        state[chat_id]["next_step"] = None
    elif step == "phone":
        state[chat_id]["phone"] = message.text
        bot.send_message(chat_id, "Введите адрес доставки:")
        state[chat_id]["next_step"] = "address"
    elif step == "address":
        state[chat_id]["address"] = message.text
        bot.send_message(chat_id, "Укажите время доставки:")
        state[chat_id]["next_step"] = "time"
    elif step == "time":
        state[chat_id]["time"] = message.text
        # Сохраняем заказ
        order = {
            "cake": f"{state[chat_id].get('tier','')} {state[chat_id].get('shape','')}",
            "topping": state[chat_id].get("topping"),
            "berries": state[chat_id].get("berries"),
            "decor": state[chat_id].get("decor"),
            "writing": state[chat_id].get("writing"),
            "phone": state[chat_id].get("phone"),
            "address": state[chat_id].get("address"),
            "time": state[chat_id].get("time"),
            "status": "Новый"
        }
        save_order_to_data(chat_id, order)
        from keyboards import get_main_menu
        bot.send_message(chat_id, "Ваш заказ оформлен! ✅", reply_markup=get_main_menu())
        state.pop(chat_id)