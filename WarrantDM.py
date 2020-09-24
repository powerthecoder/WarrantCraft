import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
import asyncio
import json
import os
import sys


prefix_list = [
    "=",
    "!"
]
client = commands.Bot(command_prefix=prefix_list)
client.remove_command("help")

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


# When Error Occurs #
@client.event
async def on_command_error(ctx, error):
	print(f"[Error] {error}")

@client.command(pass_context=True)
async def help(ctx):
    embed=discord.Embed(title="Help Menu", description="Prefix `!` or `=`")
    embed.add_field(name="!about", value="About the developer and bot", inline=False)
    embed.add_field(name="!dm @user <message>", value="Send a DM to a User", inline=False)
    embed.add_field(name="!adm @user <message>", value="Send a Anonymous DM to a User", inline=False)
    embed.add_field(name="!help", value="Get Help Menu", inline=False)
    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def about(ctx):
    embed=discord.Embed(title="About", description="**Developer:** <@255876083918831616> (Leo Power) \n**Website:** https://powerthecoder.xyz \n**Bot Owner:** <@564190903028416556>")
    await ctx.send(embed=embed)

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def dm(ctx, user_name:discord.Member, *,args):
    print(f"{ctx.message.author} sent {user_name} a DM {args}")
    try:
        embed_dm=discord.Embed(title="WarrantCraft Direct Message", description=f"**Sent From:** <@{ctx.message.author.id}> \n**Sent To:** <@{user_name.id}> \n**Message:**\n{args}", color=0xff7700)
        await user_name.send(embed=embed_dm)
        embed=discord.Embed(title="DM Sent", description=f"**Sent From:** <@{ctx.message.author.id}> \n**Sent To:** <@{user_name.id}> \n**Message:**\n{args}", color=0xff7700)
        msg1 = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        await ctx.message.delete()
        await asyncio.sleep(59)
        await msg1.delete()
    except Exception as e:
        embed=discord.Embed(title="DM Failed", description=f"**Error:** {e}")
        await ctx.send(embed=embed)

@client.command(pass_context=True)
@has_permissions(administrator=True)
async def adm(ctx, user_name:discord.Member, *,args):
    print(f"{ctx.message.author} sent {user_name} a Anonymous DM {args}")
    try:
        embed_dm=discord.Embed(title="WarrantCraft Direct Message", description=f"{args}", color=0xff7700)
        await user_name.send(embed=embed_dm)
        embed=discord.Embed(title="DM Sent", description=f"**Sent To:** <@{user_name.id}> \n**Message:**\n{args}", color=0xff7700)
        msg1 = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        await ctx.message.delete()
        await asyncio.sleep(59)
        await msg1.delete()
    except Exception as e:
        embed=discord.Embed(title="DM Failed", description=f"**Error:** {e}")
        await ctx.send(embed=embed)

with open(os.path.join(sys.path[0], "config.json"), "r") as f:
    data = json.load(f)
Token = data['Token']
client.run(Token)
