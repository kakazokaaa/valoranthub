import discord
from discord.ext import commands
import Paginator

@commands.command()
async def mapas(ctx):

    Embed1 = discord.Embed(title="The Range", description="Veneza, Itália — Terra Alfa", colour = discord.Colour.brand_red())
    Embed1.set_image(url="https://static.wikia.nocookie.net/valorant/images/3/37/Loading_Screen_Range.png/revision/latest?cb=20200607180003")

    Embed2 = discord.Embed(title="Ascent", description="Veneza, Itália — Terra Alfa", colour = discord.Colour.brand_red())
    Embed2.set_image(url="https://static.wikia.nocookie.net/valorant/images/e/e7/Loading_Screen_Ascent.png/revision/latest?cb=20200607180020")

    Embed3 = discord.Embed(title="Bind", description="Rabat, Marrocos — Terra Alfa", colour = discord.Colour.brand_red())
    Embed3.set_image(url="https://static.wikia.nocookie.net/valorant/images/2/23/Loading_Screen_Bind.png/revision/latest/scale-to-width-down/1000?cb=20200620202316")

    Embed4 = discord.Embed(title="Breeze", description="Triângulo das Bermudas, Oceano Atlântico — Terra Alfa", colour = discord.Colour.brand_red())
    Embed4.set_image(url="https://static.wikia.nocookie.net/valorant/images/1/10/Loading_Screen_Breeze.png/revision/latest?cb=20210427160616")

    Embed5 = discord.Embed(title="Fracture", description="Santa Fé, Novo México — Terra Alfa", colour = discord.Colour.brand_red())
    Embed5.set_image(url="https://static.wikia.nocookie.net/valorant/images/f/fc/Loading_Screen_Fracture.png/revision/latest?cb=20210908143656")

    Embed6 = discord.Embed(title="Haven", description="Timbu, Butão — Terra Alfa", colour = discord.Colour.brand_red())
    Embed6.set_image(url="https://static.wikia.nocookie.net/valorant/images/7/70/Loading_Screen_Haven.png/revision/latest?cb=20200620202335")

    Embed7 = discord.Embed(title="Icebox", description="Ilha Bennet, Rússia — Terra Alfa", colour = discord.Colour.brand_red())
    Embed7.set_image(url="https://static.wikia.nocookie.net/valorant/images/1/13/Loading_Screen_Icebox.png/revision/latest?cb=20201015084446")

    Embed8 = discord.Embed(title="Lotus", description="Gates Ocidentais, Índia — Terra Ômega", colour = discord.Colour.brand_red())
    Embed8.set_image(url="https://static.wikia.nocookie.net/valorant/images/d/d0/Loading_Screen_Lotus.png/revision/latest/scale-to-width-down/1000?cb=20230106163526")

    Embed9 = discord.Embed(title="Pearl", description="Lisboa, Portugal — Terra Ômega", colour = discord.Colour.brand_red())
    Embed9.set_image(url="https://static.wikia.nocookie.net/valorant/images/a/af/Loading_Screen_Pearl.png/revision/latest?cb=20220622132842")

    Embed10 = discord.Embed(title="Split", description="Tóquio, Japão — Terra Alfa", colour = discord.Colour.brand_red())
    Embed10.set_image(url="https://static.wikia.nocookie.net/valorant/images/d/d6/Loading_Screen_Split.png/revision/latest/scale-to-width-down/1000?cb=20200620202349")

    embeds = [Embed1, Embed2, Embed3, Embed4, Embed5, Embed6, Embed7, Embed8, Embed9, Embed10]

    await Paginator.Simple().start(ctx, pages=embeds)

async def setup(bot):
        bot.add_command(mapas)