import settings
import discord 
from discord.ext import commands
    
logger = settings.logging.getLogger("bot")
    
def run():
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = commands.Bot(command_prefix="/", intents = intents)
    
    @bot.event 
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")

        for cmd_file in settings.CMDS_DIR.glob("*.py"):
            if cmd_file.name != "__init__.py":
                await bot.load_extension(f"cmds.{cmd_file.name[:-3]}")

    @bot.event
    async def on_guild_join(guild):
       embed = discord.Embed(title = "Olá!", description = "Obrigado por me convidar. Para acessar a lista de comandos, digite /comandos!", colour = discord.Colour.brand_red())

       embed.set_image(url="https://www.imagemhost.com.br/images/2023/03/03/ezgif.com-gif-maker.gif")

       await guild.system_channel.send(embed = embed)

    bot.run(settings.DISCORD_API_SECRET, root_logger = True)

if __name__ == "__main__":
    run()