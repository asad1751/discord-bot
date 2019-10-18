import discord
import random
from discord.ext import commands

token = " "

client= commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency*1000)}ms')

@client.command()
async def complete(ctx,process):
    await ctx.send(f'{process} is random.randint(0,100)% complete')
