import asyncio
import random


@icssbot.on(admin_cmd(outgoing=True, pattern="abuse$"))
@icssbot.on(sudo_cmd(pattern="abuse$", allow_sudo=True))
async def abusing(abused):
    reply_text = random.choice(catmemes.ABUSE_STRINGS)
    await edit_or_reply(abused, reply_text)


@icssbot.on(admin_cmd(outgoing=True, pattern="abusehard$"))
@icssbot.on(sudo_cmd(pattern="abusehard$", allow_sudo=True))
async def fuckedd(abusehard):
    reply_text = random.choice(catmemes.ABUSEHARD_STRING)
    await edit_or_reply(abusehard, reply_text)


@icssbot.on(admin_cmd(outgoing=True, pattern="rendi$"))
@icssbot.on(sudo_cmd(pattern="rendi$", allow_sudo=True))
async def metoo(e):
    txt = random.choice(catmemes.RENDISTR)
    await edit_or_reply(e, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="rape$"))
@icssbot.on(sudo_cmd(pattern="rape$", allow_sudo=True))
async def raping(raped):
    reply_text = random.choice(catmemes.RAPE_STRINGS)
    await edit_or_reply(raped, reply_text)


@icssbot.on(admin_cmd(outgoing=True, pattern="fuck$"))
@icssbot.on(sudo_cmd(pattern="fuck$", allow_sudo=True))
async def chutiya(fuks):
    reply_text = random.choice(catmemes.CHU_STRINGS)
    await edit_or_reply(fuks, reply_text)


@icssbot.on(admin_cmd(outgoing=True, pattern="thanos$"))
@icssbot.on(sudo_cmd(pattern="thanos$", allow_sudo=True))
async def thanos(thanos):
    reply_text = random.choice(catmemes.THANOS_STRINGS)
    await edit_or_reply(thanos, reply_text)


@icssbot.on(admin_cmd(outgoing=True, pattern="kiss$"))
@icssbot.on(sudo_cmd(pattern="kiss$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`kiss`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@icssbot.on(admin_cmd(outgoing=True, pattern="fuk$"))
@icssbot.on(sudo_cmd(pattern="fuk$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`fuking....`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


@icssbot.on(admin_cmd(outgoing=True, pattern="sex$"))
@icssbot.on(sudo_cmd(pattern="sex$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    catevent = await edit_or_reply(event, "`sex`")
    animation_interval = 0.2
    animation_ttl = range(100)
    animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await catevent.edit(animation_chars[i % 4])


CMD_HELP.update(
    {
        "gali": "**plugin : **`gali`\
        \n\n**Commands :**\
        \n  •  `.abuse`\
        \n  •  `.abusehard`\
        \n  •  `.rendi`\
        \n  •  `.rape`\
        \n  •  `.fuck`\
        \n  •  `.thanos`\
        \n  •  `.kiss`\
        \n  •  `.fuk`\
        \n  •  `.sex`\
        \n\n**Function :**\
        \n__First 5 are random gali string generaters__\
        \n__Last 3 are animations__\
        "
    }
)
