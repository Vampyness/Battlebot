# rally_attack.py

def calculate_rally_attack(troops, beasts, buffs, enemy_stats):
    total_damage = 0
    for troop in troops:
        base_attack = troop['ATK']
        modifiers = 1 + buffs.get(troop['type'], 0) + beasts.get(troop['type'], {}).get('ATK_boost', 0)
        damage = base_attack * modifiers
        total_damage += damage
    reduced_by_defense = total_damage * (1 - enemy_stats.get('DEF_boost', 0))
    return reduced_by_defense
