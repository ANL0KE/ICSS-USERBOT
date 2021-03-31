#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from . import K, D

@tgbot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    await kimo.reply(D, buttons=[[Button.url("🔱 المطور 🔱", Kim)]])
