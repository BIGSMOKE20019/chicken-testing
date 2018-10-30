import discord
import asyncio
import youtube_dl
import os
from discord.ext import commands
from discord.ext.commands import Bot


bot=commands.Bot(command_prefix='!')

from discord import opus
OPUS_LIBS = ['libopus-0.x86.dll', 'libopus-0.x64.dll',
             'libopus-0.dll', 'libopus.so.0', 'libopus.0.dylib']


def load_opus_lib(opus_libs=OPUS_LIBS):
    if opus.is_loaded():
        return True

    for opus_lib in opus_libs:
            try:
                opus.load_opus(opus_lib)
                return
            except OSError:
                pass

    raise RuntimeError('Could not load an opus lib. Tried %s' %
                       (', '.join(opus_libs)))
load_opus_lib()



@bot.event
async def on_ready():
    print("hi")
opts = {
            'default_search': 'auto',
            'quiet': True,
        }    
    
@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(channel)



players={}


@bot.command(pass_context=True)
async def reset(ctx):
    await bot.say("Hi @everyone ,")
    await bot.say("I am official helper of **Chicken server**")
    await bot.say("What you need help with?")
    await bot.say("Write **!helper** and I will help you")
    
@bot.command(pass_context=True)
async def helper(ctx):
  await bot.say("**Commands:**")
  await bot.say("**         !server-info** = info about Chicken server")
  await bot.say("**         !user-info** = info about user")
  await bot.say("**         !games** = list of all supported games for updates ")
  await bot.say("** **")
  await bot.say("If you need help with something else, write **!call** to call moderators or helpers")

@bot.command(pass_context=True)
async def test(ctx):
  await bot.say("testing")

@bot.command(pass_context=True)
async def call(ctx):
  await bot.say("**Moderators** and **Helpers** was called")
  


bot.run(os.environ['BOT_TOKEN'])
