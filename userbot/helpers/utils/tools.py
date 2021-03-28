import os
from typing import Optional

from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from PIL import Image

from ...tosh import ed, eor
from ..tools import media_type
from .utils import runcmd


async def media_to_pic(event, reply):
    mediatype = media_type(reply)
    if mediatype not in ["Photo", "Round Video", "Gif", "Sticker", "Video"]:
        await ed(
            event,
            "`In the replied message. I cant extract any image to procced further reply to proper media`",
        )
        return None
    icssmedia = await reply.download_media(file="./temp")
    icssevent = await eor(event, f"`Transfiguration Time! Converting....`")
    icssfile = os.path.join("./temp/", "meme.png")
    if mediatype == "Sticker":
        if icssmedia.endswith(".tgs"):
            await runcmd(
                f"lottie_convert.py --frame 0 -if lottie -of png '{icssmedia}' '{icssfile}'"
            )
        elif icssmedia.endswith(".webp"):
            im = Image.open(icssmedia)
            im.save(icssfile)
    elif mediatype in ["Round Video", "Video", "Gif"]:
        extractMetadata(createParser(icssmedia))
        await runcmd(f"rm -rf '{icssfile}'")
        await take_screen_shot(icssmedia, 0, icssfile)
        if not os.path.exists(icssfile):
            await edit_delete(
                icssevent, f"`Sorry. I can't extract a image from this {mediatype}`"
            )
            return None
    else:
        im = Image.open(icssmedia)
        im.save(icssfile)
    await runcmd(f"rm -rf '{icssmedia}'")
    return [icssevent, icssfile, mediatype]


async def take_screen_shot(
    video_file: str, duration: int, path: str = ""
) -> Optional[str]:
    thumb_image_path = path or os.path.join(
        "./temp/", f"{os.path.basename(video_file)}.jpg"
    )
    command = f"ffmpeg -ss {duration} -i '{video_file}' -vframes 1 '{thumb_image_path}'"
    err = (await runcmd(command))[1]
    if err:
        print(err)
    return thumb_image_path if os.path.exists(thumb_image_path) else None
