I = (
    " ___ ____ ____ ____\n"
    "|_ _/ ___/ ___/ ___|\n"
    "-| | |   \___ \___ \ \n"
    "-| | |___ ___) |__) |\n"
    "|___\____|____/____/\n"
)

T = (
    "🔱 | 𝗻𝗮𝗺𝗲 :\n"
    "🔱 | 𝗳𝗿𝗼𝗺 :\n"
    "🔱 | 𝗮𝗴𝗲 :\n"
    "🔱 | 𝗤𝘂𝗼𝘁𝗲 :\n"
    " 𝒀𝑶𝑼 𝑭𝑶𝑹𝑮𝑶𝑻 𝑯𝑶𝑾 𝑻𝑶 𝑳𝑶𝑽𝑬. 𝑨𝑮𝑨𝑰𝑵\n"
)


@icssbot.on(admin_cmd(pattern="icss", outgoing=True))
async def kimo(ics):
    return await edit_or_reply(ics, I)


@icssbot.on(admin_cmd(pattern="poo", outgoing=True))
async def poo(pio):
    return await edit_or_reply(pio, T)
