from db.db import get_or_create_user, load_data, save_data
from keyboards.keyboards import profile_kb


def register_profile_handlers(bot):

    @bot.message_handler(commands=["profile"])
    def profile(message):
        user = get_or_create_user(message.from_user.id)

        text = f"""
👤 Личный кабинет

Имя: {user['name'] or 'не указано'}
Телефон: {user['phone'] or 'не указан'}
Адрес: {user['address'] or 'не указан'}
"""
        bot.send_message(message.chat.id, text, reply_markup=profile_kb())

    # изменение имени 
    @bot.message_handler(func=lambda m: m.text == "✏️ Изменить имя")
    def change_name(message):
        msg = bot.send_message(message.chat.id, "Введите имя:")
        bot.register_next_step_handler(msg, save_name)

    def save_name(message):
        data = load_data()
        user_id = str(message.from_user.id)

        data["users"][user_id]["name"] = message.text
        save_data(data)

        bot.send_message(message.chat.id, "Имя сохранено ✅")

    # телефон 
    @bot.message_handler(func=lambda m: m.text == "📞 Изменить телефон")
    def change_phone(message):
        msg = bot.send_message(message.chat.id, "Введите телефон:")
        bot.register_next_step_handler(msg, save_phone)

    def save_phone(message):
        data = load_data()
        user_id = str(message.from_user.id)

        data["users"][user_id]["phone"] = message.text
        save_data(data)

        bot.send_message(message.chat.id, "Телефон сохранен ✅")

    # адрес 
    @bot.message_handler(func=lambda m: m.text == "📍 Изменить адрес")
    def change_address(message):
        msg = bot.send_message(message.chat.id, "Введите адрес:")
        bot.register_next_step_handler(msg, save_address)

    def save_address(message):
        data = load_data()
        user_id = str(message.from_user.id)

        data["users"][user_id]["address"] = message.text
        save_data(data)

        bot.send_message(message.chat.id, "Адрес сохранен ✅")