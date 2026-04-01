import json
import os

user_data = {}
DATA_FILE = "data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_order_to_data(chat_id, order):
    data = load_data()
    str_id = str(chat_id)
    if "users" not in data:
        data["users"] = {}
    if str_id not in data["users"]:
        data["users"][str_id] = {"orders": []}
    data["users"][str_id]["orders"].append(order)
    save_data(data)

def get_user_orders(chat_id):
    data = load_data()
    str_id = str(chat_id)
    return data.get("users", {}).get(str_id, {}).get("orders", [])