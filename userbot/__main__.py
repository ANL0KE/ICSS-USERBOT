#  Icss - Userbot
#  Owner - Kimo

import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient

from userbot.kimo import *
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
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if TBOT is not None:
            print("⫷ يتم تحميل انلاين اكسس ⫸")
            bot.tgbot = TelegramClient(Xtbot, api_id=Xapid, api_hash=Xhash).start(bot_token=Xtoke)
            print("⫷ اكتمل تنزيل انلاين اكسس بدون اخطاء ⫸")
            print("⫷ يتم بدء بوت اكسس ⫸")
            bot.loop.run_until_complete(add_bot(TBOT))
            print("⫷ اكتمل بدء بوت اكسس ⫸")
        else:
            bot.start()
    except Exception as e:
        LOGS.error("{} -".format(Xt) + f"{str(e)}")
        sys.exit()


# For all plugins
path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                load_module(shortname.replace(".py", ""))
            else:
                os.remove(Path(f"userbot/plugins/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"userbot/plugins/{shortname}.py"))
            print(f"⫷ لايمكن تحميل - {shortname} بسبب {e} ⫸")


# For admin tools
print(ADMIN)
path = "userbot/plugins/Admin/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                load_admin(shortname.replace(".py", ""))
            else:
                os.remove(Path(f"userbot/plugins/Admin/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"userbot/plugins/Admin/{shortname}.py"))
            print(f"⫷ لايمكن تحميل - {shortname} بسبب {e} ⫸")


# for animations
print(ANIMATIONS)
path = "userbot/plugins/animations/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                load_anim(shortname.replace(".py", ""))
            else:
                os.remove(Path(f"userbot/plugins/animations/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"userbot/plugins/animations/{shortname}.py"))
            print(f"⫷ لايمكن تحميل - {shortname} بسبب {e} ⫸")


# for Gif
print(KIMOTOSHA)
path = "userbot/plugins/tosha/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                load_tosha(shortname.replace(".py", ""))
            else:
                os.remove(Path(f"userbot/plugins/tosha/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"userbot/plugins/tosha/{shortname}.py"))
            print(f"⫷ لايمكن تحميل - {shortname} بسبب {e} ⫸")


# for assistant
print(ASSISTANT)
path = "userbot/plugins/assistant/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        try:
            if shortname.replace(".py", "") not in Config.NO_LOAD:
                load_assistant(shortname.replace(".py", ""))
            else:
                os.remove(Path(f"userbot/plugins/assistant/{shortname}.py"))
        except Exception as e:
            os.remove(Path(f"userbot/plugins/assistant/{shortname}.py"))
            print(f"⫷ لايمكن تحميل - {shortname} بسبب {e} ⫸")


print(ICSW)
print("⫷ بوت اكسس يعمل بنجاح الان ⫸")
print(Masg.format(ALIVE_NAME, TBOT))
print("\n⫷ @rruuurr - اذا كنت بحاجه الى مساعده فتوجه الى ⫸")

bot.loop.create_task(startupmessage())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
