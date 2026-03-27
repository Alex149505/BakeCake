def register_profile_handlers(bot):

    CANCEL_TEXT = "❌ Отмена"

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

    def send_profile(chat_id, user):
        text = f"""
👤 Личный кабинет

Имя: {user.get('name') or 'не указано'}
Телефон: {user.get('phone') or 'не указан'}
Адрес: {user.get('address') or 'не указан'}
"""
        bot.send_message(chat_id, text, reply_markup=profile_kb())

    def cancel_kb():
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(CANCEL_TEXT)
        return markup

    # профиль

    @bot.message_handler(commands=["profile"])
    def profile(message):
        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)

    # универсальная отмена

    @bot.message_handler(func=lambda m: m.text == CANCEL_TEXT)
    def cancel(message):
        user = get_or_create_user(message.from_user.id)
        bot.send_message(message.chat.id, "Действие отменено ❌")
        send_profile(message.chat.id, user)

    # изменение имени

    @bot.message_handler(func=lambda m: m.text == "✏️ Изменить имя")
    def change_name(message):
        msg = bot.send_message(
            message.chat.id,
            "Введите имя:",
            reply_markup=cancel_kb()
        )
        bot.register_next_step_handler(msg, save_name)

    def save_name(message):
        if message.text == CANCEL_TEXT:
            cancel(message)
            return

        if len(message.text) < 2:
            msg = bot.send_message(message.chat.id, "Имя слишком короткое, попробуйте снова:")
            bot.register_next_step_handler(msg, save_name)
            return

        update_user_field(message.from_user.id, "name", message.text)

        bot.send_message(message.chat.id, "Имя сохранено ✅")

        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)

    # телефон

    @bot.message_handler(func=lambda m: m.text == "📞 Изменить телефон")
    def change_phone(message):
        msg = bot.send_message(
            message.chat.id,
            "Введите телефон в формате +7999...",
            reply_markup=cancel_kb()
        )
        bot.register_next_step_handler(msg, save_phone)

    def save_phone(message):
        if message.text == CANCEL_TEXT:
            cancel(message)
            return

        if not message.text.startswith("+") or len(message.text) < 10:
            msg = bot.send_message(message.chat.id, "Некорректный телефон, попробуйте снова:")
            bot.register_next_step_handler(msg, save_phone)
            return

        update_user_field(message.from_user.id, "phone", message.text)

        bot.send_message(message.chat.id, "Телефон сохранен ✅")

        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)

    # адрес

    @bot.message_handler(func=lambda m: m.text == "📍 Изменить адрес")
    def change_address(message):
        msg = bot.send_message(
            message.chat.id,
            "Введите адрес:",
            reply_markup=cancel_kb()
        )
        bot.register_next_step_handler(msg, save_address)

    def save_address(message):
        if message.text == CANCEL_TEXT:
            cancel(message)
            return

        if len(message.text) < 5:
            msg = bot.send_message(message.chat.id, "Адрес слишком короткий, попробуйте снова:")
            bot.register_next_step_handler(msg, save_address)
            return

        update_user_field(message.from_user.id, "address", message.text)

        bot.send_message(message.chat.id, "Адрес сохранен ✅")

        user = get_or_create_user(message.from_user.id)
        send_profile(message.chat.id, user)