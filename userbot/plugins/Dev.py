#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from ..Config import Config
from . import ALIVE_NAME, ICSB, tosh, mention, icsv

ICSP = Config.ALIVE_PIC if Config.ALIVE_PIC else "https://telegra.ph/file/3d9adda877b7fc7fee418.jpg"
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
            
