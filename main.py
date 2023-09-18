import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix="/",
intents=disnake.Intents.all() )

@bot.slash_command()
async def devbadge(interaction: disnake.AppCmdInter):
    await interaction.send("Заходи к нам на https://discord.gg/lothree")

bot.run("YOUR_TOKEN_BOT")