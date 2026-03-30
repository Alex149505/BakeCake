from keyboards import (
    get_tier_keyboard,
    get_shape_keyboard,
    get_topping_keyboard,
    get_berries_keyboard,
    get_decor_keyboard
)


def start_custom_cake(bot, call):
    bot.send_message(
        call.message.chat.id,
        "Выберите количество уровней:",
        reply_markup=get_tier_keyboard()
    )


def handle_custom_cake_callback(bot, call, user_data):
    chat_id = call.message.chat.id

    if call.data in ["tier_1", "tier_2", "tier_3"]:
        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]["tier"] = call.data

        bot.send_message(
            chat_id,
            "Выберите форму торта:",
            reply_markup=get_shape_keyboard()
        )

    elif call.data in ["shape_round", "shape_square", "shape_oval"]:
        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]["shape"] = call.data

        bot.send_message(
            chat_id,
            "Выберите топпинг:",
            reply_markup=get_topping_keyboard()
        )

    elif call.data in [
        "topping_blueberry",
        "topping_strawberry",
        "topping_maple",
        "topping_caramel",
        "topping_milk_chocolate",
        "topping_white_sauce",
        "topping_none"
    ]:
        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]["topping"] = call.data

        bot.send_message(
            chat_id,
            "Выберите ягоды:",
            reply_markup=get_berries_keyboard()
        )


    elif call.data in ["strawberry", "blackberry", "raspberry", "dewberry", "berries_none"]:
        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]["berries"] = call.data

        bot.send_message(
            chat_id,
            "Выберите декор:",
            reply_markup=get_decor_keyboard()
        )

    elif call.data == "add_writing":
        chat_id = call.message.chat.id

        if chat_id not in user_data:
            user_data[chat_id] = {}

        user_data[chat_id]["waiting_for_text"] = True

        bot.send_message(chat_id, "Введите надпись для торта:")



def handle_custom_cake_text(message, bot):
    chat_id = message.chat.id

    if chat_id in user_data and user_data[chat_id].get("waiting_for_text"):
        user_data[chat_id]["writing"] = message.text
        user_data[chat_id]["waiting_for_text"] = False

        bot.send_message(chat_id, f"Надпись добавлена: {message.text}")

    show_order_summary(bot, chat_id, user_data)


def show_order_summary(bot, chat_id, user_data):
    order = user_data.get(chat_id, {})

    summary = (
        f"Ваш заказ:\n"
        f"Уровни: {order.get('tier', 'не выбрано')}\n"
        f"Форма: {order.get('shape', 'не выбрано')}\n"
        f"Топпинг: {order.get('topping', 'не выбрано')}\n"
        f"Ягоды: {order.get('berries', 'не выбрано')}\n"
        f"Декор: {order.get('decor', 'не выбрано')}\n"
        f"Надпись: {order.get('writing', 'нет')}"
    )

    bot.send_message(chat_id, summary)       