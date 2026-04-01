from telebot import types

def get_main_menu():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Каталог тортов", callback_data="catalog"))
    markup.add(types.InlineKeyboardButton("Создать свой торт", callback_data="custom"))
    markup.add(types.InlineKeyboardButton("Мои заказы", callback_data="orders"))
    return markup

def get_back_to_main():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("⬅ Главная", callback_data="main_menu"))
    return markup

def get_tier_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("1", callback_data="tier_1"),
        types.InlineKeyboardButton("2", callback_data="tier_2"),
        types.InlineKeyboardButton("3", callback_data="tier_3")
    )
    markup.add(types.InlineKeyboardButton("⬅ Назад", callback_data="main_menu"))
    return markup

def get_shape_keyboard():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Круг", callback_data="shape_round"),
        types.InlineKeyboardButton("Квадрат", callback_data="shape_square")
    )
    markup.add(types.InlineKeyboardButton("Овал", callback_data="shape_oval"))
    return markup

def get_topping_keyboard():
    markup = types.InlineKeyboardMarkup()
    toppings = [
        ("Черничный сироп", "topping_blueberry"),
        ("Клубничный сироп", "topping_strawberry"),
        ("Кленовый сироп", "topping_maple"),
        ("Карамельный сироп", "topping_caramel"),
        ("Молочный шоколад", "topping_milk_chocolate"),
        ("Белый соус", "topping_white_sauce"),
        ("Без топпинга", "topping_none")
    ]
    for name, data in toppings:
        markup.add(types.InlineKeyboardButton(name, callback_data=data))
    markup.add(types.InlineKeyboardButton("⬅ Назад", callback_data="main_menu"))
    return markup

def get_berries_keyboard():
    markup = types.InlineKeyboardMarkup()
    berries = [
        ("Клубника 🍓", "berry_strawberry"),
        ("Голубика 🫐", "berry_blueberry"),
        ("Малина 🍇", "berry_raspberry"),
        ("Ежевика", "berry_blackberry"),
        ("Без ягод", "berry_none")
    ]
    for name, data in berries:
        markup.add(types.InlineKeyboardButton(name, callback_data=data))
    markup.add(types.InlineKeyboardButton("⬅ Назад", callback_data="main_menu"))
    return markup

def get_decor_keyboard():
    markup = types.InlineKeyboardMarkup()
    decor = [
        ("Добавить надпись", "add_writing"),
        ("Марципан", "marzipan"),
        ("Пекан", "pecan"),
        ("Фундук", "hazelnut"),
        ("Безе", "meringue"),
        ("Фисташки", "pistachios"),
        ("Без декора", "without_decor")
    ]
    for name, data in decor:
        markup.add(types.InlineKeyboardButton(name, callback_data=data))
    markup.add(types.InlineKeyboardButton("⬅ Назад", callback_data="main_menu"))
    return markup