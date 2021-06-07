# for plugins:
from resources.Formation.plugins import *
from userbot import bot
from userbot.tosh import *

# For format M:
O = bot.me.id
Name = bot.me.first_name
M = "[{}](tg://user?id={})".format(Name, O)


# for Calc text - HelpText & Quotly text
from userbot.tosh import (
    Calc,
    C,
    HelpString,
    Quotly,
    Echo
)

# for purge me
from asyncio sleep

async def p_me(e):
    message = e.text
    count = int(message[9:])
    i = 1

    async for message in e.client.iter_messages(e.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()
    smsg = await e.client.send_message(e.chat_id, "**⌔∮ اهلا {} تم حذف** + `str(count)` + **رساله بنجاح**".format(M))
    await sleep(5)
    await smsg.delete()

