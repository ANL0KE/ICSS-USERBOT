import asyncio

from ..kimo import *

@icss.on(
    icss_cmd(pattern="ببب$")
)
async def _(event):
    if event.fwd_from:
        return
    e = await eor(event, "yyy")
    chat = "@BotFather"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await asyinco.sleep(1)
            await conv.send_message(/setname)
            await asyinco.sleep(0.1)
            await conv.send_message(TBOT)
            await asyinco.sleep(0.1)
            await conv.send_message(ALIVE_NAME)
            await e.edit("uuuuu")
