#!/usr/bin/env python3

import discord
import extras

with open("tokenfile", "r") as tokenfile:
	token=tokenfile.read()

client = discord.Client()

@client.event
async def on_ready():
	print("logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user or message.author.bot:
		return
	if not message.content.startswith("?spoiler"):
		return
	text = message.content[9:]
	images = await extras.attachments_to_files(message.attachments,True)

	await message.delete()
	await message.channel.send(content="**{0}**\n{1}".format(message.author.name,text),files=images)

client.run(token)