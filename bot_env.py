import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='<', intents=intents)

@bot.event
async def on_ready():
    print(f'Подключен {bot.user}')

@bot.command()
async def hel(ctx):
    await ctx.send('paper - что делать с бумагой, can - с банками от напитков, plastic с пластиком')

@bot.command()
async def paper(ctx):
    await ctx.send('использованная бумага - макулатура')

@bot.command()
async def plastic(ctx):
    await ctx.send('пластик - поделки, кормушки...Используй фантазию!')

@bot.command()
async def can(ctx):
    advices = ['Сделать банки для хранения', 'Кормушка для птиц', 'Усилители для сигнала роутера']
    can_adv = random.choice(advices)
    await ctx.send(can_adv)

bot.run('token')
