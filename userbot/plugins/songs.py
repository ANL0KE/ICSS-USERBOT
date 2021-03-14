"""
Edit by: @rruuurr ( https://t.me/rruuurr  )
"""
# songs finder for Icss

import asyncio
import base64
import os
from pathlib import Path

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from . import name_dl, song_dl, video_dl, yt_search

# =========================================================== #
#                           STRINGS                           #
# =========================================================== #
SONG_SEARCH_STRING = "<code>wi8..! I am finding your song....</code>"
SONG_NOT_FOUND = "<code>Sorry !I am unable to find any song like that</code>"
SONG_SENDING_STRING = "<code>yeah..! i found something wi8..🥰...</code>"
SONGBOT_BLOCKED_STRING = "<code>Please unblock @songdl_bot and try again</code>"
# =========================================================== #
#                                                             #
# =========================================================== #


@icssbot.on(admin_cmd(pattern="(بحث|song320)($| (.*))"))
@icssbot.on(sudo_cmd(pattern="(بحث|song320)($| (.*))", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(2):
        query = event.pattern_match.group(2)
    elif reply:
        if reply.message:
            query = reply.message
    else:
        await edit_or_reply(event, "`What I am Supposed to find `")
        return
    ics = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    icsevent = await edit_or_reply(event, "**⪼ جاري البحث عن الاغنـيه 🖤🎧 ،**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await cevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    cmd = event.pattern_match.group(1)
    if cmd == "بحث":
        q = "128k"
    elif cmd == "song320":
        q = "320k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        ics = Get(ics)
        await event.client(ics)
    except BaseException:
        pass
    stderr = (await _catutils.runcmd(song_cmd))[1]
    if stderr:
        return await icsevent.edit(f"**⌔∮ خطأ :** `{stderr}`.")
    icsname, stderr = (await _icssutils.runcmd(name_cmd))[:2]
    if stderr:
        return await icsevent.edit(f"**⌔∮ خطأ :** `{stderr}`.")
    # stderr = (await runcmd(thumb_cmd))[1]
    icsname = os.path.splitext(icsname)[0]
    # if stderr:
    #    return await icsevent.edit(f"**⌔∮ خطأ :** `{stderr}`.")
    song_file = Path(f"{icsname}.mp3")
    if not os.path.exists(song_file):
        return await icsevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await icsevent.edit("** ⪼ جاري تحميل الاغنيه انتظر قليلا🖤🎧 .**")
    icsthumb = Path(f"{icsname}.jpg")
    if not os.path.exists(icsthumb):
        icsthumb = Path(f"{icsname}.webp")
    elif not os.path.exists(icsthumb):
        icsthumb = None

    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=query,
        thumb=icsthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await catevent.delete()
    for files in (icsthumb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)


@icssbot.on(admin_cmd(pattern="يوتيوب( (.*)|$)"))
@icssbot.on(sudo_cmd(pattern="يوتيوب( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        if reply.message:
            query = reply.messag
    else:
        event = await edit_or_reply(event, "What I am Supposed to find")
        return
    ics = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    icsevent = await edit_or_reply(event, "**⪼ جاري البحث عن الاغنـيه 🖤🎧 ،**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await icsevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    stderr = (await _icssutils.runcmd(video_cmd))[1]
    if stderr:
        return await icsevent.edit(f"**⌔∮ خطأ :** `{stderr}`.")
    icsname, stderr = (await _icssutils.runcmd(name_cmd))[:2]
    if stderr:
        return await icsevent.edit(f"**⌔∮ خطأ :** `{stderr}`.")
    # stderr = (await runcmd(thumb_cmd))[1]
    try:
        kim = Get(kim)
        await event.client(kim)
    except BaseException:
        pass
    # if stderr:
    #    return await catevent.edit(f"**Error :** `{stderr}`")
    icsname = os.path.splitext(icsname)[0]
    vsong_file = Path(f"{icsname}.mp4")
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{icsname}.mkv")
    elif not os.path.exists(vsong_file):
        return await icsevent.edit(
            f"Sorry!. I can't find any related video/audio for `{query}`"
        )
    await icsevent.edit("** ⪼ جاري تحميل الاغنيه انتظر قليلا🖤🎧 .**")
    Path(f"{icsname}.jpg")
    if not os.path.exists(icsthumb):
        icsthumb = Path(f"{icsname}.webp")
    elif not os.path.exists(icsthumb):
        icsthumb = None
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        force_document=False,
        caption=query,
        thumb=icsthumb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await icsevent.delete()
    for files in (icsthumb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@icssbot.on(admin_cmd(pattern="song2 (.*)"))
@icssbot.on(sudo_cmd(pattern="song2 (.*)", allow_sudo=True))
async def icss_song_fetcer(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    icsevent = await edit_or_reply(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(song)
            tsh = await conv.get_response()
            while tsh.edit_hide != True:
                await asyncio.sleep(0.1)
                tsh = await event.client.get_messages(chat, ids=tshid)
            baka = await event.client.get_messages(chat)
            if baka[0].message.startswith(
                ("I don't like to say this but I failed to find any such song.")
            ):
                await delete_messages(event, chat, purgeflag)
                return await edit_delete(
                    icsevent, SONG_NOT_FOUND, parse_mode="html", time=5
                )
            await icsevent.edit(SONG_SENDING_STRING, parse_mode="html")
            await baka[0].click(0)
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icsevent.edit(SONGBOT_BLOCKED_STRING, parse_mode="html")
            return
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"<b>➥ Song :- <code>{song}</code></b>",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await icsevent.delete()
        await delete_messages(event, chat, purgeflag)


CMD_HELP.update(
    {
        "songs": "**Plugin : **`songs`\
        \n\n  •**Syntax : **`.song <query/reply>`\
        \n  •**Function : **__searches the song you entered in query from youtube and sends it, quality of it is 128k__\
        \n\n  •**Syntax : **`.song320 <query/reply>`\
        \n  •**Function : **__searches the song you entered in query from youtube and sends it quality of it is 320k__\
        \n\n  •**Syntax : **`.vsong <query/reply>`\
        \n  •**Function : **__Searches the video song you entered in query and sends it__\
        \n\n  •**Syntax : **`.song2 query`\
        \n  •**Function : **__searches the song you entered in query and sends it quality of it is 320k__\
        "
    }
)
