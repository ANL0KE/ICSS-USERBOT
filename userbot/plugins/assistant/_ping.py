import time
from telethon import events
from datetime import datetime
from . import *
from .. import StartTime


@tgbot.on(
    events.NewMessage(pattern=("بنك"))
)
async def _(e):
    Start = datetime.now()
    End = datetime.now()
    Ms = (end - start).microseconds / 1000
    UpTime = get_readable_time((time.time() - StartTime))
    await tgbot.send_message(e.chat_id, Ping.format(Ms, UpTime))
