import discord
from discord.ext import commands
import Paginator

@commands.command()
async def faca(ctx):

    Embed1 = discord.Embed(title="Faca Tática", description="Grátis — Corpo a Corpo", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/d/d8/TacticalKnife.png/revision/latest?cb=20220306002426")

    embeds = [Embed1]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(faca)