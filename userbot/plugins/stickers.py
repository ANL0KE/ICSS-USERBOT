# edit by @rruuurr for icss

import asyncio
import base64
import io
import math
import random
import urllib.request
from os import remove

import emoji as icssemoji
from PIL import Image
from telethon.tl import functions, types
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl.types import (
    DocumentAttributeFilename,
    DocumentAttributeSticker,
    InputStickerSetID,
    MessageMediaPhoto,
)

combot_stickers_url = "https://combot.org/telegram/stickers?q="

EMOJI_SEN = [
    "Можно отправить несколько смайлов в одном сообщении, однако мы рекомендуем использовать не больше одного или двух на каждый стикер.",
    "You can list several emoji in one message, but I recommend using no more than two per sticker",
    "Du kannst auch mehrere Emoji eingeben, ich empfehle dir aber nicht mehr als zwei pro Sticker zu benutzen.",
]

KANGING_STR = "⪼ جاري صنع الملصق  "


def verify_cond(catarray, text):
    return any(i in text for i in catarray)


def pack_name(userid, pack, is_anim):
    if is_anim:
        return f"Icss_{userid}_{pack}_anim"
    return f"Icss_{userid}_{pack}"


def char_is_emoji(character):
    return character in icssemoji.UNICODE_EMOJI


def pack_nick(username, pack, is_anim):
    if Config.CUSTOM_STICKER_PACKNAME:
        if is_anim:
            packnick = f"{Config.CUSTOM_STICKER_PACKNAME} Vol.{pack} (Animated)"
        else:
            packnick = f"{Config.CUSTOM_STICKER_PACKNAME} Vol.{pack}"
    else:
        if is_anim:
            packnick = f"@{username} Vol.{pack} (Animated)"
        else:
            packnick = f"@{username} Vol.{pack}"
    return packnick


async def resize_photo(photo):
    """ Resize the given photo to 512x512 """
    image = Image.open(photo)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        maxsize = (512, 512)
        image.thumbnail(maxsize)
    return image


async def newpacksticker(
    icssevent,
    conv,
    cmd,
    args,
    pack,
    packnick,
    stfile,
    emoji,
    packname,
    is_anim,
    otherpack=False,
    pkang=False,
):
    await conv.send_message(cmd)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packnick)
    await conv.get_response()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    await args.client.send_read_acknowledge(conv.chat_id)
    if is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        remove("AnimatedSticker.tgs")
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
    rsp = await conv.get_response()
    if not verify_cond(EMOJI_SEN, rsp.text):
        await icssevent.edit(
            f"⌔∮ فشل اضافه الملصق, استخدم @Stickers لاضافه الملصق .\n**⌔∮ الخطأ :**{rsp}"
        )
        return
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/publish")
    if is_anim:
        await conv.get_response()
        await conv.send_message(f"<{packnick}>")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message("/skip")
    try:
        ics = Get(ics)
        await icssevent.client(ics)
    except BaseException:
        pass
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message(packname)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return otherpack, packname, emoji
    else:
        return pack, packname


async def add_to_pack(
    icssevent,
    conv,
    args,
    packname,
    pack,
    userid,
    username,
    is_anim,
    stfile,
    emoji,
    cmd,
    pkang=False,
):
    await conv.send_message("/addsticker")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.send_message(packname)
    x = await conv.get_response()
    while ("50" in x.text) or ("120" in x.text):
        try:
            val = int(pack)
            pack = val + 1
        except ValueError:
            pack = 1
        packname = pack_name(userid, pack, is_anim)
        packnick = pack_nick(username, pack, is_anim)
        await icssevent.edit(f"⌔∮ تبديل الى الحزمه {str(pack)} بسبب امتلاء الحزمه. ")
        await conv.send_message(packname)
        x = await conv.get_response()
        if x.text == "⌔∮ الحزمه المحدده غير صالحه. ":
            return await newpacksticker(
                icssevent,
                conv,
                cmd,
                args,
                pack,
                packnick,
                stfile,
                emoji,
                packname,
                is_anim,
                otherpack=True,
                pkang=pkang,
            )
    if is_anim:
        await conv.send_file("AnimatedSticker.tgs")
        remove("AnimatedSticker.tgs")
    else:
        stfile.seek(0)
        await conv.send_file(stfile, force_document=True)
    rsp = await conv.get_response()
    if not verify_cond(EMOJI_SEN, rsp.text):
        await icssevent.edit(
            f"⌔∮ فشل اضافه الملصق, استخدم @Stickers لاضافه الملصق .\n**⌔∮ الخطأ :**{rsp}"
        )
        return
    await conv.send_message(emoji)
    await args.client.send_read_acknowledge(conv.chat_id)
    await conv.get_response()
    await conv.send_message("/done")
    await conv.get_response()
    await args.client.send_read_acknowledge(conv.chat_id)
    if not pkang:
        return packname, emoji
    else:
        return pack, packname


@icssbot.on(admin_cmd(outgoing=True, pattern="ملصق ?(.*)"))
@icssbot.on(sudo_cmd(pattern="ملصق ?(.*)", allow_sudo=True))
async def kang(args):
    photo = None
    emojibypass = False
    is_anim = False
    emoji = None
    message = await args.get_reply_message()
    user = await args.client.get_me()
    if not user.username:
        try:
            user.first_name.encode("utf-8").decode("ascii")
            username = user.first_name
        except UnicodeDecodeError:
            username = f"cat_{user.id}"
    else:
        username = user.username
    userid = user.id
    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            icssevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            photo = await args.client.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split("/"):
            icssevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            await args.client.download_file(message.media.document, photo)
            if (
                DocumentAttributeFilename(file_name="sticker.webp")
                in message.media.document.attributes
            ):
                emoji = message.media.document.attributes[1].alt
                emojibypass = True
        elif "tgsticker" in message.media.document.mime_type:
            icssevent = await edit_or_reply(args, f"`{random.choice(KANGING_STR)}`")
            await args.client.download_file(
                message.media.document, "AnimatedSticker.tgs"
            )

            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt
            emojibypass = True
            is_anim = True
            photo = 1
        else:
            await edit_delete(args, "⪼ ملف غير مدعم")
            return
    else:
        await edit_delete(args, "⪼ لايوجد ملصق او صوره لصنعه... ")
        return
    if photo:
        splat = ("".join(args.text.split(maxsplit=1)[1:])).split()
        emoji = emoji if emojibypass else "😹"
        pack = 1
        if len(splat) == 2:
            if char_is_emoji(splat[0][0]):
                if char_is_emoji(splat[1][0]):
                    return await catevent.edit("↮")
                pack = splat[1]  # User sent both
                emoji = splat[0]
            elif char_is_emoji(splat[1][0]):
                pack = splat[0]  # User sent both
                emoji = splat[1]
            else:
                return await icssevent.edit("↮")
        elif len(splat) == 1:
            if char_is_emoji(splat[0][0]):
                emoji = splat[0]
            else:
                pack = splat[0]
        packnick = pack_nick(username, pack, is_anim)
        packname = pack_name(userid, pack, is_anim)
        cmd = "/newpack"
        stfile = io.BytesIO()
        if is_anim:
            cmd = "/newanimated"
        else:
            image = await resize_photo(photo)
            stfile.name = "sticker.png"
            image.save(stfile, "PNG")
        response = urllib.request.urlopen(
            urllib.request.Request(f"http://t.me/addstickers/{packname}")
        )
        htmlstr = response.read().decode("utf8").split("\n")
        if (
            "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."
            not in htmlstr
        ):
            async with args.client.conversation("Stickers") as conv:
                packname, emoji = await add_to_pack(
                    icssevent,
                    conv,
                    args,
                    packname,
                    pack,
                    userid,
                    username,
                    is_anim,
                    stfile,
                    emoji,
                    cmd,
                )
            await edit_delete(
                icssevent,
                f"`⪼ تم صنع الملصق بنجاح \
                    \n⪼ لأضافه الملصق` [اضغط هنا](t.me/addstickers/{packname}) ` استخدم ↫  {emoji}` للعثور على الملصقات المصنوعه",
                parse_mode="md",
                time=10,
            )
        else:
            await icssevent.edit("** ⪼ جاري صنع حزمه...**")
            async with args.client.conversation("Stickers") as conv:
                otherpack, packname, emoji = await newpacksticker(
                    icssevent,
                    conv,
                    cmd,
                    args,
                    pack,
                    packnick,
                    stfile,
                    emoji,
                    packname,
                    is_anim,
                )
            if otherpack:
                await edit_delete(
                    icssevent,
                    f"`⪼ تم صنع الملصق لحزمه مختلفه !\
                    \n⪼ والحزمة التي تم إنشاؤها حديثًا هي` [اضغط هنا](t.me/addstickers/{packname}) `  استخدم↫  {emoji}` للعثور على الملصقات المصنوعه ",
                    parse_mode="md",
                    time=10,
                )
            else:
                await edit_delete(
                    icssevent,
                    f"`⪼ تم صنع الملصق بنجاح\
                    \n⪼ تم صنع الملصق بنجاح الحزمه ` [هنا](t.me/addstickers/{packname}) ` سمايل الملصق هو {emoji}`",
                    parse_mode="md",
                    time=10,
                )


@icssbot.on(admin_cmd(pattern="حزمه ?(.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="حزمه ?(.*)", allow_sudo=True))
async def pack_kang(event):
    if event.fwd_from:
        return
    user = await event.client.get_me()
    if user.username:
        username = user.username
    else:
        try:
            user.first_name.encode("utf-8").decode("ascii")
            username = user.first_name
        except UnicodeDecodeError:
            username = f"cat_{user.id}"
    photo = None
    userid = user.id
    is_anim = False
    emoji = None
    reply = await event.get_reply_message()
    cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
    if not reply or media_type(reply) is None or media_type(reply) != "Sticker":
        return await edit_delete(
            event, "** ⪼ الرد على أي ملصق لإرسال جميع الملصقات في تلك الحزمة**"
        )
    try:
        stickerset_attr = reply.document.attributes[1]
        icssevent = await edit_or_reply(
            event, "** ⪼ إحضار تفاصيل حزمة الملصقات ، برجاء الانتظار**"
        )
    except BaseException:
        return await edit_delete(event, "**هذا ليس ملصقًا. الرد على ملصق**", 5)
    try:
        get_stickerset = await event.client(
            GetStickerSetRequest(
                InputStickerSetID(
                    id=stickerset_attr.stickerset.id,
                    access_hash=stickerset_attr.stickerset.access_hash,
                )
            )
        )
    except:
        return await edit_delete(
            icssevent,
            "⪼ أعتقد أن هذا الملصق ليس جزءًا من أي حزمة. لذا ، لا أستطيع أن احول هذا الملصق الى حزمتي",
        )
    kangst = 1
    reqd_sticker_set = await event.client(
        functions.messages.GetStickerSetRequest(
            stickerset=types.InputStickerSetShortName(
                short_name=f"{get_stickerset.set.short_name}"
            )
        )
    )
    noofst = get_stickerset.set.count
    blablapacks = []
    blablapacknames = []
    pack = None
    for message in reqd_sticker_set.documents:
        if "image" in message.mime_type.split("/"):
            await edit_or_reply(
                icssevent,
                f"**جاري استنساخ حزمه الملصقات ↫ العدد : {kangst}/{noofst}**",
            )
            photo = io.BytesIO()
            await event.client.download_file(message, photo)
            if (
                DocumentAttributeFilename(file_name="sticker.webp")
                in message.attributes
            ):
                emoji = message.attributes[1].alt
        elif "tgsticker" in message.mime_type:
            await edit_or_reply(
                icssevent,
                f"⪼ **جاري استنساخ حزمه الملصقات ↫ العدد : {kangst}/{noofst} 𓆰.**",
            )
            await event.client.download_file(message, "AnimatedSticker.tgs")
            attributes = message.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt
            is_anim = True
            photo = 1
        else:
            await edit_delete(catevent, "`Unsupported File!`")
            return
        if photo:
            splat = ("".join(event.text.split(maxsplit=1)[1:])).split()
            emoji = emoji or "😹"
            if pack is None:
                pack = 1
                if len(splat) == 1:
                    pack = splat[0]
                elif len(splat) > 1:
                    return await edit_delete(
                        icssevent,
                        "** ⪼ عذرًا ، لا يمكن استخدام الاسم المعطى للحزمة أو لا توجد حزمة بهذا الاسم**",
                    )
            try:
                ics = Get(ics)
                await event.client(ics)
            except BaseException:
                pass
            packnick = pack_nick(username, pack, is_anim)
            packname = pack_name(userid, pack, is_anim)
            cmd = "/newpack"
            stfile = io.BytesIO()
            if is_anim:
                cmd = "/newanimated"
            else:
                image = await resize_photo(photo)
                stfile.name = "sticker.png"
                image.save(stfile, "PNG")
            response = urllib.request.urlopen(
                urllib.request.Request(f"http://t.me/addstickers/{packname}")
            )
            htmlstr = response.read().decode("utf8").split("\n")
            if (
                "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>."
                in htmlstr
            ):
                async with event.client.conversation("Stickers") as conv:
                    pack, icspackname = await newpacksticker(
                        icssevent,
                        conv,
                        cmd,
                        event,
                        pack,
                        packnick,
                        stfile,
                        emoji,
                        packname,
                        is_anim,
                        pkang=True,
                    )
            else:
                async with event.client.conversation("Stickers") as conv:
                    pack, icspackname = await add_to_pack(
                        icssevent,
                        conv,
                        event,
                        packname,
                        pack,
                        userid,
                        username,
                        is_anim,
                        stfile,
                        emoji,
                        cmd,
                        pkang=True,
                    )
            if icspackname not in blablapacks:
                blablapacks.append(icspackname)
                blablapacknames.append(pack)
        kangst += 1
        await asyncio.sleep(2)
    result = "`This sticker pack is kanged into the following your sticker pack(s):`\n"
    for i in range(len(blablapacks)):
        result += f"  •  [pack {blablapacknames[i]}](t.me/addstickers/{blablapacks[i]})"
    await icssevent.edit(result)


@icssbot.on(admin_cmd(pattern="معلومات الملصق$", outgoing=True))
@icssbot.on(sudo_cmd(pattern="معلومات الملصق$", allow_sudo=True))
async def get_pack_info(event):
    if not event.is_reply:
        await edit_delete(
            event, "**لا أستطيع إحضار المعلومات من لا شيء ، هل يمكنني ذلك ؟!**", 5
        )
        return
    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        await edit_delete(event, "**قم بالرد على الملصق للحصول على تفاصيل الحزمة**", 5)
        return
    try:
        stickerset_attr = rep_msg.document.attributes[1]
        icssevent = await edit_or_reply(
            event, "**جارٍ إحضار تفاصيل حزمة الملصقات ، يُرجى الانتظار ..**"
        )
    except BaseException:
        await edit_delete(event, "**هذا ليس ملصقًا. الرد على ملصق.**", 5)
        return
    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        await catevent.edit("**هذا ليس ملصقًا. الرد على ملصق.**")
        return
    get_stickerset = await event.client(
        GetStickerSetRequest(
            InputStickerSetID(
                id=stickerset_attr.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash,
            )
        )
    )
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)
    OUTPUT = (
        f"𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑺𝑻𝑰𝑪𝑲𝑹𝑺 𝑰𝑵𝑭𝑶 𓆪\n"
        f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        f"⪼ **عنوان الملصق:** {get_stickerset.set.title}\n"
        f"⪼ **الاسم المختصر للملصق:** {get_stickerset.set.short_name}\n"
        #       f"**المسؤول:** {get_stickerset.set.official}\n"
        #       f"**المؤرشف:** {get_stickerset.set.archived}\n"
        f"⪼ **عدد الملصقات:** {get_stickerset.set.count}\n"
        f"⪼ **السمايلات المستخدمه:**\n{' '.join(pack_emojis)}"
    )
    await icssevent.edit(OUTPUT)


CMD_HELP.update(
    {
        "stickers": "**Plugins : **`stickers`\
\n\n**  •  Syntax : **`.kang [emoji('s)] [number]`\
\n**  •  Function : **__Kang's the sticker/image to the specified pack and uses the emoji('s) you picked.__\
\n\n**  •  Syntax : **`.pkang [number]`\
\n**  •  Function : **__Kang's the entire sticker pack of replied sticker to the specified pack __\
\n\n**  •  Syntax : **`.stickers name`\
\n**  •  Function : **__shows you the list of non-animated sticker packs with that name.__\
\n\n**  •  Syntax : **`.stkrinfo`\
\n**  •  Function : **__Gets info about the sticker pack.__"
    }
)
