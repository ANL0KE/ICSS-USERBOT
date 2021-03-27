#    Icss - UserBot
#    Forr - songs


from . import *
import json
import os
import random
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.errors.rpcerrorlist import UserAlreadyParticipantError
from telethon.tl.types import InputMessagesFilterMusic as filtermus
from telethon.tl.types import DocumentAttributeAudio
from youtube_dl import YoutubeDL
from lyrics_extractor import SongLyrics as sl
from youtube_dl.utils import (
    ContentTooShortError,
    DownloadError,
    ExtractorError,
    GeoRestrictedError,
    MaxDownloadsReached,
    PostProcessingError,
    UnavailableVideoError,
    XAttrMetadataError,
)
from youtubesearchpython import SearchVideos


@icssbot.on(
    icss_cmd(
       pattern="اغنيه ?(.*)"
    )
)
async def download_video(ics):
    a = ics.text
    if a[5] == "s":
        return
    x = await eor(ics, "**⌔∮ جاري البحث**")
    url = ics.pattern_match.group(1)
    if not url:
        return await x.edit("**⌔∮ خطا**\nاكتب هكذا - `.اغنيه <اسم الاغنيه>`")
    search = SearchVideos(url, offset=1, mode="json", max_results=1)
    test = search.result()
    p = json.loads(test)
    q = p.get("search_result")
    try:
        url = q[0]["link"]
    except BaseException:
        return await x.edit("**⌔∮ لم اجد هذه الاغنيه **")
    type = "audio"
    await x.edit(f"**⌔∮ جاري تنزيل {url}...**")
    if type == "audio":
        opts = {
            "format": "bestaudio",
            "addmetadata": True,
            "key": "FFmpegMetadata",
            "writethumbnail": True,
            "prefer_ffmpeg": True,
            "nocheckcertificate": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "320",
                }
            ],
            "outtmpl": "%(id)s.mp3",
            "quiet": True,
            "logtostderr": False,
        }
    try:
        await x.edit("**⌔∮ جاري الحصول على المعلومات**")
        with YoutubeDL(opts) as rip:
            rip_data = rip.extract_info(url)
    except DownloadError as DE:
        await x.edit(f"⌔∮ {str(DE)}")
        return
    except ContentTooShortError:
        await x.edit("**⌔∮ ان محتوى التنزيل قصير جدا**")
        return
    except GeoRestrictedError:
        await x.edit(
            "`Video is not available from your geographic location due to" +
            " geographic restrictions imposed by a website.`"
        )
        return
    except MaxDownloadsReached:
        await x.edit("`Max-downloads limit has been reached.`")
        return
    except PostProcessingError:
        await x.edit("`There was an error during post processing.`")
        return
    except UnavailableVideoError:
        await x.edit("`Media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        return await x.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
    except ExtractorError:
        return await x.edit("`There was an error during info extraction.`")
    except Exception as e:
        return await x.edit(f"{str(type(e)): {str(e)}}")
    dir = os.listdir()
    if f"{rip_data['id']}.mp3.jpg" in dir:
        thumb = f"{rip_data['id']}.mp3.jpg"
    elif f"{rip_data['id']}.mp3.webp" in dir:
        thumb = f"{rip_data['id']}.mp3.webp"
    else:
        thumb = None
    upteload = """
Uploading...
Song name - {}
By - {}
""".format(
        rip_data["title"], rip_data["uploader"]
    )
    await x.edit(f"`{upteload}`")
    CAPT = f"**⌔∮ الاغنيه - {rip_data['title']}**\n**⌔∮ بواسطه - {rip_data['uploader']}**\n**⌔∮ للمستخدم -** {mention}\n"
    await ics.send_file(
        ics.chat_id,
        f"{rip_data['id']}.mp3",
        thumb=thumb,
        supports_streaming=True,
        caption=CAPT,
        attributes=[
            DocumentAttributeAudio(
                duration=int(rip_data["duration"]),
                title=str(rip_data["title"]),
                performer=str(rip_data["uploader"]),
            )
        ],
    )
    await x.delete()
    os.remove(f"{rip_data['id']}.mp3")
    try:
        os.remove(thumb)
    except BaseException:
        pass


