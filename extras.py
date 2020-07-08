import discord

async def attachments_to_files(attached,spoiler=False):
	filelist = []
	for i in attached:
		file = await i.to_file(spoiler=spoiler)
		filelist.insert(len(filelist),file)
	return filelist