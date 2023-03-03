import discord
from discord.ext import commands

@commands.command()
async def valorant(ctx):
        embed = discord.Embed(
            colour = discord.Colour.brand_red(),
            title = "Sobre o Jogo",
            description = """Valorant é um jogo multijogador de tiro tático em primeira pessoa gratuito para jogar, desenvolvido e publicado pela Riot Games.
            
            Duas equipes de cinco jogam uma contra a outra, e os jogadores assumem o papel de agentes com habilidades únicas.
            
            No modo de jogo principal, a equipe atacante tem uma bomba, chamada spike, que eles precisam plantar em um local, chamado bombsite.
            
            Se a equipe atacante proteger com sucesso a bomba e ela detonar, eles ganharão um ponto.
            
            Se a equipe defensora desarmar com sucesso a bomba ou o crônometro de 100 segundos da rodada expirar, a equipe defensorá receberá um ponto.
            
            Eliminar todos os membros da equipe adversária também ganha uma rodada.
            
            A primeira equipe a vencer o melhor de 24 rodadas vence a partida."""
        )

        embed.set_image(url="https://www.imagemhost.com.br/images/2023/03/03/valorant.png")
        
        await ctx.send(embed = embed)

async def setup(bot):
        bot.add_command(valorant)