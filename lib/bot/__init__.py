import discord
from discord.ext.commands import bot
from discord import Intents
from discord.ext.commands import Bot as BotBase
from discord.ext.commands.core import has_permissions, has_role
from discord import message
from discord.ext import commands
from discord.utils import get
from discord import Embed
from discord.ext.commands import CommandNotFound
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from lib.db import db
from asyncio import sleep
from datetime import datetime
from glob import glob
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from discord import Embed, File, DMChannel
from discord.errors import HTTPException, Forbidden
from discord.ext.commands import Bot as BotBase
from discord.ext.commands import Context
from discord.ext.commands import (CommandNotFound, BadArgument, MissingRequiredArgument, CommandOnCooldown)
from discord.ext.commands import when_mentioned_or, command, has_permissions
from ..db import db


PREFIX = "[]"
OWNER_IDS = [446544356829036544]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)
        super().__init__(
            command_prefix=PREFIX,
             owner_ids=OWNER_IDS,
             intents=Intents.all(),
             )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("mogu mogu")

    async def on_disconnect(self):
        print("OKAYUUU")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong.")
        
        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exfc

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.scheduler.start()
            print("bot ready")
            # for guild in bot.guilds:
            #     await guild.system_channel.send("mogu mogu~")
            

        else:
            print("bot reconnected")

    async def on_message(self, message):
        pass

bot = Bot()
        