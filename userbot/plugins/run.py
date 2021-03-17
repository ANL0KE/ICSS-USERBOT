import asyncio
from collections import deque



@icssbot.on(admin_cmd(pattern="هااا$"))
@icssbot.on(sudo_cmd(pattern="هااا$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(14)
    event = await edit_or_reply(event, "انتضر شويه")
    animation_chars = [
        ": /",
        ": \",
        ": /",
        ": \",
        ": /",
        ": \",
        ": /",
        ": \",
        ": /",
        ": \",
        ": /",
        ": \",
        ": /",
        ": \",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 14])
