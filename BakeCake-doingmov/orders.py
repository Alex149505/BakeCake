from utils import get_user_orders, save_order_to_data

def save_order(chat_id, order_data):
    order_data["status"] = "new"
    save_order_to_data(chat_id, order_data)

def get_user_orders_list(chat_id):
    return get_user_orders(chat_id)