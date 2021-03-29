#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from ..Config import Config
from . import ALIVE_NAME, tosh, mention

@tgbot.on(
    events.NewMessage(pattern=("المطور"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat, "مطور بوت اكسس", buttons=[[Button.url("✨ المطور ✨", "https://t.me/rruuurr")]])
   
@tgbot.on(
    events.NewMessage(pattern=("/start"))
)
async def dev(kimo):
    await tgbot.send_message(kimo.chat, f"**- اني بوت مساعد للمستخدم** {mention}", buttons=[[Button.url("✨ المطور ✨", "https://t.me/rruuurr")]])
            


TOSH_PIC = Config.ALIVE_PIC if Config.ALIVE_PIC else "https://telegra.ph/file/85dc02885566034ef51a4.jpg"
if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        me = await bot.get_me()
        if query.startswith("البوت") and event.query.user_id == bot.uid:
            buttons = [
                [
                    Button.url("🔗 الرابط 🔗", K),
                    Button.url("⚙️ المطور ⚙️", "https://t.me/rruuurr"),
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

@tgbot.on(
    events.NewMessage(pattern=("/ics"))
)
async def repo(event):
    if event.fwd_from:
        return
    KIM = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await tgbot.inline_query(KIM, "البوت")
    await response[0].click(event.chat_id)
    await event.delete()
