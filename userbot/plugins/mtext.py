import random

from . import ALIVE_NAME, icssmemes

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "icss"


@icssbot.on(admin_cmd(pattern="congo$"))
@icssbot.on(sudo_cmd(pattern="congo$", allow_sudo=True))
async def _(i):
    txt = random.choice(icssmemes.CONGOREACTS)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="shg$"))
@icssbot.on(sudo_cmd(pattern="shg$", allow_sudo=True))
async def shrugger(i):
    txt = random.choice(icssmemes.SHGS)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="runs$"))
@icssbot.on(sudo_cmd(pattern="runs$", allow_sudo=True))
async def runner_lol(i):
    txt = random.choice(icssmemes.RUNSREACTS)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="noob$"))
@icssbot.on(sudo_cmd(pattern="noob$", allow_sudo=True))
async def metoo(i):
    txt = random.choice(icssmemes.NOOBSTR)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="insult$"))
@icssbot.on(sudo_cmd(pattern="insult$", allow_sudo=True))
async def insult(i):
    txt = random.choice(icssmemes.INSULT_STRINGS)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="hey$"))
@icssbot.on(sudo_cmd(pattern="hey$", allow_sudo=True))
async def hoi(i):
    txt = random.choice(icssmemes.HELLOSTR)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="pro$"))
@icssbot.on(sudo_cmd(pattern="pro$", allow_sudo=True))
async def proo(i):
    txt = random.choice(icssmemes.PRO_STRINGS)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(pattern=f"react ?(.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="react ?(.*)", allow_sudo=True))
async def _(i):
    input_str = i.pattern_match.group(1)
    if input_str in "happy":
        emoticons = icssmemes.FACEREACTS[0]
    elif input_str in "think":
        emoticons = icssmemes.FACEREACTS[1]
    elif input_str in "wave":
        emoticons = icssmemes.FACEREACTS[2]
    elif input_str in "wtf":
        emoticons = icssmemes.FACEREACTS[3]
    elif input_str in "love":
        emoticons = icssmemes.FACEREACTS[4]
    elif input_str in "confused":
        emoticons = icssmemes.FACEREACTS[5]
    elif input_str in "dead":
        emoticons = icssmemes.FACEREACTS[6]
    elif input_str in "sad":
        emoticons = icssmemes.FACEREACTS[7]
    elif input_str in "dog":
        emoticons = icssmemes.FACEREACTS[8]
    else:
        emoticons = icssmemes.FACEREACTS[9]
    txt = random.choice(emoticons)
    await edit_or_reply(i, txt)


@icssbot.on(admin_cmd(outgoing=True, pattern="10iq$"))
@icssbot.on(sudo_cmd(pattern="10iq$", allow_sudo=True))
async def iqless(i):
    await edit_or_reply(i, "♿")


@icssbot.on(admin_cmd(pattern="fp$"))
@icssbot.on(sudo_cmd(pattern=f"fp$", allow_sudo=True))
async def facepalm(i):
    await i.edit("🤦‍♂")


@icssbot.on(admin_cmd(outgoing=True, pattern="bt$"))
@icssbot.on(sudo_cmd(pattern="bt$", allow_sudo=True))
async def bluetext(i):
    if i.is_group:
        await edit_or_reply(
            i,
            "/BLUETEXT /MUST /CLICK.\n"
            "/ARE /YOU /A /STUPID /ANIMAL /WHICH /IS /ATTRACTED /TO /COLOURS?",
        )


@icssbot.on(admin_cmd(pattern="session$"))
@icssbot.on(sudo_cmd(pattern="session$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**telethon.errors.rpcerrorlist.AuthKeyDuplicatedError: The authorization key (session file) was used under two different IP addresses simultaneously, and can no longer be used. Use the same session exclusively, or use different sessions (caused by GetMessagesRequest)**"
    await event.edit(mentions)


CMD_HELP.update(
    {
        "memestext": "**Plugin : **`memestext`\
        \n\n  •  **Syntax :** `.congo`\
        \n  •  **Function : **Congratulate the people.\
        \n\n  •  **Syntax :** `.shg`\
        \n  •  **Function : **Shrug at it !!\
        \n\n  •  **Syntax :** `.runs`\
        \n  •  **Function : **Run, run, RUNNN!\
        \n\n  •  **Syntax :** `.noob`\
        \n  •  **Function : **Whadya want to know? Are you a NOOB?\
        \n\n  •  **Syntax :** `.insult`\
        \n  •  **Function : **insult someone\
        \n\n  •  **Syntax :** `.hey`\
        \n  •  **Function : **start a conversation with people\
        \n\n  •  **Syntax :** `.pro`\
        \n  •  **Function : **If you think you're pro, try this.\
        \n\n  •  **Syntax :** `.react` <type>\
        \n  •  **Function : **Make your userbot react. types are <happy ,think ,wave ,wtf ,love ,confused,dead, sad,dog>\
        \n\n  •  **Syntax :** `.10iq`\
        \n  •  **Function : **You retard !!\
        \n\n  •  **Syntax :** `.fp`\
        \n  •  **Function : **send you face pam emoji!\
        \n\n  •  **Syntax :** `.bt`\
        \n  •  **Function : **Believe me, you will find this useful.\
        \n\n  •  **Syntax :** `.session`\
        \n  •  **Function : **telethon session error code(fun)\
        "
    }
)
