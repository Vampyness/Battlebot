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

1. Paste your real bot token into `TOKEN = 'YOUR_BOT_TOKEN_HERE'`
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

