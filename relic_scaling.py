# relic_scaling.py

# Berserk adds +5% to all relic bonuses
BERSERK_BONUS = 1.05

RELICS = {
    "Axe": {"attack": 1.0, "defense": 1.0, "damage": 1.0, "max_level": 60},
    "Shield": {"attack": 1.0, "defense": 1.0, "health": 1.0, "max_level": 60},
    "Helmet": {"attack": 1.0, "defense": 1.0, "squad_size": 3200, "max_level": 60},
    "Armor": {"attack": 1.0, "defense": 1.0, "rally_size": 32000, "max_level": 60},
    "Necklace": {"attack": 1.0, "defense": 1.0, "healer_capacity": 8000, "max_level": 60},
    "Boots": {"attack": 1.0, "defense": 1.0, "march_speed": 4.0, "max_level": 60}
}

def get_relic_bonus(relic_levels: dict, berserk_enabled=True):
    bonus = {"attack": 0, "defense": 0, "damage": 0, "health": 0}
    for name, level in relic_levels.items():
        if name not in RELICS:
            continue
        relic = RELICS[name]
        scale = BERSERK_BONUS if berserk_enabled else 1.0
        for stat in bonus:
            if stat in relic:
                bonus[stat] += relic[stat] * level * scale
    return {k: round(v, 2) for k, v in bonus.items()}
