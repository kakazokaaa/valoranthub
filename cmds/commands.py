import discord
from discord.ext import commands

@commands.command()
async def comandos(ctx):
        embed = discord.Embed(
            colour = discord.Colour.brand_red(),
            title = "Comandos",
            description = "Lista de comandos disponíveis"
        )

        embed.add_field(name = "Valorant", value = "Sobre o jogo", inline = True)
        embed.add_field(name = "Lore", value = "História do jogo", inline = True)
        embed.add_field(name = "Mapas", value = "Mapas do jogo", inline = True)
        embed.add_field(name = "Roles", value = "Funções do jogo", inline = True)
        embed.add_field(name = "Agentes", value = "Agentes do jogo", inline = True)
        embed.add_field(name = "Armas", value = "Armas do jogo", inline = True)

        embed.set_image(url="https://media.tenor.com/Q0TPlNPEqTkAAAAC/sova-valorant-valorant.gif")
        
        await ctx.send(embed = embed)

async def setup(bot):
        bot.add_command(comandos)