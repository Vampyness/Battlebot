# stat_booster.py

from ritual_scaling import get_ritual_bonuses
from relic_scaling import get_relic_bonus

def get_vip_bonus(vip_level):
    atk_def = 2 * max(0, vip_level - 8)
    dmg_hp = max(0, vip_level - 10)
    return {"attack": atk_def, "defense": atk_def, "damage": dmg_hp, "health": dmg_hp}

def get_title_bonus(title):
    title_boosts = {
        "Arch Chief": {"attack": 15, "defense": 15, "health": 0, "damage": 0},
        "Slayer": {"attack": 10, "defense": 0, "damage": 5, "health": 0},
        "Sage": {"health": 5, "attack": 0, "defense": 0, "damage": 0},
        "Hero": {"attack": 15, "defense": 15, "health": 0, "damage": 0},
        "Beast Master": {"damage": 5, "attack": 0, "defense": 0, "health": 0},
    }
    return title_boosts.get(title, {"attack": 0, "defense": 0, "damage": 0, "health": 0})

def get_invoke_bonus():
    return {"attack": 140, "defense": 130, "damage": 17.5, "health": 17.5}

def get_total_stat_bonus(troop_type, ritual_level, vip_level, title, relic_levels, berserk_enabled=True):
    ritual = get_ritual_bonuses(ritual_level)[troop_type]
    vip = get_vip_bonus(vip_level)
    title_b = get_title_bonus(title)
    invoke = get_invoke_bonus()
    relic = get_relic_bonus(relic_levels, berserk_enabled)

    return {
        stat: round(ritual[stat] + vip[stat] + title_b[stat] + invoke[stat] + relic[stat], 2)
        for stat in ["attack", "defense", "damage", "health"]
    }
