from telebot import types

# Главная клавиатура
def get_main_menu():
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("Каталог тортов", callback_data="catalog"))
    markup.row(types.InlineKeyboardButton("Создать свой торт", callback_data="custom"))
    markup.row(types.InlineKeyboardButton("Мои заказы", callback_data="orders"))
    markup.row(types.InlineKeyboardButton("❌ Отменить", callback_data="cancel_agreement"))
    return markup

def get_back_to_main():
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("⬅ Главная", callback_data="back_to_main"))
    return markup

# Остальные клавиатуры добавляем кнопку «Главная» внизу
def add_main_button(markup):
    markup.row(types.InlineKeyboardButton("⬅ Главная", callback_data="back_to_main"))
    return markup

def get_tier_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("1", callback_data="tier_1"),
               types.InlineKeyboardButton("2", callback_data="tier_2"),
               types.InlineKeyboardButton("3", callback_data="tier_3"))
    return add_main_button(markup)

def get_shape_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("Круг", callback_data="shape_round"),
               types.InlineKeyboardButton("Квадрат", callback_data="shape_square"),
               types.InlineKeyboardButton("Овал", callback_data="shape_oval"))
    return add_main_button(markup)

def get_topping_keyboard():
    markup = types.InlineKeyboardMarkup()
    toppings = [("Черничный сироп", "topping_blueberry"),
                ("Клубничный сироп", "topping_strawberry"),
                ("Кленовый сироп", "topping_maple"),
                ("Карамельный сироп", "topping_caramel"),
                ("Молочный шоколад", "topping_milk_chocolate"),
                ("Белый соус", "topping_white_sauce"),
                ("Без топпинга", "topping_none")]
    for name, data in toppings:
        markup.row(types.InlineKeyboardButton(name, callback_data=data))
    return add_main_button(markup)

def get_berries_keyboard():
    markup = types.InlineKeyboardMarkup()
    berries = [("Клубника 🍓", "berry_strawberry"),
               ("Голубика 🫐", "berry_blueberry"),
               ("Малина 🍇", "berry_raspberry"),
               ("Ежевика", "berry_blackberry"),
               ("Без ягод", "berry_none")]
    for name, data in berries:
        markup.row(types.InlineKeyboardButton(name, callback_data=data))
    return add_main_button(markup)

def get_decor_keyboard():
    markup = types.InlineKeyboardMarkup()
    decor = [("добавить надпись", "add_writing"),
             ("марципан", "marzipan"),
             ("пекан", "pecan"),
             ("фундук", "huzlenut"),
             ("безе", "meringue"),
             ("фисташки", "pistachios"),
             ("без декора", "without_decor")]
    for name, data in decor:
        markup.row(types.InlineKeyboardButton(name, callback_data=data))
    return add_main_button(markup)