#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from . import ALIVE_NAME, tosh, mention, ONWER_ID

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
             

@tgbot.on(
    events.NewMessage(pattern=("/icss"))
)
async def owner(event):
    await tgbot.send_message(event.chat,
                             "هها حب",
                             buttons=[
                                 [Button.url(
                                     "المطور ⚙️", "https://t.me/NIIIN2"),
                                  Button.url(
                                     "رابط السورس ⚙️", "https://github.com/ANL0KE/ICSS-USERBOT")],
                                 [Button.url("للمساعده",
                                             "https://t.me/rruuurr")]
                             ])
