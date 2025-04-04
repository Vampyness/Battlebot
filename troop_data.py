# troop_data.py – All troop types, base stats, and skills

TROOPS = {
    "T9_Barbarian_Warrior": {
        "power": 360,
        "attack": 180,
        "defense": 200,
        "hp": 210,
        "speed": 100,
        "range": 1,
        "skills": ["Hamstring", "Savagery", "Smash", "Jump Slash"]
    },
    "T10_Rider_Vanguard": {
        "power": 400,
        "attack": 230,
        "defense": 180,
        "hp": 190,
        "speed": 110,
        "range": 1,
        "skills": ["Charge", "Agility", "Dodge", "Follow-up"]
    },
    "T9_Rider_Mounted_Archer": {
        "power": 360,
        "attack": 200,
        "defense": 170,
        "hp": 180,
        "speed": 115,
        "range": 2,
        "skills": ["Charge", "Agility", "Resource Battle", "Barrage"]
    },
    "T10_Hunter_Archer": {
        "power": 400,
        "attack": 240,
        "defense": 160,
        "hp": 150,
        "speed": 90,
        "range": 3,
        "skills": ["Burst", "Penetration", "Critical", "Phantom Arrow"]
    },
    "T10_Behemoth_Raider": {
        "power": 400,
        "attack": 200,
        "defense": 220,
        "hp": 250,
        "speed": 85,
        "range": 1,
        "skills": ["Toughness", "Max Load", "Siege Defence", "Spikehide"]
    }
}

def get_troop_stats(troop_name):
    return TROOPS.get(troop_name, None)
