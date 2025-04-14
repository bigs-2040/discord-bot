
import discord
from discord.ext import commands
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
THREAD_ID = 1346852170288595084  # ID du thread "Audience Initiale"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} est prêt et connecté.")

@bot.command()
async def envoyer(ctx):
    try:
        thread = await bot.fetch_channel(THREAD_ID)
        if isinstance(thread, discord.Thread):
            await thread.send(
                username="Yet Another M* Project",
                avatar_url="https://cdn.discordapp.com/avatars/1359539483401261167/b026d51b6d411baa8b1a37a73a812940.png",
                embeds=[
                    discord.Embed(
                        title="WELCOME TO THE NEW MODERATORS",
                        description="Congratulations on being selected to join the moderation team, and thank you for the special interest you have in this project.\n\nYou currently have standard moderation permissions. As explained in your tickets, you are all in a one-month probation period, during which you will be evaluated to determine whether you are a good fit for the role and can be trusted. At the end of this period, if the evaluation is positive, you will become a confirmed moderator, which will allow you to take on a wider range of responsibilities.\n\n**Your current permissions**\n- delete messages\n- manage nicknames\n- temporarily timeout a member\n- mute in voice channels\n- kick from a voice channel\n- move users between voice channels",
                        color=9201795,
                        thumbnail={"url": "https://media.discordapp.net/attachments/1357702436554277025/1357704982358397041/Logo.png?ex=67fdb30c&is=67fc618c&hm=d1c531b0f6643a2bed985b57ca9c5291544d15063ae85f7e12ed2c87debd065e&format=webp&quality=lossless&"}
                    ),
                    discord.Embed(
                        title="What's next ?",
                        description="You can already begin fulfilling your role as a moderator using the permissions available to you. **A meeting will be organized soon** to clearly explain what we expect from you. Until then, don’t forget to carefully read the moderator guidelines available in the https://discord.com/channels/1214142985952960522/1358238270571675732 channel.",
                        color=9201795
                    ),
                    discord.Embed(
                        title="About the language channels",
                        description="These recruitments will allow us to open several additional language-specific channels. The moderators assigned to these channels must not neglect moderation within them. Unlike moderators who speak only English, you have an extra and above all essential responsibility, and we’re placing our trust in you.\n\n**Language channels coming soon**\n- Dutch\n- Russian\n- Spanish\n\nUnfortunately, for the other languages, we haven’t gathered enough moderators yet, or there aren’t enough members to justify opening those language-specific channels.",
                        color=9201795
                    ),
                    discord.Embed(
                        description="Lastly, even though YAMP doesn’t yet have its own specific rules, the Discord Community Guidelines still apply, and we’re counting on you to enforce them.\n\nSee you soon team !",
                        color=9201795
                    ).set_footer(text="YAMP Community Moderation Team", icon_url="https://media.discordapp.net/attachments/1240678603386257510/1360994332773187645/otoofkf.png?ex=67fdccfe&is=67fc7b7e&hm=5fa5f3555cd498bff20e97137e10a6f42a284817485af765445eaafc4c339486&format=webp&quality=lossless&")
                ]
            )
            await ctx.send("Embed envoyé dans le thread !")
        else:
            await ctx.send("Le thread spécifié est introuvable ou n'est pas valide.")
    except Exception as e:
        await ctx.send(f"Erreur lors de l'envoi : {e}")

bot.run(TOKEN)
