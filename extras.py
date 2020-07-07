import discord

async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		await i.save(fp="./tempfile.png")
		filelist.insert(len(filelist),discord.File(fp="./tempfile.png",spoiler=spoiler))
	return filelist