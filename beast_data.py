# beast_data.py – All beasts, stats, and skills

BEASTS = {
    "Primal Kong": {
        "rarity": "Legendary",
        "stars": 5,
        "barbarian_atk": 240,
        "barbarian_def": 240,
        "skills": ["Savage Strength", "Savage Onslaught"]
    },
    "Black Panthera": {
        "rarity": "Legendary",
        "stars": 5,
        "rider_atk": 219,
        "hunter_def": 219,
        "skills": ["Iron Cavalry Charge", "March Speed", "Rapid Charge"]
    },
    "Tyrant Tiger": {
        "rarity": "Legendary",
        "stars": 5,
        "barbarian_atk": 219,
        "rider_atk": 219,
        "skills": ["Wild Breath", "Iron Cavalry Charge", "Bloodthirsty Fury"]
    },
    "Frost Pterodactyl": {
        "rarity": "Epic",
        "stars": 4,
        "hunter_atk": 219,
        "hunter_def": 219,
        "skills": ["Predator Aim", "Punishing Arrows", "Clawed Retribution"]
    }
}

def get_beast_stats(beast_name):
    return BEASTS.get(beast_name, None)
