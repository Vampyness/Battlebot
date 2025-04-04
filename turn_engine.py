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
# turn_engine.py

from random import random

def simulate_turns(attacker, defender, atk_boosts, def_boosts, beast_skills, turns=3):
    result_log = []
    wounded = {'attacker': 0, 'defender': 0}

    for t in range(turns):
        turn_log = f"**Turn {t+1}**\n"

        atk_total = 0
        def_total = 0

        for troop in attacker:
            atk_mod = sum(atk_boosts.get(troop['type'], [])) + sum(beast_skills.get(troop['type'], {}).get('atk', []))
            base = troop['ATK']
            # Smash: 10% chance to triple
            if troop['tier'] == 'T9' and troop['type'] == 'Barbarian' and random() < 0.1:
                base *= 3
                turn_log += "- Smash triggered! (3x ATK)\n"
            atk_total += base * (1 + atk_mod / 100) * troop['count']

        for troop in defender:
            def_mod = sum(def_boosts.get(troop['type'], [])) + sum(beast_skills.get(troop['type'], {}).get('def', []))
            base = troop['DEF']
            def_total += base * (1 + def_mod / 100) * troop['count']

        wounded_ratio = atk_total / (def_total + 1)
        wounded_def = int(wounded_ratio * 0.15)
        wounded['defender'] += wounded_def

        wounded_ratio_def = def_total / (atk_total + 1)
        wounded_att = int(wounded_ratio_def * 0.15)
        wounded['attacker'] += wounded_att

        turn_log += f"- Damage Done (ATK): {atk_total:.0f}\n"
        turn_log += f"- Damage Taken (DEF): {def_total:.0f}\n"
        turn_log += f"- Estimated Defender Wounded: {wounded_def}\n"
        turn_log += f"- Estimated Attacker Wounded: {wounded_att}\n"

        result_log.append(turn_log)

    return result_log, wounded

