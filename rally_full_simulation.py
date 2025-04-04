# rally_full_simulation.py

def calculate_effective_stat(base, boosts):
    return base * (1 + sum(boosts) / 100)

def simulate_rally_battle(attacking_troops, defending_troops, atk_boosts, def_boosts, beast_skills):
    attack_power = 0
    defense_power = 0
    formation_bonus = 1.0

    for troop in attacking_troops:
        atk_mods = atk_boosts.get(troop['type'], []) + beast_skills.get(troop['type'], {}).get('atk', [])
        troop_atk = calculate_effective_stat(troop['ATK'], atk_mods)
        attack_power += troop_atk * troop['count']

    for troop in defending_troops:
        def_mods = def_boosts.get(troop['type'], []) + beast_skills.get(troop['type'], {}).get('def', [])
        troop_def = calculate_effective_stat(troop['DEF'], def_mods)
        defense_power += troop_def * troop['count']

    if any(t['tier'] == 'T10' and t['type'] == 'Barbarian' for t in defending_troops):
        formation_bonus += 0.1  # defensive layering bonus

    adjusted_attack = attack_power
    adjusted_defense = defense_power * formation_bonus

    outcome = 'Victory' if adjusted_attack > adjusted_defense else 'Defeat'
    result = {
        'adjusted_attack': adjusted_attack,
        'adjusted_defense': adjusted_defense,
        'outcome': outcome
    }
    return result
