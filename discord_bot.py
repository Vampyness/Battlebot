# discord_bot.py
# Place final bot code with rally + solo support here
# Discord Bot Command Guide – Savage Survival Rally Simulator

---
# discord_bot.py
import discord
from rally_full_simulation import simulate_rally_battle

TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

# Troop stat reference (simplified)
TROOP_STATS = {
    'rider9': {'type': 'Rider', 'tier': 'T9', 'ATK': 91, 'DEF': 49},
    'barb10': {'type': 'Barbarian', 'tier': 'T10', 'ATK': 49, 'DEF': 114},
    'behe10': {'type': 'Behemoth', 'tier': 'T10', 'ATK': 164, 'DEF': 73},
    'hunt9': {'type': 'Hunter', 'tier': 'T9', 'ATK': 98, 'DEF': 49}
}

def parse_input_block(block):
    troops = []
    parts = block.split(',')
    for part in parts:
        if ':' not in part:
            continue
        key, count = part.split(':')
        key = key.lower()
        if key in TROOP_STATS:
            base = TROOP_STATS[key]
            troop = base.copy()
            troop['count'] = int(count)
            troops.append(troop)
    return troops

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rallysimulate'):
        try:
            content = message.content.replace('!rallysimulate', '').strip()
            args = dict(pair.split('=') for pair in content.split() if '=' in pair)
            atk = parse_input_block(args.get('atk', ''))
            defend = parse_input_block(args.get('def', ''))

            atk_boosts = {t['type']: [140, 65, 10] for t in atk}
            def_boosts = {t['type']: [130, 65, 10] for t in defend}
            beast_skills = {
                'Rider': {'atk': [25]},
                'Behemoth': {'def': [25]}
            }

            result = simulate_rally_battle(atk, defend, atk_boosts, def_boosts, beast_skills)
            response = f"**Rally Sim Result**\n\n**Adjusted ATK**: {result['adjusted_attack']:.0f}\n**Adjusted DEF**: {result['adjusted_defense']:.0f}\n**Outcome**: **{result['outcome']}**"

            # DM Whisper
            await message.author.send(response)
            await message.channel.send(f"Simulation sent to your DM, {message.author.mention}.")

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

bot.run(TOKEN)


# discord_bot.py
import discord
from rally_full_simulation import simulate_rally_battle
from turn_engine import simulate_turns
from troop_data import TROOP_STATS

TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

def parse_input_block(block):
    troops = []
    parts = block.split(',')
    for part in parts:
        if ':' not in part:
            continue
        key, count = part.split(':')
        key = key.lower()
        if key in TROOP_STATS:
            base = TROOP_STATS[key]
            troop = base.copy()
            troop['count'] = int(count)
            troops.append(troop)
    return troops

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rallysimulate'):
        try:
            content = message.content.replace('!rallysimulate', '').strip()
            args = dict(pair.split('=') for pair in content.split() if '=' in pair)
            atk = parse_input_block(args.get('atk', ''))
            defend = parse_input_block(args.get('def', ''))

            atk_boosts = {t['type']: [140, 65, 10] for t in atk}
            def_boosts = {t['type']: [130, 65, 10] for t in defend}
            beast_skills = {
                'Rider': {'atk': [25]},
                'Behemoth': {'def': [25]},
                'Barbarian': {'atk': [25]},
                'Hunter': {'atk': [25]}
            }

            result = simulate_rally_battle(atk, defend, atk_boosts, def_boosts, beast_skills)
            turn_logs, wounded = simulate_turns(atk, defend, atk_boosts, def_boosts, beast_skills, turns=3)

            report = f"**Rally Sim Result**\n\n"
            report += f"**Adjusted ATK**: {result['adjusted_attack']:.0f}\n"
            report += f"**Adjusted DEF**: {result['adjusted_defense']:.0f}\n"
            report += f"**Outcome**: **{result['outcome']}**\n"
            report += f"**Total Wounded (Attacker)**: {wounded['attacker']}\n"
            report += f"**Total Wounded (Defender)**: {wounded['defender']}\n\n"

            report += "\n".join(turn_logs)

            await message.author.send(report)
            await message.channel.send(f"Simulation sent to your DM, {message.author.mention}.")

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

bot.run(TOKEN)


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

1. Paste your real bot token into `TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'`
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

TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'

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

# discord_bot.py
import discord
from rally_full_simulation import simulate_rally_battle
from turn_engine import simulate_turns
from troop_data import TROOP_STATS

TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

def parse_input_block(block):
    troops = []
    parts = block.split(',')
    for part in parts:
        if ':' not in part:
            continue
        key, count = part.split(':')
        key = key.lower()
        if key in TROOP_STATS:
            base = TROOP_STATS[key]
            troop = base.copy()
            troop['count'] = int(count)
            troops.append(troop)
    return troops

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rallysimulate'):
        try:
            content = message.content.replace('!rallysimulate', '').strip()
            args = dict(pair.split('=') for pair in content.split() if '=' in pair)
            atk = parse_input_block(args.get('atk', ''))
            defend = parse_input_block(args.get('def', ''))

            atk_boosts = {t['type']: [140, 65, 10] for t in atk}
            def_boosts = {t['type']: [130, 65, 10] for t in defend}
            beast_skills = {
                'Rider': {'atk': [25]},
                'Behemoth': {'def': [25]},
                'Barbarian': {'atk': [25]},
                'Hunter': {'atk': [25]}
            }

            result = simulate_rally_battle(atk, defend, atk_boosts, def_boosts, beast_skills)
            turn_logs, wounded = simulate_turns(atk, defend, atk_boosts, def_boosts, beast_skills, turns=3)

            report = f"**Rally Sim Result**\n\n"
            report += f"**Adjusted ATK**: {result['adjusted_attack']:.0f}\n"
            report += f"**Adjusted DEF**: {result['adjusted_defense']:.0f}\n"
            report += f"**Outcome**: **{result['outcome']}**\n"
            report += f"**Total Wounded (Attacker)**: {wounded['attacker']}\n"
            report += f"**Total Wounded (Defender)**: {wounded['defender']}\n\n"

            report += "\n".join(turn_logs)

            await message.author.send(report)
            await message.channel.send(f"Simulation sent to your DM, {message.author.mention}.")

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

bot.run(TOKEN)


import discord
from rally_full_simulation import simulate_rally_battle

TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

# Troop stat reference (simplified)
TROOP_STATS = {
    'rider9': {'type': 'Rider', 'tier': 'T9', 'ATK': 91, 'DEF': 49},
    'barb10': {'type': 'Barbarian', 'tier': 'T10', 'ATK': 49, 'DEF': 114},
    'behe10': {'type': 'Behemoth', 'tier': 'T10', 'ATK': 164, 'DEF': 73},
    'hunt9': {'type': 'Hunter', 'tier': 'T9', 'ATK': 98, 'DEF': 49}
}

def parse_input_block(block):
    troops = []
    parts = block.split(',')
    for part in parts:
        if ':' not in part:
            continue
        key, count = part.split(':')
        key = key.lower()
        if key in TROOP_STATS:
            base = TROOP_STATS[key]
            troop = base.copy()
            troop['count'] = int(count)
            troops.append(troop)
    return troops

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rallysimulate'):
        try:
            content = message.content.replace('!rallysimulate', '').strip()
            args = dict(pair.split('=') for pair in content.split() if '=' in pair)
            atk = parse_input_block(args.get('atk', ''))
            defend = parse_input_block(args.get('def', ''))

            atk_boosts = {t['type']: [140, 65, 10] for t in atk}
            def_boosts = {t['type']: [130, 65, 10] for t in defend}
            beast_skills = {
                'Rider': {'atk': [25]},
                'Behemoth': {'def': [25]}
            }

            result = simulate_rally_battle(atk, defend, atk_boosts, def_boosts, beast_skills)
            response = f"**Rally Sim Result**\n\n**Adjusted ATK**: {result['adjusted_attack']:.0f}\n**Adjusted DEF**: {result['adjusted_defense']:.0f}\n**Outcome**: **{result['outcome']}**"

            # DM Whisper
            await message.author.send(response)
            await message.channel.send(f"Simulation sent to your DM, {message.author.mention}.")

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

bot.run(TOKEN)


# discord_bot.py
import discord
from rally_full_simulation import simulate_rally_battle

TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

# Troop stat reference (simplified)
TROOP_STATS = {
    'rider9': {'type': 'Rider', 'tier': 'T9', 'ATK': 91, 'DEF': 49},
    'barb10': {'type': 'Barbarian', 'tier': 'T10', 'ATK': 49, 'DEF': 114},
    'behe10': {'type': 'Behemoth', 'tier': 'T10', 'ATK': 164, 'DEF': 73},
    'hunt9': {'type': 'Hunter', 'tier': 'T9', 'ATK': 98, 'DEF': 49}
}

def parse_input_block(block):
    troops = []
    parts = block.split(',')
    for part in parts:
        if ':' not in part:
            continue
        key, count = part.split(':')
        key = key.lower()
        if key in TROOP_STATS:
            base = TROOP_STATS[key]
            troop = base.copy()
            troop['count'] = int(count)
            troops.append(troop)
    return troops

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rallysimulate'):
        try:
            content = message.content.replace('!rallysimulate', '').strip()
            args = dict(pair.split('=') for pair in content.split() if '=' in pair)
            atk = parse_input_block(args.get('atk', ''))
            defend = parse_input_block(args.get('def', ''))

            atk_boosts = {t['type']: [140, 65, 10] for t in atk}
            def_boosts = {t['type']: [130, 65, 10] for t in defend}
            beast_skills = {
                'Rider': {'atk': [25]},
                'Behemoth': {'def': [25]}
            }

            result = simulate_rally_battle(atk, defend, atk_boosts, def_boosts, beast_skills)
            response = f"**Rally Sim Result**\n\n**Adjusted ATK**: {result['adjusted_attack']:.0f}\n**Adjusted DEF**: {result['adjusted_defense']:.0f}\n**Outcome**: **{result['outcome']}**"

            # DM Whisper
            await message.author.send(response)
            await message.channel.send(f"Simulation sent to your DM, {message.author.mention}.")

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

bot.run(TOKEN)

# discord_bot.py
import discord
from rally_full_simulation import simulate_rally_battle
from turn_engine import simulate_turns
from troop_data import TROOP_STATS

TOKEN = 'MTM1NjAzMDg4MzM5MTQ3MTc4OQ.G5EEZb.6ucbeMhvw3rpumgtFbsao-3dOCv-84B9GgB3yw'
intents = discord.Intents.default()
intents.messages = True
bot = discord.Client(intents=intents)

def parse_input_block(block):
    troops = []
    parts = block.split(',')
    for part in parts:
        if ':' not in part:
            continue
        key, count = part.split(':')
        key = key.lower()
        if key in TROOP_STATS:
            base = TROOP_STATS[key]
            troop = base.copy()
            troop['count'] = int(count)
            troops.append(troop)
    return troops

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('!rallysimulate'):
        try:
            content = message.content.replace('!rallysimulate', '').strip()
            args = dict(pair.split('=') for pair in content.split() if '=' in pair)
            atk = parse_input_block(args.get('atk', ''))
            defend = parse_input_block(args.get('def', ''))

            atk_boosts = {t['type']: [140, 65, 10] for t in atk}
            def_boosts = {t['type']: [130, 65, 10] for t in defend}
            beast_skills = {
                'Rider': {'atk': [25]},
                'Behemoth': {'def': [25]},
                'Barbarian': {'atk': [25]},
                'Hunter': {'atk': [25]}
            }

            result = simulate_rally_battle(atk, defend, atk_boosts, def_boosts, beast_skills)
            turn_logs, wounded = simulate_turns(atk, defend, atk_boosts, def_boosts, beast_skills, turns=3)

            report = f"**Rally Sim Result**\n\n"
            report += f"**Adjusted ATK**: {result['adjusted_attack']:.0f}\n"
            report += f"**Adjusted DEF**: {result['adjusted_defense']:.0f}\n"
            report += f"**Outcome**: **{result['outcome']}**\n"
            report += f"**Total Wounded (Attacker)**: {wounded['attacker']}\n"
            report += f"**Total Wounded (Defender)**: {wounded['defender']}\n\n"

            report += "\n".join(turn_logs)

            await message.author.send(report)
            await message.channel.send(f"Simulation sent to your DM, {message.author.mention}.")

        except Exception as e:
            await message.channel.send(f"Error: {str(e)}")

bot.run(TOKEN)


