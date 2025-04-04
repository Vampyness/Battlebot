# formation_simulator.py – Layered troop battle simulation + Overflow + Kill Estimate

from battle_simulator import simulate_fight

TROOP_HP_DEF = {
    "Barbarian": 130,
    "Rider": 120,
    "Hunter": 110,
    "Behemoth": 150
}

def simulate_formation_side(formation_rows):
    total_score = 0
    row_outputs = []
    overflow_damage = 0

    for i, row in enumerate(formation_rows):
        row_result = simulate_fight(**row)
        row_score = row_result['total_power_score'] + overflow_damage

        durability = TROOP_HP_DEF.get(row['troop_type'], 120)
        kills_estimate = round(row_score / durability)
        overflow_damage = max(0, row_score * 0.10)

        total_score += row_score

        row_outputs.append({
            "row": i + 1,
            "score_with_overflow": round(row_score, 2),
            "overflow_passed": round(overflow_damage, 2),
            "kills_estimate": kills_estimate,
            **row_result
        })

    return total_score, row_outputs

def simulate_full_formation(attacker_formation, defender_formation):
    atk_score, atk_rows = simulate_formation_side(attacker_formation)
    def_score, def_rows = simulate_formation_side(defender_formation)

    if atk_score > def_score:
        result = "Attacker Wins"
    elif def_score > atk_score:
        result = "Defender Wins"
    else:
        result = "Draw"

    return {
        "attacker_rows": atk_rows,
        "defender_rows": def_rows,
        "attacker_total": round(atk_score, 2),
        "defender_total": round(def_score, 2),
        "result": result
    }
