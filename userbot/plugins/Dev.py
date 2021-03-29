#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
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
            

@tgbot.on(
    events.NewMessage(pattern=("/ics"))
)
async def repo(event):
    if event.fwd_from:
        return
    KIM = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await tgbot.send_message(KIM, "البوت")
    await response[0].click(event.chat_id)
    await event.delete()
