# coach.py

def suggest_formation(attacker, defender):
    advice = []
    for t in defender:
        if t['type'] == 'Barbarian' and t['tier'] == 'T10':
            advice.append("Consider shielding front with T10 Guardians.")
        if t['type'] == 'Hunter':
            advice.append("Avoid stacking Hunters if facing Riders.")
        if t['type'] == 'Rider':
            advice.append("Mix in Barbarians to counter heavy Riders.")
    if not advice:
        advice.append("Formation appears balanced. Fine-tune with layering.")
    return advice


# coach.py

on appears balanced. Fine-tune with layering.")
    return advice

def suggest_formation(attacker, defender):
    advice = []
    for t in defender:
        if t['type'] == 'Barbarian' and t['tier'] == 'T10':
            advice.append("Consider shielding front with T10 Guardians.")
        if t['type'] == 'Hunter':
            advice.append("Avoid stacking Hunters if facing Riders.")
        if t['type'] == 'Rider':
            advice.append("Mix in Barbarians to counter heavy Riders.")
    if not advice:
        advice.append("Formation appears balanced. Fine-tune with layering.")
    return advice
