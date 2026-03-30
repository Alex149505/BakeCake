from telebot import types

def register_profile_handlers(bot):

    # обновление профиля
    def update_user_field(user_id, field, value):
        data = load_data()
        user_id = str(user_id)

        if "users" not in data:
            data["users"] = {}

        if user_id not in data["users"]:
            data["users"][user_id] = {}

        data["users"][user_id][field] = value
        save_data(data)

    # клавиатура профиля
    def profile_kb():
        markup = types.InlineKeyboardMarkup()

        markup.add(
            types.InlineKeyboardButton("✏️ Имя", callback_data="edit_name"),
            types.InlineKeyboardButton("📞 Телефон", callback_data="edit_phone"),
        )
        markup.add(
            types.InlineKeyboardButton("📍 Адрес", callback_data="edit_address")
        )

        return markup

    # кнопка отмены
    def cancel_kb():
        markup = types.InlineKeyboardMarkup()
        markup.add(
            types.InlineKeyboardButton("❌ Отмена", callback_data="cancel")
        )
        return markup

    # отправка профиля
    def send_profile(chat_id, user):
        text = f"""
👤 Личный кабинет

Имя: {user.get('name') or 'не указано'}
Телефон: {user.get('phone') or 'не указан'}
Адрес: {user.get('address') or 'не указан'}
"""
        bot.send_message(chat_id, text, reply_markup=profile_kb())

    # команда /profile
    @bot.message_handler(commands=["profile"])
    def profile(message):
        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)

    # обработка INLINE кнопок
    @bot.callback_query_handler(func=lambda call: True)
    def handle_callbacks(call):
        user = get_or_create_user(call.from_user.id)

        # чтобы убрать "часики" в Telegram
        bot.answer_callback_query(call.id)

        if call.data == "edit_name":
            msg = bot.send_message(
                call.message.chat.id,
                "Введите имя:",
                reply_markup=cancel_kb()
            )
            bot.register_next_step_handler(msg, save_name)

        elif call.data == "edit_phone":
            msg = bot.send_message(
                call.message.chat.id,
                "Введите телефон в формате +7999...",
                reply_markup=cancel_kb()
            )
            bot.register_next_step_handler(msg, save_phone)

        elif call.data == "edit_address":
            msg = bot.send_message(
                call.message.chat.id,
                "Введите адрес:",
                reply_markup=cancel_kb()
            )
            bot.register_next_step_handler(msg, save_address)

        elif call.data == "cancel":
            bot.send_message(call.message.chat.id, "Действие отменено ❌")
            send_profile(call.message.chat.id, user)

    # save данных

    def save_name(message):
        if len(message.text) < 2:
            msg = bot.send_message(message.chat.id, "Имя слишком короткое, попробуйте снова:")
            bot.register_next_step_handler(msg, save_name)
            return

        update_user_field(message.from_user.id, "name", message.text)

        bot.send_message(message.chat.id, "Имя сохранено ✅")

        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)

    def save_phone(message):
        if not message.text.startswith("+") or len(message.text) < 10:
            msg = bot.send_message(message.chat.id, "Некорректный телефон, попробуйте снова:")
            bot.register_next_step_handler(msg, save_phone)
            return

        update_user_field(message.from_user.id, "phone", message.text)

        bot.send_message(message.chat.id, "Телефон сохранен ✅")

        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)

    def save_address(message):
        if len(message.text) < 5:
            msg = bot.send_message(message.chat.id, "Адрес слишком короткий, попробуйте снова:")
            bot.register_next_step_handler(msg, save_address)
            return

        update_user_field(message.from_user.id, "address", message.text)

        bot.send_message(message.chat.id, "Адрес сохранен ✅")

        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)
