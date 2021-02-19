#!/usr/bin/env python3

import discord
from discord.ext import commands
from extras import *

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

prefix = 's?'

client = commands.Bot(command_prefix=prefix)
client.remove_command("help")

helpmessage = discord.Embed(title="Commands", colour=discord.Colour(0xd084), description=f"**spoiler** - makes a message spoilered, can do images too. use: ```{prefix}[spoiler|sp] [text]```\n\n**help** - help message. use: ```{prefix}[help|h]```")
helpmessage.set_author(name="Help")

@client.event
async def on_ready():
	await client.change_presence(activity=discord.Game(name="s?help"))
	print("hello world")
	

@client.command(aliases=["sp"])
async def spoiler(ctx,*text):
	use_prev_msg = True if text == () and len(ctx.message.attachments) == 0 else False
	if use_prev_msg:
		async for message in ctx.channel.history(limit=10):
			if message.author != ctx.author:
				continue
			if message == ctx.message:
				continue
			msg = message
			break
	else:
		msg = ctx.message
	txt = msg.content if msg != ctx.message else " ".join(text)
	images = await attachments_to_files(msg.attachments,True)
	await msg.delete()
	if use_prev_msg:
		await ctx.message.delete()
	if len(images) == 0:
		txt = f"|| {txt} ||"
	imitated = ctx.author
	avatar = await imitated.avatar_url_as(format="png").read()
	hook = await ctx.channel.create_webhook(name=imitated.display_name,avatar=avatar)
	await hook.send(content=txt,files=images)
	await hook.delete()

@client.command(aliases=["h"])
async def help(ctx,*text):
	
	helpmessage.set_footer(text=f"{ctx.author.name}", icon_url=f"https://cdn.discordapp.com/avatars/{ctx.author.id}/{ctx.author.avatar}.png")

	await ctx.send(embed=helpmessage)

@client.command(aliases=["p"])
async def ping(ctx,*text):
	ping = client.latency * 1000
	ping = str(ping).split(".")
	await ctx.send(ping[0])

@client.command(aliases=["github","git","r"])
async def repo(ctx,*text):
	await ctx.send("this spoiler bot: http://github.com/gamererr/spoiler-bot\nthe old one: http://github.com/vresod/spoiler-bot")

client.run(token)