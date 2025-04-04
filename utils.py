
# utils.py

def apply_skill_modifiers(troops, skills):
    for troop in troops:
        if troop['tier'] == 'T10' and troop['type'] == 'Behemoth':
            if 'Spikehide' in skills:
                troop['DEF'] *= 1.10  # Example boost
    return troops
