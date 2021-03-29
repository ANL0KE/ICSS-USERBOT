#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events
from . import tosh, reply_id

@tgbot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat, tosh)
        
