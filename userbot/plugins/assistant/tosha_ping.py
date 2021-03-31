#   ICSS - USERBOT
#   TELE - @NIIIN2

from telethon import events
from datetime import datetime
from .. import StartTime, get_readable_time

@tgbot.on(events.NewMessage(pattern="^/ping",
                            from_users=OWNER_ID)) 
async def botping(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    get_readable_time(time.time() - StartTime))
    await tgbot.send_message(
        f"⌔∮ **سرعه الاستجابه ↫** `{ms}` ** ⇲**"
    )
