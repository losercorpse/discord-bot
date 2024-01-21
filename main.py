import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()


# Define your intents
intents = discord.Intents.default()
intents.message_content = True #v2
client = commands.Bot(command_prefix = '!' , intents=intents)

# Access the bot token from the environment variables
bot_token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print("The bot is ready for use")
    print("-------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the anime bot")
    
client.run(bot_token)