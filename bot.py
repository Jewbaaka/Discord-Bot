import discord
from discord.ext import commands
from config import BOT_TOKEN, GUILD_ID

# intents tell Discord what data your bot needs access to
INTENTS = discord.Intents.default()
INTENTS.message_content = True  # Enable access to message content
INTENTS.members = True  # Enable access to member data
INTENTS.guilds = True  # Enable access to guild data


class MyBot(commands.Bot):
    def __init__(self):
        # Command_prefix is used for older style commands
        # slash commands don't really need
        super()._init_(command_prefix="!", intents=INTENTS)

        async def setup_hook(self):
            # Load cogs (files from cogs folder)
            extensions = [
                "cogs.moderation",
                "cogs.news",
                "cogs.stocks",
                "cogs.weather",
                "cogs.music",
                "cogs.arr_notify",
                "cogs.memes"
            ]

            for ext in extensions:
                try:
                    await self.load_extension(ext)
                    print(f"Loaded extension: {ext}")
                except Exception as e:
                    print(f"Failed to load {ext}: {e}")

            # Sync slash commands
            if GUILD_ID:
                guild = discord.Object(id=GUILD_ID)
                self.tree.copy_global_to(guild=guild)
                await self.tree.sync(guild=guild)
                print(f"Synced commands to guild {GUILD_ID}")
            else:
                await self.tree.sync()
                print("Synced global commands")


bot = MyBot()


@bot.event
async def on_ready0():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("Bot is ready!")

bot.run(BOT_TOKEN)
