# Don't Remove Credit @Spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @Spideyofficial_777
# Ask Doubt on telegram @hacker_x_official_777

# Clone Code Credit : YT - @Spidey_official_777 / TG - @hacker_x_official_777/ GitHub - @Spideyofficial777


import os
from pyrogram import Client, filters
from urllib.parse import quote
from info import CHNL_LNK
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["share_text", "share", "sharetext"]))
async def share_text(client, message):
    Spidey = await client.ask(chat_id = message.from_user.id, text = "Now Send me your text.")
    if Spidey and (Spidey.text or Spidey.caption):
        input_text = Spidey.text or Spidey.caption
    else:
        await Spidey.reply_text(
            text=f"**Notice:**\n\n1. Send Any Text Messages.\n2. No Media Support\n\n**Join Update Channel**",               
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel", url=CHNL_LNK)]])
            )                                                   
        return
    await Spidey.reply_text(
        text=f"**Here is Your Sharing Text 👇**\n\nhttps://t.me/share/url?url=" + quote(input_text),
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("♂️ Share", url=f"https://t.me/share/url?url={quote(input_text)}")]])       
    )
