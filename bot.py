import discord
from discord.ext import commands
import os
from googletrans import Translator
from dotenv import load_dotenv

# Load environment variables (Discord Token)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up intents and bot
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Command to automatically detect the language and translate to English
@bot.command()
async def auto_translate(ctx, *, text):
    """ 
    Detects the language of the input text and responds in that language.
    """
    translator = Translator()

    try:
        # Detect the language of the text
        detected = translator.detect(text)
        detected_language = detected.lang  # Detected language code (e.g., 'en', 'es', etc.)

        # Translate the text to English (or change 'en' to any other language)
        translated = translator.translate(text, dest='en')  # Change 'en' to another language if needed
        response = f"Detected language: {detected_language}\nOriginal text: {text}\nTranslated to English: {translated.text}"

        # If the detected language is not English, translate the response to the detected language
        if detected_language != 'en':  # Check if the language is not English
            translated_response = translator.translate(response, dest=detected_language)
            response = translated_response.text

        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error detecting or translating: {e}")

# Command to display supported languages and their codes
@bot.command()
async def languages(ctx):
    """ 
    Shows the list of supported languages and their codes.
    """
    languages = """ 
    Supported Languages:
    - de: German
    - tl: Tagalog (Filipino)
    - id: Indonesian
    - ms: Malay
    - fr: French
    - es: Spanish
    - zh-CN: Simplified Chinese
    - ja: Japanese
    - en: English (Standard)
    """
    await ctx.send(languages)

# Command to test the bot
@bot.command()
async def hello(ctx):
    await ctx.send("Hello, I am BattleBot!")

# Start the bot
bot.run(TOKEN)
