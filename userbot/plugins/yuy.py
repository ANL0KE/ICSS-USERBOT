import time
from platform import python_version
from telethon import version
from telethon.errors.rpcerrorlist import ChatSendMediaForbiddenError
from ..Config import Config
from . import StartTime, mention, icsv, alive_1

@icssbot.on(
    icss_cmd(pattern="alive$")
)
async def lol(tosh):
    Tpic = Config.ALIVE_PIC or "https://telegra.ph/file/648b0cab5d52daa8b19f6.jpg"
    kim = (alive_1.format(
        version.__version__,
        icsv,
        python_version(),
        mention
    )
    if Tpic:
            await tosh.reply(kim, file=Tpic)
            await tosh.delete()
        except ChatSendMediaForbiddenError:
            await eor(tosh, kim)
    else:
        try:
            await bot.send_message(tosh.chat_id, file=Tpic)
            await bot.send_message(tosh.chat_id, kim)
            await tosh.delete()
        except ChatSendMediaForbiddenError:
            await eor(tosh, kim)
