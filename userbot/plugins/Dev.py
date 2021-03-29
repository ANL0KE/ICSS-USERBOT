#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from ..Config import Config
from . import ALIVE_NAME, tosh, mention

@tgbot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat, "مطور بوت اكسس", buttons=[[Button.url("✨ المطور ✨", "https://t.me/rruuurr")]])
   
@tgbot.on(
    events.NewMessage(pattern=("/start"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat, f"**- اني بوت مساعد للمستخدم** {mention}", buttons=[[Button.url("✨ المطور ✨", "https://t.me/rruuurr")]])
            
