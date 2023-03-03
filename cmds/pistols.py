import discord
from discord.ext import commands
import Paginator

@commands.command()
async def pistolas(ctx):

    Embed1 = discord.Embed(title="Classic", description="Grátis — Penetração Baixa", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/57/Classic.png/revision/latest?cb=20220306002125")

    Embed2 = discord.Embed(title="Shorty", description="150 — Penetração Baixa", colour = discord.Colour.brand_red())
    Embed2.set_image(url="https://static.wikia.nocookie.net/valorant/images/7/77/Shorty.png/revision/latest?cb=20220306002343")

    Embed3 = discord.Embed(title="Frenzy", description="450 — Penetração Baixa", colour = discord.Colour.brand_red())
    Embed3.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/f1/Frenzy.png/revision/latest?cb=20220306002141")

    Embed4 = discord.Embed(title="Ghost", description="500 — Penetração Média", colour = discord.Colour.brand_red())
    Embed4.set_image(url="https://static.wikia.nocookie.net/valorant/images/a/ab/Ghost.png/revision/latest?cb=20220306002156")

    Embed5 = discord.Embed(title="Sheriff", description="800 — Penetração Alta", colour = discord.Colour.brand_red())
    Embed5.set_image(url="https://static.wikia.nocookie.net/valorant/images/3/3e/Sheriff.png/revision/latest?cb=20220306002329")

    embeds = [Embed1, Embed2, Embed3, Embed4, Embed5]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(pistolas)