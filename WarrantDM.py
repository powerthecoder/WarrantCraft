import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import json
import os
import sys


prefix_list = [
    "=",
    "!"
]
client = commands.Bot(command_prefix=prefix_list)

print("""
Developer: Leo Power
GitHub: https://github.com/powerthecoder/
Website: https://powerthecoder.xyz/

""")

@client.event
async def on_ready():
    print("-"*30)
    print("Bot Started")
    print("-"*30)

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def dm(ctx, user_name:discord.Member, *,args):
    print(f"{ctx.message.author} sent {user_name} a DM {args}")
    try:
        await user_name.send(args)
        embed=discord.Embed(title="DM Sent", description=f"**Sent From:** {ctx.message.author} \n**Sent To:** {user_name} \n**Message:**\n{args}")
        await ctx.send(embed=embed)
    except Exception as e:
        embed=discord.Embed(title="DM Failed", description=f"**Error:** {e}")
        await ctx.send(embed=embed)

with open(os.path.join(sys.path[0], "config.json"), "r") as f:
    data = json.load(f)
Token = data['Token']
client.run(Token)