# preset_handler.py
import json
import os

PRESET_FILE = "presets.json"

def load_presets():
    if os.path.exists(PRESET_FILE):
        with open(PRESET_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_presets(data):
    with open(PRESET_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def save_preset(user_id, name, atk, defend):
    data = load_presets()
    user_key = str(user_id)
    if user_key not in data:
        data[user_key] = {}
    data[user_key][name] = {'atk': atk, 'def': defend}
    save_presets(data)

def get_preset(user_id, name):
    data = load_presets()
    return data.get(str(user_id), {}).get(name)


# preset_handler.py
import json
import os

PRESET_FILE = "presets.json"

def load_presets():
    if os.path.exists(PRESET_FILE):
        with open(PRESET_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_presets(data):
    with open(PRESET_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def save_preset(user_id, name, atk, defend):
    data = load_presets()
    user_key = str(user_id)
    if user_key not in data:
        data[user_key] = {}
    data[user_key][name] = {'atk': atk, 'def': defend}
    save_presets(data)

def get_preset(user_id, name):
    data = load_presets()
    return data.get(str(user_id), {}).get(name)
