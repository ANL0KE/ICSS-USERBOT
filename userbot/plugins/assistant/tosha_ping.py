#   ICSS - USERBOT
#   TELE - @NIIIN2

import time
from telethon import events
from . get_readable_time
from .. import StartTime

@tgbot.on(events.NewMessage(pattern="^/ping",
                            from_users=OWNER_ID)) 
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    uptime = get_readable_time((time.time() - StartTime))
    await tgbot.send_message(event.chat, 
        f"⌔∮ **سرعه الاستجابه ↫** `{ms}` ** ⇲**"
    )
