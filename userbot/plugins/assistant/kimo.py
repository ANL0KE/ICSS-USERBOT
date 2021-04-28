#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from . import K, D

@asst_cmd("المطور")
# for all
async def dev(kimo):
    await kimo.reply(D, buttons=[[Button.url("🔱 المطور 🔱", K)]])
