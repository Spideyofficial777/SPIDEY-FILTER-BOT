# Don't Remove Credit @Spideyofficial777
# Subscribe YouTube Channel For Amazing Bot @Spideyofficial_777
# Ask Doubt on telegram @hacker_x_official_777

# Clone Code Credit : YT - @Spidey_official_777 / TG - @hacker_x_official_777/ GitHub - @Spideyofficial777

import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("**You are very lucky 🤞 I am alive ❤️ Press /start to use me**")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
