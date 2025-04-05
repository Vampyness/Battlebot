# image_handler.py
import discord
from report_ocr import extract_battle_data
from stat_sheet_parser import parse_stat_sheet

async def handle_image_upload(message):
    if not message.attachments:
        await message.channel.send("Please upload a screenshot with your command.")
        return

    image = message.attachments[0]
    await image.save("temp_report.png")
    text = extract_battle_data("temp_report.png")
    stats = parse_stat_sheet(text)

    formatted_stats = "\n".join([f"{k.title()}: {v}%" for k, v in stats.items()])
    response = f"**Parsed Stat Sheet:**\n{formatted_stats}\n\nType `!applystats` to use these in your next sim."

    # Save to temporary file for session use (can be replaced with DB)
    with open("latest_stats.json", "w") as f:
        import json
        json.dump(stats, f, indent=2)

    await message.author.send(response)
