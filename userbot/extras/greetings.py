import random


@icssbot.on(admin_cmd(pattern=f"gm$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="gm$", allow_sudo=True))
async def morning(morning):
    txt = random.choice(icsmemes.GDMORNING)
    await edit_or_reply(morning, txt)


@icssbot.on(admin_cmd(pattern=f"gnoon$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="gnoon$", allow_sudo=True))
async def noon(noon):
    txt = random.choice(icsmemes.GDNOON)
    await edit_or_reply(noon, txt)


@icssbot.on(admin_cmd(pattern=f"gn$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="gn$", allow_sudo=True))
async def night(night):
    txt = random.choice(icsmemes.GDNIGHT)
    await edit_or_reply(night, txt)


@icssbot.on(admin_cmd(pattern="gmg$"))
@icssbot.on(sudo_cmd(pattern="gmg$", allow_sudo=True))
async def gm(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･\n╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭╮\n╭━┳━┳━┳╯┃╭━━┳━┳┳┳━┳╋╋━┳┳━╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃╋┃╭┫┃┃┃┃┃┃┃╋┃\n┣╮┣━┻━┻━╯╰┻┻┻━┻╯╰┻━┻┻┻━╋╮┃\n╰━╯╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･｡♥｡･ﾟ♡ﾟ･",
    )


@icssbot.on(admin_cmd(pattern="gnt$"))
@icssbot.on(sudo_cmd(pattern="gnt$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "｡♥｡･ﾟ♡ﾟ･｡♥｡･｡･｡･｡♥｡･\n╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮\n╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮\n┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫\n┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯\n╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯\n｡♥｡･ﾟ♡ﾟ･｡♥° ♥｡･ﾟ♡ﾟ･",
    )


# ©icss - @rruuurr


@icssbot.on(admin_cmd(pattern=r"hi ?(.*)"))
@icssbot.on(sudo_cmd(pattern=r"hi ?(.*)", allow_sudo=True))
async def hi(event):
    giveVar = event.text
    ics = giveVar[4:5]
    if not ics:
        ics = "🌺"
    await eor(
        event,
        f"{ics}✨✨{ics}✨{ics}{ics}{ics}\n{ics}✨✨{ics}✨✨{ics}✨\n{ics}{ics}{ics}{ics}✨✨{ics}✨\n{ics}✨✨{ics}✨✨{ics}✨\n{ics}✨✨{ics}✨{ics}{ics}{ics}\n☁☁☁☁☁☁☁☁",
    )


@icssbot.on(admin_cmd(pattern=r"cheer$"))
@icssbot.on(sudo_cmd(pattern="cheer$", allow_sudo=True))
async def cheer(event):
    if event.fwd_from:
        return
    await eor(
        event,
        "💐💐😉😊💐💐\n☕ Cheer Up  🍵\n🍂 ✨ )) ✨  🍂\n🍂┃ (( * ┣┓ 🍂\n🍂┃*💗 ┣┛ 🍂 \n🍂┗━━┛  🍂🎂 For YOU  🍰\n💐💐😌😚💐💐",
    )


@icssbot.on(admin_cmd(pattern=r"getwell$"))
@icssbot.on(sudo_cmd(pattern="getwell$", allow_sudo=True))
async def getwell(event):
    if event.fwd_from:
        return
    await eor(
        event, "🌹🌹🌹🌹🌹🌹🌹🌹 \n🌹😷😢😓😷😢💨🌹\n🌹💝💉🍵💊💐💝🌹\n🌹 GetBetter Soon! 🌹\n🌹🌹🌹🌹🌹🌹🌹🌹"
    )


@icssbot.on(admin_cmd(pattern=r"luck$"))
@icssbot.on(sudo_cmd(pattern="luck$", allow_sudo=True))
async def luck(event):
    if event.fwd_from:
        return
    await eor(
        event, "💚~🍀🍀🍀🍀🍀\n🍀╔╗╔╗╔╗╦╗✨🍀\n🍀║╦║║║║║║👍🍀\n🍀╚╝╚╝╚╝╩╝。 🍀\n🍀・・ⓁⓊⒸⓀ🍀\n🍀🍀🍀 to you💚"
    )


@icssbot.on(admin_cmd(pattern=r"sprinkle$"))
@icssbot.on(sudo_cmd(pattern="sprinkle$", allow_sudo=True))
async def sprinkle(event):
    if event.fwd_from:
        return
    await eor(
        event,
        "✨.•*¨*.¸.•*¨*.¸¸.•*¨*• ƸӜƷ\n🌸🌺🌸🌺🌸🌺🌸🌺\n Sprinkled with love❤\n🌷🌻🌷🌻🌷🌻🌷🌻\n ¨*.¸.•*¨*. ¸.•*¨*.¸¸.•*¨`*•.✨\n🌹🍀🌹🍀🌹🍀🌹🍀",
    )


CMD_HELP.update(
    {
        "greetings": """**Plugin : **`greetings`

**Syntax : **
  •  `.gm`
  •  `.gnoon`
  •  `.gn`  
**Function : **__sends you random good morning , afternoon and night quotes respectively.__

**Syntax : **
  •  `.gnt`
  •  `.gmg`
  •  `.hi/.hi emoji`
  •  `.cheer`
  •  `.getwell`
  •  `.luck`
  •  `.sprinkle`
**Function : **__shows you some text arts for these greeting commands.__"""
    }
)
