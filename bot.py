import discord 
from discord.ext import commands

import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
    channel = bot.get_channel(722095922015895562) 
    await channel.send("我來了!")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(722031237174263848) 
    print(f"{member} join!")
    await channel.send(f"{member} 歡迎來到實力至上主義的教室:kissing_closed_eyes:!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(722031237174263848)
    print(f"{member} leave!")
    await channel.send(f"{member} 離開了實力至上主義的教室.....:tired_face:")

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.command()
async def 堀北鈴音1(ctx): 
    pic= discord.File(jdata['pic1'])
    await ctx.send(file=pic)

@bot.command()
async def 堀北鈴音2(ctx): 
    pic= discord.File(jdata['pic2'])
    await ctx.send(file=pic)

@bot.command()
async def 堀北鈴音3(ctx): 
    pic= discord.File(jdata['pic3'])
    await ctx.send(file=pic)

@bot.command()
async def 堀北鈴音4(ctx): 
    pic= discord.File(jdata['pic4'])
    await ctx.send(file=pic)


bot.run(jdata['TOKEN'])