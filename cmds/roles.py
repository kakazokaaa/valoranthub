import discord
from discord.ext import commands
import Paginator

@commands.command()
async def roles(ctx):

    Embed1 = discord.Embed(title="Iniciador", description="Desafia ângulos, preparando sua equipe para contestar território e afastar os inimigos.", colour = discord.Colour.brand_red())
    Embed1.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/7/77/InitiatorClassSymbol.png/revision/latest?cb=20200408043926")

    Embed2 = discord.Embed(title="Controlador", description="Especialista em dividir o território inimigo e preparar sua equipe para o sucesso.", colour = discord.Colour.brand_red())
    Embed2.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/0/04/ControllerClassSymbol.png/revision/latest?cb=20200408043911")

    Embed3 = discord.Embed(title="Duelista", description="Fragger que busca o primeiro contato por meio das habilidades.", colour = discord.Colour.brand_red())
    Embed3.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/f/fd/DuelistClassSymbol.png/revision/latest?cb=20200408043920")

    Embed4 = discord.Embed(title="Sentinela", description="Especialista defensivo que bloqueia áreas e observa os flancos.", colour = discord.Colour.brand_red())
    Embed4.set_thumbnail(url="https://static.wikia.nocookie.net/valorant/images/4/43/SentinelClassSymbol.png/revision/latest?cb=20200408043934")

    embeds = [Embed1, Embed2, Embed3, Embed4]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(roles)