import discord 
from discord.ext import commands

import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")


@bot.command()
async def c1(ctx): 
    pic= discord.File(jdata['pic1'])
    await ctx.send(file=pic)

@bot.command()
async def c2(ctx): 
    pic= discord.File(jdata['pic2'])
    await ctx.send(file=pic)

@bot.command()
async def c3(ctx): 
    pic= discord.File(jdata['pic3'])
    await ctx.send(file=pic)

@bot.command()
async def c4(ctx): 
    pic= discord.File(jdata['pic4'])
    await ctx.send(file=pic)


bot.run(jdata['TOKEN'])