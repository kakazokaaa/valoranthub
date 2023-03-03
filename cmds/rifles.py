import discord
from discord.ext import commands
import Paginator

@commands.command()
async def rifles(ctx):

    Embed1 = discord.Embed(title="Bulldog", description="2,050 — Penetração Média", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/0/07/Bulldog.png/revision/latest?cb=20220306002110")

    Embed2 = discord.Embed(title="Guardian", description="2,250 — Penetração Alta", colour = discord.Colour.brand_red())
    Embed2.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/fd/Guardian.png/revision/latest?cb=20220306002211")

    Embed3 = discord.Embed(title="Phantom", description="2,900 — Penetração Média", colour = discord.Colour.brand_red())
    Embed3.set_image(url="https://static.wikia.nocookie.net/valorant/images/e/ec/Phantom.png/revision/latest?cb=20220306002314")

    Embed4 = discord.Embed(title="Vandal", description="2,900 — Penetração Média", colour = discord.Colour.brand_red())
    Embed4.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/56/Vandal.png/revision/latest?cb=20220306002438")

    embeds = [Embed1, Embed2, Embed3, Embed4]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(rifles)