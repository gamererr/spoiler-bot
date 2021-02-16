#!/usr/bin/env python3

import discord
from discord.ext import commands
from extras import *

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

client = commands.Bot(command_prefix="s?")

@client.event
async def on_ready():
	print("logged in as {0.user}".format(client))
	

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

@client.command(aliases=["sw"])
async def swear(ctx,*text):
	pass


client.run(token)