#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from . import tosh, mention

@tgbot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat, "مطور بوت اكسس", buttons=[[Button.url("✨ المطور ✨", "https://t.me/rruuurr")]])
   
@tgbot.on(
    events.NewMessage(pattern=("/start"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat, f"اهلا بك - {mention}\n انا بوت مساعد للمستخدم {ALIVE_NAME} ", buttons=[[Button.url("✨ المطور ✨", "https://t.me/rruuurr")]])
             
