import time
from platform import python_version
from telethon import version
from . import StartTime, mention, icsv, get_readable_time as grt

@icssbot.on(
    icss_cmd(pattern="alive$")
)
async def lol(tosh):
    pic = Config.ALIVE_PIC or "https://telegra.ph/file/648b0cab5d52daa8b19f6.jpg"
    icsupt = await grt(time.time() - StartTime)
    kim = (alive_1.format(
        version.__version__,
        icsv,
        python_version(),
        mention
    )
    if pic:
            await tosh.reply(kim, file=pic)
            await tosh.delete()
        except ChatSendMediaForbiddenError:
            await eor(tosh, kim)
    else:
        try:
            await bot.send_message(tosh.chat_id, file=pic)
            await bot.send_message(tosh.chat_id, kim)
            await tosh.delete()
        except ChatSendMediaForbiddenError:
            await eor(tosh, kim)
    if pic is None:
        return await eor(tosh, kim)
