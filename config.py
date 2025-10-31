import os
from dotenv import load_dotenv

# Load the .env file so env variables work locally & in Docker
load_dotenv()

# Discord Bot Basics
BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GUILD_ID = int(os.getenv("DISCORD_GUILD_ID", "0")) or None
NOTIFY_CHANNEL_ID = int(os.getenv("NOTIFY_CHANNEL_ID", "0"))


# API Keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OWM_KEY = os.getenv("OWM_KEY")  # OpenWeatherMap API Key

# Webhook auth
WEB_SECRET = os.getenv("WEB_SECRET", "change-me")
WEB_PORT = int(os.getenv("WEB_PORT", "8088"))

# Lavalink for music
LAVALINK_HOST = os.getenv("LAVALINK_HOST", "lavalink")
LAVALINK_PORT = int(os.getenv("LAVALINK_PORT", "2333"))
LAVALINK_PASS = os.getenv("LAVALINK_PASS", "youshallnotpass")

# Optional log file paths if you want game server notifications later
VALHEIM_LOG = os.getenv("VALHEIM_LOG", "/data/valheim/valheim.log")
MINECRAFT_LOG = os.getenv("MINECRAFT_LOG", "/data/minecraft/logs/latest.log")
