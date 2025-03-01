# Don't Remove Credit @Spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @Spideyofficial_777
# Ask Doubt on telegram @hacker_x_official_777

# Clone Code Credit : YT - @Spidey_official_777 / TG - @hacker_x_official_777/ GitHub - @Spideyofficial777

from pyrogram import Client, filters
from plugins.Extra.engine import ask_ai


@Client.on_message(filters.command('openai'))
async def openai_ask(client, message):
    if len(message.command) == 1:
       return await message.reply_text("Give an input!")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)
