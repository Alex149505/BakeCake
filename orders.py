user_orders = {}

def save_order(chat_id, order_data):
    if chat_id not in user_orders:
        user_orders[chat_id] = []
    user_orders[chat_id].append(order_data)

def get_user_orders(chat_id):
    return user_orders.get(chat_id, [])