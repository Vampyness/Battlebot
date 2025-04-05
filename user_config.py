# user_config.py
import json
import os

CONFIG_FILE = "user_config.json"

def load_user_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_user_config(data):
    with open(CONFIG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def set_user_title(user_id, title):
    data = load_user_config()
    uid = str(user_id)
    if uid not in data:
        data[uid] = {}
    data[uid]["title"] = title
    save_user_config(data)

def set_user_clan_status(user_id, status):
    data = load_user_config()
    uid = str(user_id)
    if uid not in data:
        data[uid] = {}
    data[uid]["clan"] = status
    save_user_config(data)

def set_user_relics(user_id, relic_levels):
    data = load_user_config()
    uid = str(user_id)
    if uid not in data:
        data[uid] = {}
    data[uid]["relics"] = relic_levels
    save_user_config(data)

def get_user_profile(user_id):
    return load_user_config().get(str(user_id), {})
