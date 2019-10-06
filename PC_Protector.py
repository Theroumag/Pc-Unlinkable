import discord, re, time
from discord.ext import commands
from discord.utils import get

linkRegrex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")

client = commands.Bot(command_prefix = "?")
with open("token.txt", "r") as f: token = f.read()[:-1]

@client.event
async def on_ready():
    print("uLink Origin Online")
    await client.change_presence(activity=discord.Activity(name="Protecting the campus enviorment"))
    client.help_command = commands.DefaultHelpCommand(no_category='Commands')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    link = linkRegrex.search(message.content)
    if link is not None:
        if message.guild.get_role(627889209302319114) not in message.author.roles:
            await message.channel.send(f"Brooo... {message.author.mention} that link looks hella susPISious brooo {message.author.mention}")
            channel = client.get_channel(628290881270579210)
            await channel.send(f"{message.author.mention} posted {link.group()} in {message.channel}")

    await client.process_commands(message)

@client.command()
async def catcall(ctx, user: discord.Member):
    while True:
        await ctx.send(f"{user.mention} Hey babe :kissing_heart:")
        time.sleep(1)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong bro! My latency is {round(client.latency *100)}ms bro!")

@client.command(aliases=["purge", "c", "p"])
async def clear(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
client.run(token)

