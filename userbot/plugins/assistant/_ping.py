import time
from telethon import events
from datetime import datetime
from . import *

@tgbot.on(
    events.NewMessage(pattern=("بنك"))
)
async def _(e):
    Start = datetime.now()
    End = datetime.now()
    Ms = (end - start).microseconds / 1000
    UpTime = get_readable_time((time.time() - StartTime))
    await e.reply(Ping.format(Ms, UpTime))
