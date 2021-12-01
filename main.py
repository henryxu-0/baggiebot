import discord
from discord.ext import commands
import music

cogs = [music]

client = commands.Bot(command_prefix='?', intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)
  
client.run("OTE1Njg4MTE3MzAwNzgxMDY2.YafPAw._h0e_Nxr4UVfMdHYkN1MYoOyME4")