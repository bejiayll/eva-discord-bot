import discord as ds
import os
import asyncio
import time as tm
import random

from dotenv import load_dotenv

load_dotenv()

admin_user = int(os.getenv("ADMIN-USER"))
debug_guildes = [int(os.getenv("DEBUG-GUILD"))]

bot = ds.Bot()

c_debug = bot.create_group("debug", "debug commands", guild_ids=[debug_guildes])
c_fun = bot.create_group("fun", "Just for fun")
c_utils = bot.create_group("utils", "Useless commands")


@bot.event
async def on_ready():
    print(f"{bot.user} is ready")


