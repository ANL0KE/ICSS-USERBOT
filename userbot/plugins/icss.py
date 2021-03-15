icss = [
    " ___ ____ ____ ____",
    "|_ _/ ___/ ___/ ___|",
    " | | |   \___ \___ \ ",
    " | | |___ ___) |__) |",
    "|___\____|____/____/",
]


@icssbot.on(admin_cmd(pattern="icss", outgoing=True))
async def kimo(ics):
    kim = icss
    return await ics.edit(kim)


tosh = [
    "🔱 | 𝗻𝗮𝗺𝗲 :",
    "🔱 | 𝗳𝗿𝗼𝗺 :",
    "🔱 | 𝗮𝗴𝗲 :",
    "🔱 | 𝗤𝘂𝗼𝘁𝗲 :",
    " 𝒀𝑶𝑼 𝑭𝑶𝑹𝑮𝑶𝑻 𝑯𝑶𝑾 𝑻𝑶 𝑳𝑶𝑽𝑬. 𝑨𝑮𝑨𝑰𝑵",
]


@icssbot.on(admin_cmd(pattern="Poo", outgoing=True))
async def poo(pio):
    th = tosh
    return await pio.edit(th)
