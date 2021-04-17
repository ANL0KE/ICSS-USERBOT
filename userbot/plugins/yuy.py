import time
from platform import python_version
from telethon import version
from ..Config import Config
from . import StartTime, mention, icsv, alive_1

Tpic = "https://telegra.ph/file/648b0cab5d52daa8b19f6.jpg"
kim = alive_1.format(version.__version__, icsv, python_version(), mention)

@icssbot.on(
    icss_cmd(pattern="alive")
)
async def lol(tosh):
    if Tpic:
        await tosh.reply(kim, file=Tpic)
        await tosh.delete()
        await eor(tosh, kim)
    else:
        try:
           await bot.send_message(tosh.chat_id, file=Tpic)
           await bot.send_message(tosh.chat_id, kim)
           await tosh.delete()
           await eor(tosh, kim)
  
