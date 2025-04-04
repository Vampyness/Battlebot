# battle_math_engine.py

from stat_booster import get_total_stat_bonus

BASE_STATS = {
    "Rider": {"attack": 100, "defense": 80, "health": 60},
    "Hunter": {"attack": 90, "defense": 70, "health": 50},
    "Barbarian": {"attack": 110, "defense": 90, "health": 70},
    "Behemoth": {"attack": 85, "defense": 100, "health": 100}
}

def apply_bonuses(troop_type, ritual_level, vip_level, title, relic_levels):
    base = BASE_STATS[troop_type]
    bonus = get_total_stat_bonus(troop_type, ritual_level, vip_level, title, relic_levels)

    final_stats = {
        "attack": round(base["attack"] * (1 + bonus["attack"] / 100), 2),
        "defense": round(base["defense"] * (1 + bonus["defense"] / 100), 2),
        "health": round(base["health"] * (1 + bonus["health"] / 100), 2),
        "damage": round(bonus["damage"], 2)
    }
    return final_stats
