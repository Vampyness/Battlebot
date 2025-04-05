# battle_logger.py
import json
import os
from datetime import datetime

LOG_FILE = "battle_chain_log.json"

def load_logs():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_logs(data):
    with open(LOG_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def log_battle(user_id, target_name, result_summary):
    logs = load_logs()
    uid = str(user_id)
    if uid not in logs:
        logs[uid] = []
    timestamp = datetime.utcnow().isoformat()
    logs[uid].append({"target": target_name, "summary": result_summary, "time": timestamp})
    save_logs(logs)

def get_battle_chain(user_id, target_name=None):
    uid = str(user_id)
    logs = load_logs().get(uid, [])
    if target_name:
        return [log for log in logs if log["target"].lower() == target_name.lower()]
    return logs
