icss = [
    " ___ ____ ____ ____",
    "|_ _/ ___/ ___/ ___|",
    " | | |   \___ \___ \ ",
    " | | |___ ___) |__) |",
    "|___\____|____/____/",
]

tosh = [
    "🔱 | 𝗻𝗮𝗺𝗲 :",
    "🔱 | 𝗳𝗿𝗼𝗺 :",
    "🔱 | 𝗮𝗴𝗲 :",
    "🔱 | 𝗤𝘂𝗼𝘁𝗲 :",
    " 𝒀𝑶𝑼 𝑭𝑶𝑹𝑮𝑶𝑻 𝑯𝑶𝑾 𝑻𝑶 𝑳𝑶𝑽𝑬. 𝑨𝑮𝑨𝑰𝑵",
]


@icssbot.on(admin_cmd(pattern="icss", outgoing=True))
async def kimo(ics):
    await edit_or_reply(ics, icss)


@icssbot.on(admin_cmd(pattern="Poo", outgoing=True))
async def poo(pio):
    await edit_or_reply(pio, tosh)
