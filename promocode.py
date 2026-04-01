from utils import load_data, save_data

def apply_promo(order, code):
    promos = {
        "SPRING10": 0.1,
        "HAPPY15": 0.15
    }
    discount = promos.get(code.upper())
    if discount:
        order["price"] = int(order["price"] * (1 - discount))
        order["promo_code"] = code.upper()
        return True, f"Промокод применён! Новая цена: {order['price']} ₽"
    return False, "Промокод некорректен."