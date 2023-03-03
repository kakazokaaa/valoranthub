import discord
from discord.ext import commands
import Paginator

@commands.command()
async def submetralhadoras(ctx):

    Embed1 = discord.Embed(title="Stinger", description="1,100 — Penetração Baixa", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/b/b6/Stinger.png/revision/latest?cb=20220306002413")

    Embed2 = discord.Embed(title="Spectre", description="1,600 — Penetração Média", colour = discord.Colour.brand_red())
    Embed2.set_image(url="https://static.wikia.nocookie.net/valorant/images/9/90/Spectre.png/revision/latest?cb=20220306002356")

    embeds = [Embed1, Embed2]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(submetralhadoras)