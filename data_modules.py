
def beast_trigger(beast_name, rider_pct):
    if beast_name == "Demon Rex":
        return {"triggers": 6, "kills": 12000 if rider_pct < 60 else 8000}
    elif beast_name == "ThunderBull":
        return {"triggers": 4, "kills": 10000 if rider_pct >= 30 else 6000}
    elif beast_name == "Crystarex":
        return {"triggers": 5, "kills": 9000}
    else:
        return {"triggers": 2, "kills": 3000}

def calculate_damage(attack, defense, damage_bonus=0):
    effective_attack = attack * (1 + damage_bonus / 100)
    return max(effective_attack - defense, 0)
def analyze_rally(attacker_troops, beast_combo, buffs):
    total_troops = sum(attacker_troops.values())
    rider_pct = sum(v for k, v in attacker_troops.items() if 'Rider' in k or 'Mounted Archer' in k) / total_troops * 100
    barb_pct = sum(v for k, v in attacker_troops.items() if 'Barb' in k or 'Warrior' in k or 'Guard' in k) / total_troops * 100

    beast_output = {}
    for beast in beast_combo:
        beast_output[beast] = beast_trigger(beast, rider_pct)

    total_kills = sum(data["kills"] for data in beast_output.values())
    has_guardians = any("Guard" in k for k in attacker_troops)
    wounded = int(0.25 * total_troops) if has_guardians else int(0.45 * total_troops)
    defender_loss_est = total_kills + int(0.15 * total_troops)

    summary = f"**Rally Simulation Result**\n"
    summary += f"Troops Sent: {total_troops:,}\n"
    summary += f"Rider %: {rider_pct:.1f}% | Barb %: {barb_pct:.1f}%\n"
    summary += f"Wounded: {wounded:,}\n"
    summary += f"Estimated Kills: {defender_loss_est:,}\n\n"
    for beast, data in beast_output.items():
        summary += f"• {beast}: {data['triggers']} triggers, ~{data['kills']} kills\n"

    return summary

TROOP_BASE_STATS = {
    'T10 Guardians': {'atk': 150, 'def': 450, 'hp': 300},
    'T9 Mounted Archers': {'atk': 400, 'def': 200, 'hp': 150},
    'T10 Archers': {'atk': 420, 'def': 180, 'hp': 160},
    # Add all troops here...
}
