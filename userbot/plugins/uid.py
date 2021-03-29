import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
from . import *
from userbot.kimo import *
import random
from telethon import events, Button, custom
from telethon.tl.custom import Button
from telethon.tl.types import ChannelParticipantsAdmins 
ok = bot.uid
from PIL import Image
import requests
from io import BytesIO
from userbot.Confg import Config

ALIVE_NAME = Config.ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "**@rruuurr**"

pro_text=(f"**{ICSB} IS ON FIRE **\n\n**Yes Master, Am Alive And Systems Are Working Perfectly As It Should Be...**\n\n🔥 About My System 🔥\n➾ **ʟɪᴄᴇɴꜱᴇ**  ☞ [ANL0KE](https://github.com/ANL0KE)\n➾ **ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ** ☞ [ICSS-USERBOT](https://github.com/ANL0KE/ICSS-USERBOT)\n\n➾ **ᴍʏ ᴍᴀsᴛᴇʀ** ☞ [{DEFAULTUSER}](tg://user?id={ok})\n")
TG_BOT_USERNAME = os.environ.get("ALIVE_PIC", None)
if TG_BOT_USERNAME is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await borg.get_me()
        if query.startswith("alive") and event.query.user_id == me.id:
            buttons = [
                [
                    Button.url("Repo", "https://github.com/ANL0KE/ICSS-USERBOT"),
                    Button.url("Deploy", "https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FANL0KE%2FICSSBACK")],
                    [Button.url("String", "https://repl.it/ANL0KE/ICSS#main.py"),
                    Button.url("Channel", "https://t.me/rruuurr"),
                ]
            ]
            if ALIVE_PIC and ALIVE_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    ALIVE_PIC,
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    ALIVE_PHOTTO,
                    title="ICSS BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="ICSS BOT",
                    text=pro_text,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)


@bot.on(admin_cmd(outgoing=True, pattern="alive"))
async def repo(event):
    if event.fwd_from:
        return
    TOSH = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(TOSH, "alive")
    await response[0].click(event.chat_id)
    await event.delete()
