import discord as ds 

from .bot import bot

temp_channels = []

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        await handle_voice_join(member, after.channel)
    elif before.channel is not None and after.channel is None:
        await handle_voice_leave(member, before.channel)

async def handle_voice_join(member: ds.Member, channel: ds.VoiceChannel):
    global temp_channels
    guild = channel.guild
    if channel.id == 1453442969641418871:
        new_voice = await guild.create_voice_channel(name=member.name, category=guild.get_channel(1453442969641418869))  
        temp_channels.append(new_voice.id)

    await member.move_to(new_voice)

async def handle_voice_leave(member: ds.Member, channel: ds.VoiceChannel):
    global temp_channels
    if channel.id in temp_channels:
        if len(channel.members) < 1:
            await channel.delete()