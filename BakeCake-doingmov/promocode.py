from utils import load_data, save_data

def apply_promo(user_order, code):
    data = load_data()
    discount = data.get("promo_codes", {}).get(code.upper())
    if discount:
        price = user_order.get("price", 0)
        user_order["price"] = int(price * (1 - discount))
        return True, f"Промокод применён! Новая цена: {user_order['price']} руб."
    return False, "Промокод некорректен."