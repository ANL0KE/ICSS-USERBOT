
from telethon import events, Button, custom
import re, os
from userbot.Config import Config
from userbot.assistant.tosh import *
from . import ICSBOT

LOAD_MYBOT = Config.TG_BOT_USERNAME
BOT_PIC = Config.ALIVE_PIC if ALIVE_PIC else None
OWNER_ID = Config.OWNER_ID

@bot.on(events.NewMessage(pattern=("/alive")))
async def awake(event):
  ics = "hii\n"
  ics += f"heloo {ICSBOT}"
  BUTTON = [[Button.url("𝙼𝙰𝚂𝚃𝙴𝚁", f"https://t.me/{bot.me.username}"), Button.url(f"{ICSBOT} 𝚁𝙴𝙿𝙾", "https://github.com/ANL0KE/ICSS-USERBOT")]]
  await bot.send_file(event.chat_id, caption=ics, buttons=BUTTON)


@tgbot.on(events.NewMessage(pattern=("/repo|#repo")))
async def repo(event):
  await tgbot.send_message(event.chat, "thnx", buttons=[[Button.url("⚜️ icsd ⚜️", "https://github.com/ANL0KE/ICSS-USERBOT")]])


@tgbot.on(events.NewMessage(pattern="^/start"))  # pylint: disable=oof
async def start_all(event):
    if event.chat_id == OWNER_ID:
        return
    target = event.sender_id
    if present_in_userbase(target):
        pass
    else:
        try:
            add_to_userbase(target)
        except BaseException:
            pass
    if LOAD_MYBOT == "False":
        if BOT_PIC:
            await tgbot.send_file(event.chat_id,
                                  BOT_PIC,
                                  caption=startotherdis,
                                  buttons=[
                                      (Button.inline(
                                          "What can I do here?",
                                          data="wew"))]
                                  )
        else:
            await tgbot.send_message(event.chat_id,
                                     startotherdis,
                                     buttons=[
                                         (Button.inline(
                                             "What can I do here?",
                                             data="wew"))]
                                     )
    elif LOAD_MYBOT == "True":
        if BOT_PIC:
            await tgbot.send_file(event.chat_id,
                                  BOT_PIC,
                                  caption=startotherena,
                                  buttons=[
                                      [Button.url(
                                          "TeleBot", url="https://github.com/ANL0KE/ICSS-USERBOT")],
                                      [Button.inline(
                                          "Whats this?", data="telebot")]
                                  ]
                                  )
        else:
            await tgbot.send_message(event.chat_id,
                                     startotherena,
                                     buttons=[
                                         [Button.url(
                                             "Kimo", url="https://t.me/rruuurr")],
                                         [Button.inline(
                                             "Whats this?", data="telebot")]
                                     ]
                                     )
