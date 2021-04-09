# animation code for icss edit by @rruuurr

import asyncio
from collections import deque


@icssbot.on(admin_cmd(pattern="افكر$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="افكر$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, ".🧐")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern=r"متت$"))
@icssbot.on(sudo_cmd(pattern="متت$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, ".🤣")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern=r"ضايج$"))
@icssbot.on(sudo_cmd(pattern="ضايج$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🙂.")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(outgoing=True, pattern="ساعه$"))
@icssbot.on(sudo_cmd(pattern="ساعه$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🕙.")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern=r"مح$"))
@icssbot.on(sudo_cmd(pattern="مح$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "😗.")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern="قلب$"))
@icssbot.on(sudo_cmd(pattern="قلب$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🧡.")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern="جيم$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="جيم$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "جيم")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern=f"الارض$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="الارض$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🌏.")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(outgoing=True, pattern="قمر$"))
@icssbot.on(sudo_cmd(pattern="قمر$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🌗.")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@icssbot.on(admin_cmd(pattern=f"اقمار$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="اقمار$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "🌗.")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("⇆")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@icssbot.on(admin_cmd(pattern=f"قمور$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="قمور$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await eor(event, "قمور..")
    animation_interval = 0.1
    animation_ttl = range(96)
    await event.edit("tmoon..")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])


CMD_HELP.update(
    {
        "animation2": """**Plugin : **`animation2`
        
**Commands in animation2 are **
  •  `.think`
  •  `.lmao`
  •  `.nothappy`
  •  `.clock`
  •  `.muah`
  •  `.heart`
  •  `.gym`
  •  `.earth`
  •  `.moon`
  •  `.smoon`
  •  `.tmoon`
  
**Function : **__Different kinds of animation commands check yourself for their animation .__"""
    }
)
