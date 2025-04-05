# troop_data.py

TROOP_STATS = {
    # Barbarian Troops
    'guard10': {'type': 'Barbarian', 'tier': 'T10', 'ATK': 49, 'DEF': 114},
    'guard7': {'type': 'Barbarian', 'tier': 'T7', 'ATK': 29, 'DEF': 68},
    'warrior9': {'type': 'Barbarian', 'tier': 'T9', 'ATK': 84, 'DEF': 49},
    'warrior8': {'type': 'Barbarian', 'tier': 'T8', 'ATK': 70, 'DEF': 41},

    # Rider Troops
    'rider9': {'type': 'Rider', 'tier': 'T9', 'ATK': 91, 'DEF': 49},
    'vanguard10': {'type': 'Rider', 'tier': 'T10', 'ATK': 90, 'DEF': 65},
    'vanguard8': {'type': 'Rider', 'tier': 'T8', 'ATK': 64, 'DEF': 34},

    # Behemoth Troops
    'marauder9': {'type': 'Behemoth', 'tier': 'T9', 'ATK': 48, 'DEF': 70},
    'raider10': {'type': 'Behemoth', 'tier': 'T10', 'ATK': 164, 'DEF': 73},

    # Hunter Troops
    'archer10': {'type': 'Hunter', 'tier': 'T10', 'ATK': 65, 'DEF': 49},
    'archer8': {'type': 'Hunter', 'tier': 'T8', 'ATK': 47, 'DEF': 35},
    'javelineer9': {'type': 'Hunter', 'tier': 'T9', 'ATK': 98, 'DEF': 49},
    'javelineer7': {'type': 'Hunter', 'tier': 'T7', 'ATK': 68, 'DEF': 34}
}


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

# troop_data.py

TROOP_STATS = {
    # Barbarian Troops
    'guard10': {'type': 'Barbarian', 'tier': 'T10', 'ATK': 49, 'DEF': 114},
    'guard7': {'type': 'Barbarian', 'tier': 'T7', 'ATK': 29, 'DEF': 68},
    'warrior9': {'type': 'Barbarian', 'tier': 'T9', 'ATK': 84, 'DEF': 49},
    'warrior8': {'type': 'Barbarian', 'tier': 'T8', 'ATK': 70, 'DEF': 41},

    # Rider Troops
    'rider9': {'type': 'Rider', 'tier': 'T9', 'ATK': 91, 'DEF': 49},
    'vanguard10': {'type': 'Rider', 'tier': 'T10', 'ATK': 90, 'DEF': 65},
    'vanguard8': {'type': 'Rider', 'tier': 'T8', 'ATK': 64, 'DEF': 34},

    # Behemoth Troops
    'marauder9': {'type': 'Behemoth', 'tier': 'T9', 'ATK': 48, 'DEF': 70},
    'raider10': {'type': 'Behemoth', 'tier': 'T10', 'ATK': 164, 'DEF': 73},

    # Hunter Troops
    'archer10': {'type': 'Hunter', 'tier': 'T10', 'ATK': 65, 'DEF': 49},
    'archer8': {'type': 'Hunter', 'tier': 'T8', 'ATK': 47, 'DEF': 35},
    'javelineer9': {'type': 'Hunter', 'tier': 'T9', 'ATK': 98, 'DEF': 49},
    'javelineer7': {'type': 'Hunter', 'tier': 'T7', 'ATK': 68, 'DEF': 34}
}

