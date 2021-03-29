#    Icss - Userbot
#    Owner - @rruuurr

from telethon import events, Button
from . import R, K

@icssbot.on(icss_cmd(pattern="repo$"))
@icssbot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def icsrepo(icsp):
    await eor(icsp, R)


@tgbot.on(
    events.NewMessage(pattern=("/repo|#repo"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat,
        "⌔∮ 𝙎𝙊𝙐𝙍𝘾𝙀 𝙄𝘾𝙎𝙎 - 𝙍𝙀𝙋𝙊 𓆪",
        buttons=[[Button.url("🔗 𝙍𝙀𝙋𝙊 🔗", K)]]
    )
   


