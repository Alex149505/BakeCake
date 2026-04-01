from telebot import types

READY_CAKES = [
    {"name": "Шоколадный торт", "price": 1200, "photo": "images/chocolate.jpg"},
    {"name": "Фруктовый торт", "price": 1500, "photo": "images/fruit.jpg"},
    {"name": "Карамельный торт", "price": 1100, "photo": "images/caramel.jpg"}
]

def show_ready_cakes(bot, chat_id):
    for cake in READY_CAKES:
        markup = types.InlineKeyboardMarkup()
        btn_order = types.InlineKeyboardButton("Заказать", callback_data=f"order_ready_{cake['name']}")
        markup.add(btn_order)
        with open(cake['photo'], 'rb') as photo:
            bot.send_photo(chat_id, photo, caption=f"{cake['name']} - {cake['price']}₽", reply_markup=markup)