import discord
from discord.ext import commands
import Paginator

@commands.command()
async def riflesdeatirador(ctx):

    Embed1 = discord.Embed(title="Marshal", description="950 — Penetração Média", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/b/b9/Marshal.png/revision/latest?cb=20220306002237")

    Embed2 = discord.Embed(title="Operator", description="4,700 — Penetração Alta", colour = discord.Colour.brand_red())
    Embed2.set_image(url="https://static.wikia.nocookie.net/valorant/images/1/17/Operator.png/revision/latest?cb=20220306002302")

    embeds = [Embed1, Embed2]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(riflesdeatirador)