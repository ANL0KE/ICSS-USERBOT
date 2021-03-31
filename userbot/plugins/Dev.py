#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from . import ALIVE_NAME, mention

@tgbot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    await kimo.reply("مطور بوت اكسس", buttons=[[Button.url("🔱 المطور 🔱", "https://t.me/rruuurr")]])
