#    Icss - Userbot
#    Owner - @rruuurr

from telethon import events, Button
from ..Config import Config
from . import R, K, mention

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
   

TOSH = f"**- اهلا بك انا {ICSB} بوت اكسس مساعد **\n**- للمستخدم** : {mention}"
TOSH_PIC = "https://telegra.ph/file/85dc02885566034ef51a4.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await bot.get_me()
        if query.startswith("alive") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("الرابط", K),
                    Button.url("القناة", "https://t.me/rruuurr"),
                ]
            ]
            if TOSH_PIC and TOSH_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(
                    TOSH_PIC,
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False
                )
            elif ALIVE_PHOTTO:
                result = builder.document(
                    TOSH_PIC,
                    title="ICSS - USERBOT",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            else:
                result = builder.article(
                    title="ICSS - USERBOT",
                    text=TOSH,
                    buttons=buttons,
                    link_preview=False,
                )
            await event.answer([result] if result else None)

