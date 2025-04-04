
# rally_defense.py

def calculate_rally_defense(troops, beasts, buffs, enemy_stats):
    total_defense = 0
    for troop in troops:
        base_def = troop['DEF']
        modifiers = 1 + buffs.get(troop['type'], 0) + beasts.get(troop['type'], {}).get('DEF_boost', 0)
        defense = base_def * modifiers
        total_defense += defense
    reduced_by_attack = total_defense * (1 - enemy_stats.get('ATK_boost', 0))
    return reduced_by_attack
