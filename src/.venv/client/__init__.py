from dotenv import load_dotenv
import os

from client.bot import bot
import client.fun
import client.utils
import client.auto_create_voice_channel

load_dotenv()

token = str(os.getenv("TOKEN"))

bot.run(token)