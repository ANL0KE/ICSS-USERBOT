from telethon import events, Button
from ..Config import Config

K = "https://t.me/rruuurr"

@icss.on(icss_cmd(pattern="تيست1"))
async def _(e):
    await eor(e,
        "⌔∮ 𝙎𝙊𝙐𝙍𝘾𝙀 𝙄𝘾𝙎𝙎 - 𝙍𝙀𝙋𝙊 𓆪",
        buttons=[[Button.url("🔗 𝙍𝙀𝙋𝙊 🔗", K)]]
    )
