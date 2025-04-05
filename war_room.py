# war_room.py
import json
import os

WAR_FILE = "warroom_targets.json"

def load_war_data():
    if os.path.exists(WAR_FILE):
        with open(WAR_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_war_data(data):
    with open(WAR_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def create_target(tag):
    data = load_war_data()
    if tag not in data:
        data[tag] = {"notes": "", "formation": "", "beasts": ""}
        save_war_data(data)
        return True
    return False

def update_target(tag, notes=None, formation=None, beasts=None):
    data = load_war_data()
    if tag not in data:
        return False
    if notes:
        data[tag]["notes"] = notes
    if formation:
        data[tag]["formation"] = formation
    if beasts:
        data[tag]["beasts"] = beasts
    save_war_data(data)
    return True

def get_target(tag):
    return load_war_data().get(tag, None)

def delete_target(tag):
    data = load_war_data()
    if tag in data:
        del data[tag]
        save_war_data(data)
        return True
    return False
