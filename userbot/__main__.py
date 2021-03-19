# Icss - Userbot
# Owner - Kimo

import glob
from pathlib import Path
from sys import argv

import telethon.utils
from telethon import TelegramClient

from . import LOGS, bot
from .Config import Config
from .kimo import *
from .utils import load_module


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me()
    bot.uid = telethon.utils.get_peer_id(bot.me)


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Config.TG_BOT_USERNAME is not None:
        LOGS.info("⫷ بدء بوت اكسس ⫸")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
        ).start(bot_token=Config.TG_BOT_TOKEN)
        LOGS.info("⫷ انتهت التهيئة بدون أخطاء ⫸")
        LOGS.info("⫷ جاري بدء بوت اكسس ⫸")
        bot.loop.run_until_complete(add_bot(Config.TG_BOT_USERNAME))
        LOGS.info("⫷ اكتمل بدء التشغيل ⫸")
    else:
        bot.start()

path = "userbot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        if shortname.replace(".py", "") not in Config.NO_LOAD:
            load_module(shortname.replace(".py", ""))

LOGS.info("⫷ بوت اكسس يعمل بنجاح ⫸")
LOGS.info(
    "⫷ مبروك عزيزي اكتب الان .ايدي لترى ما اذا كان البوت يعمل ⫸\
    \n ⫷ إذا كنت بحاجة إلى مساعدة ، فتوجه إلى مطور السورس @rruuurr ⫸"
)


async def startupmessage():
    try:
        if Config.PRIVATE_GROUP_BOT_API_ID:
            await bot.send_message(
                Config.PRIVATE_GROUP_BOT_API_ID,
                f"**⌔∮ تم تحديث سورس اكسس 𓄂 **\n"
                f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 \n"
                f"⩫ اكتب .بنك لتحقق اذا ما كان البوت يعمل \n"
                f"**⩫ المستخدم : **{icsme} \n"
                f"**⩫ بوت المستخدم :** {ICSBOT} \n"
                f"**⩫ للمساعده :** {DEV}\n"
                f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻",
                link_preview=False,
            )
    except Exception as e:
        LOGS.info(str(e))


bot.loop.create_task(startupmessage())

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
