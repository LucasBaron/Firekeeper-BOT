import discord
import os
import requests
from decouple import config
from discord.ext import commands
bot = commands.Bot("f!")


def load_cogs(bot):
 for file in os.listdir("commands"):
      if file.endswith(".py"):
       cog = file[:-3]
       bot.load_extension(f"commands.{cog}")


load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN)
#    await message.add_reaction("◀️")
#    await message.add_reaction("▶️") 