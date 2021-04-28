# import discord
# from . import db
# from discord.ext import commands
# from discord.utils import get
# from discord import message
# from discord.ext.commands import bot
# from discord.ext.commands.core import has_permissions, has_role
# db.build()
# #sheesh peko

# import os

# import json

# with open("token.json", "r") as f:
#     my_dict = json.load(f)


# client = discord.Client()

# intents = discord.Intents.default()
# intents.members = True

# client = commands.Bot(command_prefix='mogu mogu ', intents=intents)


# @client.event
# async def on_ready():
#     print('Mogu Mogu')

# @client.event
# async def on_member_join(member):
#     print(f"{member} has joined")
#     guild = member.guild
#     if guild.system_channel is not None:
#         embed=discord.Embed(
#     title="Welcome to Kone Squad!",
#     url="https://kone.club",
#     description=f"mogu mogu... Okayu!! Welcome {member.mention}. Please make sure to enjoy your stay",
#     color=0x964B00,)
#     embed.set_image(url="https://i.amankins.com/2021/04/eUCCstW.jpg")
#     embed.set_footer(text="mogu mogu")
#     #Eventually make configurable
#     await guild.system_channel.send(embed=embed)

# client.run(my_dict["token"])

