
# Spoiler Bot
The only discord bot made because the bot's author's friend complained about jojo spoilers.

## Why?
Discord mobile doesn't have an (easy) way to mark images as spoilers. This is the solution.

## How do I use it?
Make sure the bot is on your server. If it isn't, use the [this link](https://discord.com/api/oauth2/authorize?client_id=730114126508195901&permissions=8192&scope=bot) to get it on there. Keep in mind that this bot requires the "Manage Messages" permission.

Once the bot is on the server, use the "command" `?spoiler (text)` and then attach an image. When you send this message, it will be nearly immediately deleted and replaced with a message by the bot which is exactly the same except has the image marked as a spoiler.

## How do I host it?

### For versions prior to 1217d75
Running this project requires Python 3.4+ and pip.

This bot requires the files `main.py` and `extras.py`. If you don't want to download `extras.py` you can also copy the function from it into the main file. Please note that if you do this, do not copy `import discord` from the top.

After you have the files, run `pip install -r requirements.txt`. This will download all of the requirements for the project. Finally, run `python3 main.py`.

### For versions including and after 1217d75
Read above section, except instead of doing `pip install -r requirements.txt`, you have to manually install the development version of `discord.py`. This can be installed from [Rapptz/discord.py](https://github.com/Rapptz/discord.py#installing). Alternatively, reverse this commit and just use the above section's instructions.