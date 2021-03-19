
from telethon import events, Button, custom
import re, os
from . import ICSBOT
from .IcssGif import *
from userbot import bot
@bot.on(events.NewMessage(pattern=("/alive|/start")))
async def awake(event):
  ics = f"ʜᴇʟʟᴏ ᴛʜɪs ɪs  {ICSBOT}\n\n"
  ics += "ᴀʟʟ sʏsᴛᴇᴍ ɪs ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
  ics += f"{BOT} ᴏs : 3.0 ʟᴀsᴛᴇsᴛ\n\n"
  ics += f"ᴍʏ ᴍᴀsᴛᴇʀ @{bot.me.username} ☺️\n\n"
  ics += "ғᴜʟʟʏ ᴜᴘᴅᴀᴛᴇᴅ ʙᴏᴛ\n\n"
  ics += "ᴛᴇʟᴇᴛʜᴏɴ : 1.20 LATEST\n\n"
  ics += "ᴛʜᴀɴᴋs ғᴏʀ ᴄʜᴇᴄᴋɪɴɢ ᴍᴇ"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{ICSBOT} 𝚁𝙴𝙿𝙾", "https://github.com/ANL0KE/ICSS")]]
  await bot.send_file(event.chat_id, kut_gif, caption=ics,  buttons=BUTTON)
