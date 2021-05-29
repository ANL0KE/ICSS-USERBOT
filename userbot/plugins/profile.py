# profile code for -<*>- SOURCE ICSS -<*>- #
# =========================================#
# edit By: @rruuurr
# =========================================#

import os

from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl import functions
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest
from telethon.tl.functions.photos import DeletePhotosRequest, GetUserPhotosRequest
from telethon.tl.types import Channel, Chat, InputPhoto, User

from userbot import CMD_HELP
from userbot.utils import admin_cmd

# ====================== CONSTANT ===============================
INVALID_MEDIA = "```The extension of the media entity is invalid.```"
PP_CHANGED = "** ⪼ تم تغير صورة حسابك بنجاح 𓆰،**"
PP_TOO_SMOL = "** ⪼ هذه الصوره صغيره جدا قم بختيار صوره اخرى  𓆰،**"
PP_ERROR = "** ⪼ حدث خطا اثناء معالجه الصوره  𓆰،**"
BIO_SUCCESS = "** ⪼ تم تغير بايو حسابك بنجاح 𓆰،**"
NAME_OK = "** ⪼ تم تغير اسم حسابك بنجاح 𓆰،**"
USERNAME_SUCCESS = "**⪼ تم تغير معرف حسابك بنجاح 𓆰،**"
USERNAME_TAKEN = "** ⪼ هذا المعرف مستخدم  𓆰،**"
# ===============================================================


@icssbot.on(admin_cmd(pattern="بايو (.*)"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(about=bio)  # pylint:disable=E0602
        )
        await event.edit("**⪼ تم تغير بايو حسابك بنجاح 𓆰،**")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@icssbot.on(admin_cmd(pattern="اسم ((.|\n)*)"))  # pylint:disable=E0602,W0703
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "|" in names:
        first_name, last_name = names.split("|", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("**⪼ تم تغير اسم حسابك بنجاح 𓆰،**")
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))


@icssbot.on(admin_cmd(pattern="صوره"))  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("**⪼ جاري تنزيل صورة ملفي الشخصي  𓆰،**")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  # pylint:disable=E0602
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)  # pylint:disable=E0602
    photo = None
    try:
        photo = await event.client.download_media(  # pylint:disable=E0602
            reply_message, Config.TMP_DOWNLOAD_DIRECTORY  # pylint:disable=E0602
        )
    except Exception as e:  # pylint:disable=C0103,W0703
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("**⪼ جاري تحميل صورة ملفي الشخصي  𓆰،**")
            if photo.endswith((".mp4", ".MP4")):
                # https://t.me/tgbetachat/324694
                size = os.stat(photo).st_size
                if size > 2097152:
                    await event.edit("**⪼ يجب ان يكون الحجم اقل من 2 ميغا بايت 𓆰،**")
                    os.remove(photo)
                    return
                catpic = None
                catvideo = await event.client.upload_file(photo)
            else:
                catpic = await event.client.upload_file(photo)  # pylint:disable=E0602
                catvideo = None
            try:
                await event.client(
                    functions.photos.UploadProfilePhotoRequest(
                        file=catpic, video=catvideo, video_start_ts=0.01
                    )
                )
            except Exception as e:  # pylint:disable=C0103,W0703
                await event.edit(str(e))
            else:
                await event.edit("**⪼ تم تغير صورة حسابك بنجاح 𓆰،**")
    try:
        os.remove(photo)
    except Exception as e:  # pylint:disable=C0103,W0703
        logger.warn(str(e))  # pylint:


@icssbot.on(admin_cmd(outgoing=True, pattern="معرف (.*)"))
async def update_username(username):
    """ امر - معرف - لتغير معرف حسابك """
    newusername = username.pattern_match.group(1)
    try:
        await username.client(UpdateUsernameRequest(newusername))
        await username.edit(USERNAME_SUCCESS)
    except UsernameOccupiedError:
        await username.edit(USERNAME_TAKEN)


@icssbot.on(admin_cmd(outgoing=True, pattern="الحساب$"))
async def count(event):
    """ هذا امر الحساب - لعرض معلومات الحساب """
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("**⪼ جاري المعـالجه ༗.**")
    dialogs = await bot.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        currrent_entity = d.entity
        if isinstance(currrent_entity, User):
            if currrent_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(currrent_entity, Chat):
            g += 1
        elif isinstance(currrent_entity, Channel):
            if currrent_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)

    result += f"𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑷𝑹𝑶𝑭𝑰𝑳 𝑫𝑨𝑻𝑨 𓆪\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    result += f"**⌔∮ المستخدمون :**\t**{u}**\n"
    result += f"**⌔∮ المجموعات :**\t**{g}**\n"
    result += f"**⌔∮ المجموعات الخارقه :**\t**{c}**\n"
    result += f"**⌔∮ القنوات :**\t**{bc}**\n"
    result += f"**⌔∮ البوتات :**\t**{b}**\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"

    await event.edit(result)


@icssbot.on(admin_cmd(outgoing=True, pattern=r"مسح الصور"))
async def remove_profilepic(delpfp):
    """ امر حذف الصور - لحذ صوره واحد من حسابك او جميعها """
    group = delpfp.text[8:]
    if group == "الصور":
        lim = 0
    elif group.isdigit():
        lim = int(group)
    else:
        lim = 1
    pfplist = await delpfp.client(
        GetUserPhotosRequest(user_id=delpfp.sender_id, offset=0, max_id=0, limit=lim)
    )
    input_photos = [
        InputPhoto(
            id=sep.id,
            access_hash=sep.access_hash,
            file_reference=sep.file_reference,
        )
        for sep in pfplist.photos
    ]
    await delpfp.client(DeletePhotosRequest(id=input_photos))
    await delpfp.edit(f"**⪼ تم حذف ↩︎** {len(input_photos)} **من صور حسابك ༗.**")


@icssbot.on(admin_cmd(pattern="كروباتي$"))
async def _(event):
    if event.fwd_from:
        return
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = ""
    for channel_obj in result.chats:
        output_str += f"**⪼ كروبك ↩︎** {channel_obj.title} @{channel_obj.username} .\n"
    await event.edit(output_str)


CMD_HELP.update(
    {
        "profile": ".username <new_username>\
\nUsage: Changes your Telegram username.\
\n\n.pname <firstname> or .pname <firstname> <lastname>\
\nUsage: Changes your Telegram name.(First and last name will get split by the first space)\
\n\n.setpfp or .ppic\
\nUsage: Reply with .setpfp or .ppic to an image to change your Telegram profie picture.\
\n\n.pbio <new_bio>\
\nUsage: Changes your Telegram bio.\
\n\n.delpfp or .delpfp <number>/<all>\
\nUsage: Deletes your Telegram profile picture(s).\
\n\n.myusernames\
\nUsage: Shows usernames of your created channels and groups \
\n\n.count\
\nUsage: Counts your groups, chats, bots etc..."
    }
)
