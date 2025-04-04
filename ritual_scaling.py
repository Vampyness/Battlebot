# ritual_scaling.py

# Max ritual level is 20
# Each troop type scales independently: Barbarian, Rider, Hunter, Behemoth

# Scaling values per level
SCALING = {
    "attack": 2.0,
    "defense": 2.0,
    "damage": 0.5,
    "health": 0.5
}

def get_ritual_bonuses(ritual_level):
    if not (0 <= ritual_level <= 20):
        raise ValueError("Ritual level must be between 0 and 20")
    troop_types = ["Barbarian", "Rider", "Hunter", "Behemoth"]
    bonuses = {}
    for troop in troop_types:
        bonuses[troop] = {
            stat: round(ritual_level * value, 2)
            for stat, value in SCALING.items()
        }
    return bonuses
