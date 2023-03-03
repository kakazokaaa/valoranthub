import discord
from discord.ext import commands
import Paginator

@commands.command()
async def espingardas(ctx):

    Embed1 = discord.Embed(title="Bucky", description="850 — Penetração Baixa", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/e/eb/Bucky.png/revision/latest?cb=20220306002057")

    Embed2 = discord.Embed(title="Judge", description="1,850 — Penetração Baixa", colour = discord.Colour.brand_red())
    Embed2.set_image(url="https://static.wikia.nocookie.net/valorant/images/8/8a/Judge.png/revision/latest?cb=20220306002225")

    embeds = [Embed1, Embed2]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(espingardas)