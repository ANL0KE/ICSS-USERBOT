#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events
from . import tosh, reply_id

@bot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    rd = await reply_id(kimo)
    await bot.send_message(kimo.chat, tosh, reply_to=rd)
        
