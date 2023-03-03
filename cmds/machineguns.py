import discord
from discord.ext import commands
import Paginator

@commands.command()
async def metralhadoras(ctx):

    Embed1 = discord.Embed(title="Ares", description="1,600 — Penetração Alta", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/0/05/Ares.png/revision/latest?cb=20220306002039")

    Embed2 = discord.Embed(title="Odin", description="3,200 — Penetração Alta", colour = discord.Colour.brand_red())
    Embed2.set_image(url="https://static.wikia.nocookie.net/valorant/images/5/58/Odin.png/revision/latest?cb=20220306002249")

    embeds = [Embed1, Embed2]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(metralhadoras)