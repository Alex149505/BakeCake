from telebot import types


def get_main_menu():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "Каталог тортов", callback_data="catalog")
    btn2 = types.InlineKeyboardButton(
        "Создать свой торт", callback_data="custom")
    btn3 = types.InlineKeyboardButton("Мои заказы", callback_data="orders")

    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)

    return markup


def get_tier_keyboard():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("1", callback_data="tier_1")
    btn2 = types.InlineKeyboardButton("2", callback_data="tier_2")
    btn3 = types.InlineKeyboardButton("3", callback_data="tier_3")

    markup.row(btn1, btn2, btn3)

    return markup


def get_shape_keyboard():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton("Круг", callback_data="shape_round")
    btn2 = types.InlineKeyboardButton("Квадрат", callback_data="shape_square")
    btn3 = types.InlineKeyboardButton("Овал", callback_data="shape_oval")

    markup.row(btn1, btn2)
    markup.row(btn3)

    return markup


def get_topping_keyboard():
    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "Черничный сироп", callback_data="topping_blueberry")
    btn2 = types.InlineKeyboardButton(
        "Клубничный сироп", callback_data="topping_strawberry")
    btn3 = types.InlineKeyboardButton(
        "Кленовый сироп", callback_data="topping_maple")
    btn4 = types.InlineKeyboardButton(
        "Карамельный сироп", callback_data="topping_caramel")
    btn5 = types.InlineKeyboardButton(
        "Молочный шоколад", callback_data="topping_milk_chocolate")
    btn6 = types.InlineKeyboardButton(
        "Белый соус", callback_data="topping_white_sauce")
    btn7 = types.InlineKeyboardButton(
        "Без топпинга", callback_data="topping_none")

    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    markup.row(btn4)
    markup.row(btn5)
    markup.row(btn6)
    markup.row(btn7)

    return markup


def get_berries_keyboard():

    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "клубника", callback_data="strawberry")
    btn2 = types.InlineKeyboardButton(
        "голубика", callback_data="blackberry")
    btn3 = types.InlineKeyboardButton(
        "малина", callback_data="raspberry")
    btn4 = types.InlineKeyboardButton(
        "ежевика", callback_data="dewberry")
    btn5 = types.InlineKeyboardButton(
        "без ягод", callback_data="berries_none")

    markup.row(btn1, btn2)
    markup.row(btn3, btn4, btn5)

    return markup

def get_decor_keyboard():

    markup = types.InlineKeyboardMarkup()

    btn1 = types.InlineKeyboardButton(
        "добавить надпись", callback_data="add_writing")
    btn2 = types.InlineKeyboardButton("марципан", callback_data="marzipan")
    btn3 = types.InlineKeyboardButton("пекан", callback_data="pecan")
    btn4 = types.InlineKeyboardButton("фундук", callback_data="huzlenut")
    btn5 = types.InlineKeyboardButton("безе", callback_data="meringue")
    btn6 = types.InlineKeyboardButton(
        "фисташки", callback_data="pistachios")
    btn7 = types.InlineKeyboardButton(
        "без декора", callback_data="without_decor")

    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6, btn7) 

    return markup      
