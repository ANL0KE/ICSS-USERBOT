# for -<*>~ SOURCE ICSS ~<*>-
# edit By: @rruuurr

import asyncio
import os

from . import *


@icssbot.on(admin_cmd(pattern="tspam"))
async def icss(ics):
    tspam = str(ics.text[7:])
    message = tspam.replace(" ", "")
    for letter in message:
        await ics.respond(letter)
    await ics.delete()


@icssbot.on(admin_cmd(pattern="سبام"))
async def icss(ics):
    if not ics.text[0].isalpha() and ics.text[0] not in ("/", "#", "@", "!"):
        message = ics.text
        counter = int(message[6:8])
        spam_message = str(ics.text[8:])
        await asyncio.wait([ics.respond(spam_message) for i in range(counter)])
        await ics.delete()


@icssbot.on(admin_cmd(pattern="bigspam"))
async def icss(ics):
    if not ics.text[0].isalpha() and ics.text[0] not in ("/", "#", "@", "!"):
        message = ics.text
        counter = int(message[9:13])
        spam_message = str(ics.text[13:])
        for i in range(ics, counter):
            await ics.respond(spam_message)
        await ics.delete()


@icssbot.on(admin_cmd(pattern="picspam"))
async def tiny_pic_spam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        reply = await e.get_reply_message()
        message = e.text
        text = message.split()
        counter = int(text[1])
        media = await e.client.download_media(reply)
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, media)
        os.remove(media)
        await e.delete()


@icssbot.on(admin_cmd(pattern="delayspam ?(.*)"))
async def delayspammer(e):
    args = e.pattern_match.group(1)
    print(args)

    try:
        args = args.split(" ", 2)
        delay = float(args[0])
        count = int(args[1])
        msg = str(args[2])
    except BaseException:
        return await e.edit(
            f"**- الاستخدام :** {HNDLR}delayspam <delay time> <count> <msg>"
        )

    if not msg[0].isalpha() and msg[0] in ("/", "#", "@", "!"):
        return

    await e.delete()
    try:
        for i in range(count):
            await e.respond(msg)
            await asyncio.sleep(delay)
    except Exception as u:
        await e.respond(f"**Error :** `{u}`")
