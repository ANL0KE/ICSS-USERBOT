#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events
from . import tosh

@bot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    await bot.send_message(kimo.chat, tosh)
        
