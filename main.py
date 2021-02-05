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
	images = await attachments_to_files(ctx.message.attachments,True)
	txt = " ".join(text)
	await ctx.message.delete()
	imitated = ctx.author
	avatar = await imitated.avatar_url_as(format="png").read()
	hook = await ctx.channel.create_webhook(name=imitated.display_name,avatar=avatar)
	await hook.send(content=txt,files=images)

client.run(token)