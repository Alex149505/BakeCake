from telebot import types
from utils import get_ready_cakes

def show_ready_cakes(bot, chat_id):
    cakes = get_ready_cakes()
    for cake in cakes:
        markup = types.InlineKeyboardMarkup()
        btn_order = types.InlineKeyboardButton("Заказать", callback_data=f"order_ready_{cake['name']}")
        markup.add(btn_order)
        bot.send_photo(chat_id, open(cake['photo'], 'rb'),
                       caption=f"{cake['name']} - {cake['price']}₽",
                       reply_markup=markup)