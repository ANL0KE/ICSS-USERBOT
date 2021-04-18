import asyncio

from ..kimo import *

@icssbot.on(
    icss_cmd(pattern="ببب$")
)
async def _(event):
    e = await eor(event, "yyy")
    chat = "@BotFather"
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await asyinco.sleep(1)
            await conv.send_message(/setname)
            await asyinco.sleep(1)
            await conv.send_message(TBOT)
            await asyinco.sleep(1)
            await conv.send_message(ALIVE_NAME)
            await event.client.send_read_acknowledge(conv.chat_id)
            await e.edit("uuuuu")
