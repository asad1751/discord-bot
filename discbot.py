import discord
import random
from discord.ext import commands

token = " "

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")
