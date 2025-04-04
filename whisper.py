
# Whisper + Input Parsing Guide for Savage Survival Discord Bot

---

## DM Whisper Support

- When a user types `!rallysimulate`, the bot calculates the result and DMs it privately.
- Main channel only sees: "Simulation sent to your DM."

---

## Input Command Format

```
!rallysimulate atk=rider9:30000,barb10:35000 def=behe10:40000,hunt9:30000
```

- `atk=` = Attacker troops
- `def=` = Defender troops
- Format: troopTypeTier:count
  - Example: `rider9:30000`

---

## Supported Troops (Base Stats Preloaded)

- `rider9` – Mounted Archers (T9)
- `barb10` – Guardians (T10)
- `behe10` – Raiders (T10)
- `hunt9` – Javelineers (T9)

---

## Notes

- Output includes adjusted ATK, DEF, and outcome.
- Future updates can expand supported troop dictionary or load from a stat file.
