import discord
from discord.ext import commands

@commands.command()
async def armas(ctx):
        embed = discord.Embed(
            colour = discord.Colour.brand_red(),
            title = "Armas do Jogo",
            description = """Pistolas
            
            Submetralhadoras
            
            Espingardas
            
            Rifles
            
            Rifles de Atirador
            
            Metralhadoras
            
            Faca
            
            Digite / antes da categoria para saber mais!"""
        )
        
        await ctx.send(embed = embed)

async def setup(bot):
        bot.add_command(armas)