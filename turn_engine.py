# turn_engine.py – Simulates skill triggers + cooldowns over battle turns

import random

# Example skill templates (can be expanded)
TROOP_SKILLS = {
    "Smash": {"multiplier": 3.0, "chance": 0.2, "cooldown": 3},
    "Critical": {"multiplier": 2.0, "chance": 0.25, "cooldown": 2},
    "Block": {"multiplier": 0.5, "chance": 0.3, "cooldown": 2},
}

BEAST_SKILLS = {
    "Savage Onslaught": {"bonus": 0.6, "target": "Barbarian", "cooldown": 3},
    "Bovine Charge": {"bonus": 0.3, "target": "Rider", "cooldown": 4},
    "Charging Rush": {"bonus": 0.8, "target": "Behemoth", "cooldown": 6}
}

def simulate_troop_skill(skill_name, turns):
    skill = TROOP_SKILLS.get(skill_name)
    if not skill:
        return 1.0
    total_multiplier = 0
    last_triggered = -99
    for t in range(1, turns + 1):
        if t - last_triggered >= skill['cooldown']:
            if random.random() < skill['chance']:
                total_multiplier += skill['multiplier']
                last_triggered = t
            else:
                total_multiplier += 1.0
        else:
            total_multiplier += 1.0
    return round(total_multiplier / turns, 3)

def simulate_beast_trigger(beast_skill, turns):
    data = BEAST_SKILLS.get(beast_skill)
    if not data:
        return 0.0
    triggers = turns // data['cooldown']
    return round(triggers * data['bonus'], 3)
