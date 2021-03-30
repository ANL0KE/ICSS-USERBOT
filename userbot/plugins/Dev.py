#  ICSS - USERBOT
#  TELE - @NIIIN2

from telethon import events, Button
from ..Config import Config
from . import ALIVE_NAME, ICSB, tosh, mention, icsv

ICSP = Config.ALIVE_PIC if Config.ALIVE_PIC else "https://telegra.ph/file/3d9adda877b7fc7fee418.jpg"
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
            
@tgbot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  TOSHA = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {ICSB}\n"
  TOSHA += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n"
  TOSHA += f"{ICSB} VERSION : {icsv} ʟᴀsᴛᴇsᴛ\n"
  TOSHA += f"ᴍʏ ᴍᴀsᴛᴇʀ {mention} ☺️\n"
  TOSHA += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n"
  TOSHA += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTON += [[Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="ICSUSERBOT")]]
  await tgbot.send_file(event.chat, ICSP, caption=TOSHA,  buttons=BUTTON)




@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ICSUSERBOT")))
async def callback_query_handler(event):
  TOSHA = [[Button.url("REPO-ICSS", "https://github.com/ANL0KE/ICSS-USERBOT")]]
  TOSHA +=[[Button.url("DEPLOY-ICSS", "https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FANL0KE%2FICSSBACK")]]
  TOSHA +=[[Button.url("API_ID & HASH", "https://t.me/usetgxbot"), Button.url("REDIS", "https://redislabs.com")]]
  TOSHA +=[[Button.url("SUPPORT CHANNEL", "https://t.me/rruuurr"), Button.url("ICSS DEV", "https://t.me/NIIIN2")]]
  TOSHA +=[[Button.inline("ALIVE", data="KIMO")]]
  await event.edit(text=f"𝙰𝙻𝙻 𝙳𝙴𝚃𝙰𝙸𝙻𝚂 𝙾𝙵 𝚁𝙴𝙿𝙾𝚂", buttons=TOSHA)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"KIMO")))
async def callback_query_handler(event):
  TOSHA = f" - ʜᴇʟʟᴏ ᴛʜɪs ɪs  {ICSB}\n"
  TOSHA += " - ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n"
  TOSHA += [[Button.inline("𝚁𝙴𝙿𝙾𝚂𝙸𝚃𝙾𝚁𝚈", data="ICSUSERBOT")]]
  await event.edit(text= TOSHA, buttons=BUTTONS)
