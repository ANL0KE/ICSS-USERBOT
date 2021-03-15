icss = (
    " ___ ____ ____ ____",
    "|_ _/ ___/ ___/ ___|",
    " | | |   \___ \___ \ ",
    " | | |___ ___) |__) |",
    "|___\____|____/____/",
)

tosh = (
    "🔱 | 𝗻𝗮𝗺𝗲 :",
    "🔱 | 𝗳𝗿𝗼𝗺 :",
    "🔱 | 𝗮𝗴𝗲 :",
    "🔱 | 𝗤𝘂𝗼𝘁𝗲 :",
    " 𝒀𝑶𝑼 𝑭𝑶𝑹𝑮𝑶𝑻 𝑯𝑶𝑾 𝑻𝑶 𝑳𝑶𝑽𝑬. 𝑨𝑮𝑨𝑰𝑵",
)


@icssbot.on(admin_cmd(pattern=r"icss$"))
async def kimo(ics):
    await ics.edit(icss)


@icssbot.on(admin_cmd(pattern=r"poo$"))
async def poo(pio):
    await pio.edit(tosh)
