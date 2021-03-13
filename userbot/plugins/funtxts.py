import nekos


@icssbot.on(admin_cmd(pattern="tcat$"))
@icssbot.on(sudo_cmd(pattern="tcat$", allow_sudo=True))
async def hmm(cat):
    if cat.fwd_from:
        return
    reactcat = nekos.textcat()
    await edit_or_reply(cat, reactcat)


@icssbot.on(admin_cmd(pattern="why$"))
@icssbot.on(sudo_cmd(pattern="why$", allow_sudo=True))
async def hmm(cat):
    if cat.fwd_from:
        return
    whycat = nekos.why()
    await edit_or_reply(cat, whycat)


@icssbot.on(admin_cmd(pattern="fact$"))
@icssbot.on(sudo_cmd(pattern="fact$", allow_sudo=True))
async def hmm(cat):
    if cat.fwd_from:
        return
    factcat = nekos.fact()
    await edit_or_reply(cat, factcat)


CMD_HELP.update(
    {
        "funtxts": """**Plugin : **`funtxts`

  •  **Syntax : **`.tcat`
  •  **Function : **__Sens you some random cat facial text art__

  •  **Syntax : **`.why`
  •  **Function : **__Asks some random Funny questions__

  •  **Syntax : **`.fact`
  •  **Function : **__Sends you some random facts__"""
    }
)
