# discord_bot.py
# Place final bot code with rally + solo support here
# Discord Bot Command Guide – Savage Survival Rally Simulator

---

## Bot File: discord_bot.py

### Purpose:
Allows players to run rally battle simulations using Discord commands.

### How It Works:
- Users type `!rallysimulate`
- Bot loads predefined troops and buffs (sample data)
- Calls rally simulator
- Returns damage and win/loss prediction

---

## Setup Instructions

1. Paste your real bot token into `TOKEN = '8ujVzDVORwPnoFqia9p7Dwub_FmUEZgF'`
2. Install dependencies:
```bash
pip install discord.py
```
3. Run the bot:
```bash
python discord_bot.py
```

---

## Usage in Discord

```
!rallysimulate
```

Response:
```
**Rally Sim Result**
Attack: 3,521,000
Defense: 2,980,000
Outcome: Victory
```

---

## Customization

To support DM commands:
Replace:
```python
@bot.event
async def on_message(message):
```
With:
```python
@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        # run simulation
```

---

## Notes

- Future updates will parse user inputs for dynamic simulations
- You can connect this to a database for saved presets and logs
- Visual embeds and reaction menus are also possible for upgrades


                                                    
# discord_bot.py
import discord
from rally_full_simulation import simulate_rally_battle

TOKEN = 'YOUR_BOT_TOKEN_HERE'

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rallysimulate'):
        # Sample dummy data
        attacker = [
            {'type': 'Rider', 'tier': 'T9', 'ATK': 91, 'DEF': 49, 'count': 30000},
            {'type': 'Barbarian', 'tier': 'T10', 'ATK': 49, 'DEF': 114, 'count': 35000}
        ]
        defender = [
            {'type': 'Behemoth', 'tier': 'T10', 'ATK': 164, 'DEF': 73, 'count': 40000},
            {'type': 'Hunter', 'tier': 'T9', 'ATK': 98, 'DEF': 49, 'count': 30000}
        ]
        atk_boosts = {
            'Rider': [140, 65, 10],
            'Barbarian': [140, 65, 10]
        }
        def_boosts = {
            'Behemoth': [130, 65, 10],
            'Hunter': [130, 65, 10]
        }
        beast_skills = {
            'Rider': {'atk': [25]},
            'Behemoth': {'def': [25]}
        }

        result = simulate_rally_battle(attacker, defender, atk_boosts, def_boosts, beast_skills)
        response = f"**Rally Sim Result**\nAttack: {result['adjusted_attack']:.0f}\nDefense: {result['adjusted_defense']:.0f}\nOutcome: {result['outcome']}"
        await message.channel.send(response)

bot.run(TOKEN)


