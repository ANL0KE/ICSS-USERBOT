
from telethon import events, Button, custom
import re, os
from . import ICSBOT

@bot.on(events.NewMessage(pattern=("/alive|/start")))
async def awake(event):
  ics = "hii\n"
  ics += f"heloo {ICSBOT}"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{ICSBOT} 𝚁𝙴𝙿𝙾", "https://github.com/ANL0KE/ICSS-USERBOT")]]
  await bot.send_file(event.chat_id, caption=ics, buttons=BUTTON)

@bot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await bot.send_message(event.chat, "thnx", buttons=[[Button.url("⚜️ icsd ⚜️", "https://github.com/ANL0KE/ICSS-USERBOT")]])

