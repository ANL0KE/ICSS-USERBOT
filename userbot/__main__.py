# Icss - Userbot
# Owner - Kimo

import glob
import os
import sys
from pathlib import Path as P

import telethon.utils
from telethon.tl.functions.channels import JoinChannelRequest 
from telethon import TelegramClient as TC

from userbot.tosh import *
from userbot import LOGS, bot
from userbot.Config import Config
from userbot.utils import (
    load_module,
    load_admin, 
    load_anim, 
    load_tosha, 
    load_assistant,
)

async def startupmessage():
    try:
        if TOSHA != 0:
            await bot.send_message(TOSHA, MSGE)
    except Exception as e:
        LOGS.info(str(e))

async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error("{} -".format(Xe) + f"{str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if TBOT is not None:
            print(Mesg[0])
            bot.tgbot = TC(Xtbot, api_id=A, api_hash=H).start(bot_token=B)
            print(Mesg[1])
            print(Mesg[2])
            bot.loop.run_until_complete(add_bot(TBOT))
            print(Mesg[3])
        else:
            bot.start()
    except Exception as e:
        LOGS.error("{} -".format(Xt) + f"{str(e)}")
        sys.exit()


# For all plugins
print(Start)
print(StartLoaded)
Kim = glob.glob(Plg)
for name in Kim:
    with open(name) as k:
        Kim1 = P(k.name)
        shortname = Kim1.stem
        try:
            if shortname.replace(".py", "") not in N:
                load_module(shortname.replace(".py", ""))
            else:
                os.remove(P(Plugin.format(shortname)))
        except Exception as e:
            os.remove(P(Plugin.format(shortname)))
            print(IS.format(shortname, e))


# For admin tools
print(ADMIN)
Kim = glob.glob(Adm)
for name in Kim:
    with open(name) as k:
        Kim1 = P(k.name)
        shortname = Kim1.stem
        try:
            if shortname.replace(".py", "") not in N:
                load_admin(shortname.replace(".py", ""))
            else:
                os.remove(P(Admin.format(shortname)))
        except Exception as e:
            os.remove(P(Admin.format(shortname)))
            print(IS.format(shortname, e))


# for animations
print(ANIMATIONS)
Kim = glob.glob(Inm)
for name in Kim:
    with open(name) as k:
        Kim1 = P(k.name)
        shortname = Kim1.stem
        try:
            if shortname.replace(".py", "") not in N:
                load_anim(shortname.replace(".py", ""))
            else:
                os.remove(P(Animation.format(shortname)))
        except Exception as e:
            os.remove(P(Animation.format(shortname)))
            print(IS.format(shortname, e))


# for Gif
print(KIMOTOSHA)
Kim = glob.glob(Tsh)
for name in Kim:
    with open(name) as k:
        Kim1 = P(k.name)
        shortname = Kim1.stem
        try:
            if shortname.replace(".py", "") not in N:
                load_tosha(shortname.replace(".py", ""))
            else:
                os.remove(P(Tosh.format(shortname)))
        except Exception as e:
            os.remove(P(Tosh.format(shortname)))
            print(IS.format(shortname, e))


# for assistant
print(ASSISTANT)
Kim = glob.glob(Ast)
for name in Kim:
    with open(name) as k:
        Kim1 = P(k.name)
        shortname = Kim1.stem
        try:
            if shortname.replace(".py", "") not in N:
                load_assistant(shortname.replace(".py", ""))
            else:
                os.remove(P(Assistant.format(shortname)))
        except Exception as e:
            os.remove(P(Assistant.format(shortname)))
            print(IS.format(shortname, e))


print(ICSW)
print(Message.format(Name, TBOT))

bot.loop.create_task(startupmessage())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
