# battle_simulator.py – Full PvP Battle Formula + Skill Triggers

from battle_math_engine import apply_bonuses
from turn_engine import simulate_troop_skill, simulate_beast_trigger

DEFAULT_TURNS = 10

def simulate_fight(troop_type, count, ritual_level, vip_level, title, relic_levels, troop_skill=None, beast_skill=None):
    stats = apply_bonuses(troop_type, ritual_level, vip_level, title, relic_levels)
    total_base = stats['attack'] + stats['defense'] + stats['health']
    damage_factor = (1 + stats['damage'] / 100)

    skill_multiplier = simulate_troop_skill(troop_skill, DEFAULT_TURNS) if troop_skill else 1.0
    beast_bonus = simulate_beast_trigger(beast_skill, DEFAULT_TURNS) * count if beast_skill else 0

    raw_score = total_base * count
    with_damage = raw_score * damage_factor
    with_skills = with_damage * skill_multiplier
    final_score = with_skills + beast_bonus

    breakdown = {
        "base_stat_score": round(raw_score, 2),
        "with_damage": round(with_damage, 2),
        "after_skills": round(with_skills, 2),
        "beast_bonus": round(beast_bonus, 2),
        "total_power_score": round(final_score, 2),
        "troop_skill_multiplier": skill_multiplier,
        "beast_trigger_bonus": beast_bonus
    }
    return breakdown

def simulate_battle(attacker, defender):
    atk = simulate_fight(**attacker)
    defn = simulate_fight(**defender)

    atk_score = atk['total_power_score']
    def_score = defn['total_power_score']

    if atk_score > def_score:
        result = "Attacker Wins"
    elif def_score > atk_score:
        result = "Defender Wins"
    else:
        result = "Draw"

    return {
        "attacker": atk,
        "defender": defn,
        "result": result
    }
