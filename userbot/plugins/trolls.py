import base64
import os

from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from . import convert_toimage, deEmojify, phcomment, threats, trap, trash


@icssbot.on(admin_cmd(pattern="threats$"))
@icssbot.on(sudo_cmd(pattern="threats$", allow_sudo=True))
async def icsbot(icsmem):
    if icsmem.fwd_from:
        return
    replied = await icsmem.get_reply_message()
    icsid = await reply_id(icsmem)
    if not replied:
        await edit_or_reply(icsmem, "reply to a supported media file")
        return
    output = await _icsstools.media_to_pic(icsmem, replied)
    kim = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    try:
        kim = Get(kim)
        await icsmem.client(kim)
    except BaseException:
        pass
    if size > 5242880:
        await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
        os.remove(download_location)
        return
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await output[0].edit(f"**Error: **\n`{str(exc)}`")
        os.remove(download_location)
        return
    ics = f"https://telegra.ph{response[0]}"
    ics = await threats(ics)
    await output[0].delete()
    await icsmem.client.send_file(icsmem.chat_id, ics, reply_to=icsid)


@icssbot.on(admin_cmd(pattern="trash$"))
@icssbot.on(sudo_cmd(pattern="trash$", allow_sudo=True))
async def icsbot(icsmem):
    if icsmem.fwd_from:
        return
    replied = await icsmem.get_reply_message()
    icsid = await reply_id(icsmem)
    if not replied:
        await edit_or_reply(icsmem, "reply to a supported media file")
        return
    output = await _icsstools.media_to_pic(icsmem, replied)
    lon = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    try:
        lon = Get(lon)
        await icsmem.client(lon)
    except BaseException:
        pass
    if size > 5242880:
        await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
        os.remove(download_location)
        return
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await output[0].edit(f"**Error: **\n`{str(exc)}`")
        os.remove(download_location)
        return
    ics = f"https://telegra.ph{response[0]}"
    ics = await trash(ics)
    await output[0].delete()
    await icsmem.client.send_file(icsmem.chat_id, ics, reply_to=icsid)


@icssbot.on(admin_cmd(pattern="trap(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="trap(?: |$)(.*)", allow_sudo=True))
async def icsbot(icsmem):
    if icsmem.fwd_from:
        return
    input_str = icsmem.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if ";" in input_str:
        text1, text2 = input_str.split(";")
    else:
        await edit_or_reply(
            icsmem,
            "**Syntax :** reply to image or sticker with `.trap (name of the person to trap);(trapper name)`",
        )
        return
    replied = await icsmem.get_reply_message()
    icsid = await reply_id(icsmem)
    if not replied:
        await edit_or_reply(icsmem, "reply to a supported media file")
        return
    output = await _icsstools.media_to_pic(icsmem, replied)
    kim = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    try:
        kim = Get(kim)
        await icsmem.client(kim)
    except BaseException:
        pass
    if size > 5242880:
        await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
        os.remove(download_location)
        return
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await output[0].edit(f"**Error: **\n`{str(exc)}`")
        os.remove(download_location)
        return
    ics = f"https://telegra.ph{response[0]}"
    ics = await trap(text1, text2, ics)
    await output[0].delete()
    await icsmem.client.send_file(icsmem.chat_id, ics, reply_to=icsid)


@icssbot.on(admin_cmd(pattern="phub(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="phub(?: |$)(.*)", allow_sudo=True))
async def icsbot(icsmem):
    if icsmem.fwd_from:
        return
    input_str = icsmem.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if ";" in input_str:
        username, text = input_str.split(";")
    else:
        await edit_or_reply(
            icsmem,
            "**Syntax :** reply to image or sticker with `.phub (username);(text in comment)`",
        )
        return
    replied = await icsmem.get_reply_message()
    icsid = await reply_id(icsmem)
    if not replied:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    output = await _cattools.media_to_pic(catmemes, replied)
    ik = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    download_location = convert_toimage(output[1])
    size = os.stat(download_location).st_size
    try:
        ik = Get(ik)
        await icsmem.client(ik)
    except BaseException:
        pass
    if size > 5242880:
        await output[0].edit(
            "the replied file size is not supported it must me below 5 mb"
        )
        os.remove(download_location)
        return
    await output[0].edit("generating image..")
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await output[0].edit(f"**Error: **\n`{str(exc)}`")
        os.remove(download_location)
        return
    ics = f"https://telegra.ph{response[0]}"
    ics = await phcomment(ics, text, username)
    await output[0].delete()
    await icsmem.client.send_file(icsmem.chat_id, ics, reply_to=icsid)


CMD_HELP.update(
    {
        "trolls": "**Plugin : **`trolls`\
      \n\n• **Syntax :** `.threats`\
      \n• **Function :** __Just a troll meme try yourself by replying cmd to image/sticker.__\
      \n\n• **Syntax :** `.trash`\
      \n• **Function :** __Just a troll meme try yourself by replying cmd to image/sticker.__\
      \n\n• **Syntax :** `.trap (name of the person to trap);(trapper name)`\
      \n• **Function :** __Just a troll meme try yourself by replying cmd to image/sticker. (trap card)__\
      \n\n• **Syntax :** `.phub (username);(text in comment)`\
      \n• **Function :** __Just a troll meme try yourself by replying cmd to image/sticker. (pornhub comment)__\
      "
    }
)
