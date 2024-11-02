import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

botprueba=commands.Bot(command_prefix="/",intents=intents)
@botprueba.event
async def on_ready():
    print("se inicio el bot")

@botprueba.command()
async def hola(ctx):
    await ctx.send("Hola como estas")

@botprueba.command()
async def suma(ctx,num2:int,num3:int):
    suma=num2+num3
    await ctx.send(f"La suma de {num2} + {num3} = {suma}")


@botprueba.command()
async def division(ctx,num2:int,num3:int):
    division=num2/num3
    await ctx.send(f"La division de {num2} / {num3} = {division}")



botprueba.run("MTI5Njk2ODM1NTM5OTM0MDEzMw.GwKHSx.DgYwHkOFQY2cVBHVr51F-zgDN9ana2h1UoBrpY")
