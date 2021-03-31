#   ICSS - USERBOT
#   TELE - @NIIIN2

from telethon import events
from datetime import datetime

@tgbot.on(events.NewMessage(pattern="/ping",
                            from_users=OWNER_ID))
async def _(event):
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await tgbot.send_message(
        event.chat,
        f"**Pong!!**\n `{ms}ms`"
    )
