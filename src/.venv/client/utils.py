import discord as ds
import asyncio

from .bot import bot, c_utils

time_mult = {
    'Years' : 3600 * 24 * 356,
    'Mouths': 3600 * 24 * 30,
    'Weeks' : 3600 * 24 * 7,
    'Days'  : 3600 * 24,
    'Hours' : 3600,
    'Minutes': 60,
    'Seconds': 1 
}

@c_utils.command(name="timer", description="It's just timer man")
async def timer(ctx: ds.ApplicationContext, time: int, unit: ds.Option(str, choices=['Hours', 'Minutes', 'Seconds'])='Seconds'):
    await ctx.respond(f"Установлен таймер на `{time} {unit}`")
    await asyncio.sleep(time*time_mult[unit])
    await ctx.respond(f"{ctx.author.mention} таймер на `{time} {unit}` сработал")

@c_utils.command(name="clear_crash", description="After chash you can clear all channels")
@ds.default_permissions(administrator=True)
async def clear_crash(ctx: ds.ApplicationContext):
    await ctx.respond("Cleaning channels started")
    guild = ctx.interaction.guild
    channels = [channel for channel in guild.channels if isinstance(channel, ds.TextChannel)]
    for channel in channels:
        if str(channel.name).startswith('crashed'):
            await channel.delete()
    await ctx.respond("Cleaning chats finished ")