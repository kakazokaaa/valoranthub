import discord
from discord.ext import commands

@commands.command()
async def lore(ctx):
        embed = discord.Embed(
            colour = discord.Colour.brand_red(),
            title = "História do Jogo",
            description = """Valorant se passa em uma versão da Terra em um futuro próximo seguinte de um evento chamado de First Light.
            
            Esse evento abrange todo o globo, transformando a vida, a tecnologia e a forma como os governos operam.
            
            Entretando, algumas pessoas ao redor do mundo começaram a ganhar habilidades por conta desse evento. Esses seres são chamados de Radiantes.
            
            Como resposta ao First Light, uma organização secreta fundou o Protocolo Valorant, que agrupa todos os agentes ao redor do mundo.
            
            Esses agentes consistem em Radiantes e outros indivíduos equipados com tecnologia Radiante."""
        )

        embed.set_image(url="https://i.ibb.co/W09rTPt/lore.png")
        
        await ctx.send(embed = embed)

async def setup(bot):
        bot.add_command(lore)