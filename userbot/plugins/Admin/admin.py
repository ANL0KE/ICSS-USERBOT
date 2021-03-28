#     Icss - Userbot
#     edit - @rruuurr

# ====================================================== #

from asyncio import sleep

from telethon import functions
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import (
    UserAdminInvalidError, 
    UserIdInvalidError, 
)
from telethon.tl.functions.channels import (
    EditAdminRequest,
    EditBannedRequest,
    EditPhotoRequest,
)
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChatAdminRights, 
    ChatBannedRights, 
    MessageMediaPhoto, 
)

from ...utils import errors_handler
from .. import (
    BOTLOG, 
    BOTLOG_CHATID, 
    LOGS, get_user_from_event, 
)
from ..sql_helper.mute_sql import (
    is_muted,
    mute,
    unmute, 
)
# ====================================================== #
#                     OWNER - ANL0KE
# ====================================================== #

PP_TOO_SMOL = "⪼ **الصورة صغيرة جدًا** 𓆰."
PP_ERROR = "⪼ **فشل أثناء معالجة الصورة** 𓆰."
NO_ADMIN = "⪼ **أنا لست مشرف هنا!!** 𓆰."
NO_PERM = "⪼ **ليس لدي أذونات كافية!** 𓆰."
CHAT_PP_CHANGED = "⪼ **تغيرت صورة الدردشة** 𓆰."
INVALID_MEDIA = "⪼ **ملحق غير صالح** 𓆰."

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)

MUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=True)
UNMUTE_RIGHTS = ChatBannedRights(until_date=None, send_messages=False)

# ====================================================== #


@icssbot.on(icss_cmd(pattern="ضع صوره$"))
@icssbot.on(sudo_cmd(pattern="ضع صوره$", allow_sudo=True))
async def set_group_photo(gpic):
    if gpic.fwd_from:
        return
    if not gpic.is_group:
        await eor(
            gpic,
            "** ⪼ لا اعتقد ان ۿذه مجمـوعه 𓆰،**\n ⫷ [𝙎𝙊𝙐𝙍𝘾𝞝  𝙞𝘾𝙎𝙎 ](t.me/rruuurr) ⫸",
        )
        return
    replymsg = await gpic.get_reply_message()
    await gpic.get_chat()
    photo = None
    if replymsg and replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await gpic.client.download_media(message=replymsg.photo)
        elif "image" in replymsg.media.document.mime_type.split("/"):
            photo = await gpic.client.download_file(replymsg.media.document)
        else:
            await eor(gpic, INVALID_MEDIA)
    kimo = None
    if photo:
        try:
            await gpic.client(
                EditPhotoRequest(gpic.chat_id, await gpic.client.upload_file(photo))
            )
            await eor(gpic, CHAT_PP_CHANGED)
            kimo = True
        except PhotoCropSizeSmallError:
            await eor(gpic, PP_TOO_SMOL)
        except ImageProcessFailedError:
            await eor(gpic, PP_ERROR)
        except Exception as e:
            await eor(gpic, f"**خطأ : **`{str(e)}`")
        if BOTLOG and kimo:
            await gpic.client.send_message(
                BOTLOG_CHATID,
                "#صوره_المجموعه\n"
                f"تغير صوره المجموعه "
                f"الدردشه: {gpic.chat.title}(`{gpic.chat_id}`)",
            )


# ====================================================== #


@icssbot.on(icss_cmd(pattern="رفع مشرف(?: |$)(.*)", command="promote"))
@icssbot.on(sudo_cmd(pattern="رفع مشرف(?: |$)(.*)", command="promote", allow_sudo=True))
async def promote(promt):
    if promt.fwd_from:
        return
    chat = await promt.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(promt, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=False,
        invite_users=True,
        change_info=False,
        ban_users=False,
        delete_messages=True,
        pin_messages=True,
    )
    icse = await eor(promt, "**╮ ❐  جـاري ࢪفعه مشرف  ❏╰**")
    user, rank = await get_user_from_event(promt)
    if not rank:
        rank = "مشرف"
    if not user:
        return
    try:
        await promt.client(EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await icse.edit("**- ❝ ⌊  تم تـرقيتـه مشـرف 𓆰.**")
    except BadRequestError:
        await icse.edit(NO_PERM)
        return
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID,
            "#مشرف\n"
            f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
            f"الدردشه: {promt.chat.title}(`{promt.chat_id}`)",
        )


# ====================================================== #


@icssbot.on(icss_cmd(pattern="رفع مالك(?: |$)(.*)", command="promote"))
@icssbot.on(sudo_cmd(pattern="رفع مالك(?: |$)(.*)", command="promote", allow_sudo=True))
async def promote(promt):
    if promt.fwd_from:
        return
    chat = await promt.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(promt, NO_ADMIN)
        return
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
    )
    icse = await eor(promt, "**╮ ❐  جـاري ࢪفعه مالك  ❏╰**")
    user, rank = await get_user_from_event(promt)
    if not rank:
        rank = "مالك"
    if not user:
        return
    try:
        await promt.client(EditAdminRequest(promt.chat_id, user.id, new_rights, rank))
        await icse.edit("**- ❝ ⌊  تم تـرقيتـه مالك 𓆰.**")
    except BadRequestError:
        await icse.edit(NO_PERM)
        return
    if BOTLOG:
        await promt.client.send_message(
            BOTLOG_CHATID,
            "#مالك\n"
            f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
            f"الدردشه: {promt.chat.title}(`{promt.chat_id}`)",
        )


# ====================================================== #


@icssbot.on(icss_cmd(pattern="تك(?: |$)(.*)", command="demote"))
@icssbot.on(sudo_cmd(pattern="تك(?: |$)(.*)", command="demote", allow_sudo=True))
async def demote(dmod):
    if dmod.fwd_from:
        return
    chat = await dmod.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(dmod, NO_ADMIN)
        return
    icse = await eor(dmod, "↮")
    rank = "مشرف"
    user = await get_user_from_event(dmod)
    user = user[0]
    if not user:
        return
    newrights = ChatAdminRights(
        add_admins=None,
        invite_users=None,
        change_info=None,
        ban_users=None,
        delete_messages=None,
        pin_messages=None,
    )
    try:
        await dmod.client(EditAdminRequest(dmod.chat_id, user.id, newrights, rank))
    except BadRequestError:
        await icse.edit(NO_PERM)
        return
    await icse.edit("**- ❝ ⌊  تم تنزلـيه من الاشـرف بنجـاح  𓆰.**")
    if BOTLOG:
        await dmod.client.send_message(
            BOTLOG_CHATID,
            "#تنزيل_مشرف\n"
            f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
            f"الدردشه: {dmod.chat.title}(`{dmod.chat_id}`)",
        )


# ====================================================== #


@icssbot.on(admin_cmd(pattern="دي(?: |$)(.*)", command="ban"))
@icssbot.on(sudo_cmd(pattern="دي(?: |$)(.*)", command="ban", allow_sudo=True))
async def ban(bon):
    if bon.fwd_from:
        return
    chat = await bon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(bon, NO_ADMIN)
        return
    user, reason = await get_user_from_event(bon)
    if not user:
        return
    icse = await eor(bon, "**╮ ❐  جـاري حظره  ❏╰**")
    try:
        await bon.client(EditBannedRequest(bon.chat_id, user.id, BANNED_RIGHTS))
    except BadRequestError:
        await icse.edit(NO_PERM)
        return
    try:
        reply = await bon.get_reply_message()
        if reply:
            await reply.delete()
    except BadRequestError:
        await icse.edit(
            "** ⪼ ليس لدي صلاحيـة حذف الرسـائل لڪنه لايـزال محظـور 𓆰،**"
        )
        return
    if reason:
        await icse.edit(f"`{str(user.id)}` محظور !!\n دقيقه: {reason}")
    else:
        await icse.edit(f"`{str(user.id)}` محظور !!")
    if BOTLOG:
        await bon.client.send_message(
            BOTLOG_CHATID,
            "#حظر\n"
            f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
            f"الدردشه: {bon.chat.title}(`{bon.chat_id}`)",
        )


# ====================================================== #


@icssbot.on(icss_cmd(pattern="رفع القيود(?: |$)(.*)", command="unban"))
@icssbot.on(sudo_cmd(pattern="رفع القيود(?: |$)(.*)", command="unban", allow_sudo=True))
async def nothanos(unbon):
    if unbon.fwd_from:
        return
    chat = await unbon.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(unbon, NO_ADMIN)
        return
    icse = await eor(unbon, "**╮ ❐  جـاري رفـع القيـود  ❏╰**")
    user = await get_user_from_event(unbon)
    user = user[0]
    if not user:
        return
    try:
        await unbon.client(EditBannedRequest(unbon.chat_id, user.id, UNBAN_RIGHTS))
        await ics.edit("تم رفع جميع القيود")
        if BOTLOG:
            await unbon.client.send_message(
                BOTLOG_CHATID,
                "#رفع_القيود\n"
                f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
                f"الدردشه: {unbon.chat.title}(`{unbon.chat_id}`)",
            )
    except UserIdInvalidError:
        await icse.edit("**- ❝ ⌊  تم رفـع جميـع القيـود بنجـاح  𓆰.**")


# ====================================================== #


@bot.on(admin_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        try:
            await event.delete()
        except Exception as e:
            LOGS.info(str(e))


# ====================================================== #


@icssbot.on(icss_cmd(pattern="تقيد(?: |$)(.*)", command="mute"))
@icssbot.on(sudo_cmd(pattern="تقيد(?: |$)(.*)", command="mute", allow_sudo=True))
async def startmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("**╮ ❐  جـاري تقيده  ❏╰**")
        await sleep(3)
        await event.get_reply_message()
        userid = event.chat_id
        replied_user = await event.client(GetFullUserRequest(userid))
        chat_id = event.chat_id
        if is_muted(userid, chat_id):
            return await event.edit("**╮ ❐ المسـتخدم مقيد بالفعـل  ❏╰**")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.edit("حدث خطأ!\nالخطأ هو " + str(e))
        else:
            await event.edit("**╮ ❐ تم تقـيده  ❏╰**")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#تقيد\n"
                f"المستخدم: [{replied_user.user.first_name}](tg://user?id={userid})\n"
                f"الدردشه: {event.chat.title}(`{event.chat_id}`)",
            )
    else:
        chat = await event.get_chat()
        user, reason = await get_user_from_event(event)
        if not user:
            return
        if user.id == bot.uid:
            return await eor(event, "**- ❝ ⌊  لا استـطيع تقيـد نفـسي  𓆰.**")
        if is_muted(user.id, event.chat_id):
            return await eor(event, "**╮ ❐ المسـتخدم مقيد بالفعـل  ❏╰**")
        try:
            admin = chat.admin_rights
            creator = chat.creator
            if not admin and not creator:
                await eor(
                    event, "** ⪼ لا استطيع تقـيد شخص بـدون صلاحـيات الشرفـين 𓆰،** "
                )
                return
            result = await event.client(
                functions.channels.GetParticipantRequest(
                    channel=event.chat_id, user_id=user.id
                )
            )
            try:
                if result.participant.banned_rights.send_messages:
                    return await eor(
                        event,
                        "**مقيد بالفعل- **",
                    )
            except:
                pass
            await event.client(EditBannedRequest(event.chat_id, user.id, MUTE_RIGHTS))
        except UserAdminInvalidError:
            if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None:
                if chat.admin_rights.delete_messages is not True:
                    return await eor(
                        event,
                        "**⪼ لا يمكنك كتم أي شخص إذا لم يكن لديك إذن حذف الرسائل  𓆰،**",
                    )
            elif "creator" not in vars(chat):
                return await eor(
                    event, "**⪼ لا يمكنك كتم أي شخص بدون صلاحيه مشرفين  𓆰، ** "
                )
            try:
                mute(user.id, event.chat_id)
            except Exception as e:
                return await eor(event, "حدث خطأ!\nالخطأ هو " + str(e))
        except Exception as e:
            return await eor(event, f"**خطأ : **`{str(e)}`")
        if reason:
            await eor(
                event,
                f" المستخدم ↫[{user.first_name}](tg://user?id={user.id})تم تقيده بنجاح✅"
                #                 f"`Reason:`{reason}",
            )
        else:
            await eor(
                event,
                f"المستخدم ↫[{user.first_name}](tg://user?id={user.id})تم تقيده بنجاح✅",
            )
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#تقيد\n"
                f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
                f"الدردشه: {event.chat.title}(`{event.chat_id}`)",
            )


# ====================================================== #


@icssbot.on(icss_cmd(pattern="الغاء تقيد(?: |$)(.*)", command="unmute"))
@icssbot.on(sudo_cmd(pattern="الغاء تقيد(?: |$)(.*)", command="unmute", allow_sudo=True))
async def endmute(event):
    if event.fwd_from:
        return
    if event.is_private:
        await event.edit("**╮ ❐  جـاري الغـاء تقيده  ❏╰**")
        await sleep(3)
        userid = event.chat_id
        replied_user = await event.client(GetFullUserRequest(userid))
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.edit("**❐ ⋮ هذا المستخدم غير مقيد هنا**")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.edit("حدث خطأ!\nالخطأ هو " + str(e))
        else:
            await event.edit("** - ❝ ⌊  تم رفـع القيـود عـنه  𓆰.**")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#رفع_القيود\n"
                f"المستخدم: [{replied_user.user.first_name}](tg://user?id={userid})\n"
                f"الدردشه: {event.chat.title}(`{event.chat_id}`)",
            )
    else:
        user = await get_user_from_event(event)
        user = user[0]
        if not user:
            return
        try:
            if is_muted(user.id, event.chat_id):
                unmute(user.id, event.chat_id)
            else:
                result = await event.client(
                    functions.channels.GetParticipantRequest(
                        channel=event.chat_id, user_id=user.id
                    )
                )
                try:
                    if result.participant.banned_rights.send_messages:
                        await event.client(
                            EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS)
                        )
                except:
                    return await eor(
                        event,
                        "هذا المستخدم غير مقيد هنا~~",
                    )
        except Exception as e:
            return await eor(event, f"**خطأ : **`{str(e)}`")
        await eor(event, "** - ❝ ⌊  تم رفـع القيـود عـنه  𓆰.**")
        if BOTLOG:
            await event.client.send_message(
                BOTLOG_CHATID,
                "#رفع_القيود\n"
                f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
                f"الدردشه: {event.chat.title}(`{event.chat_id}`)",
            )


# ====================================================== #


@icssbot.on(icss_cmd(pattern="طرد(?: |$)(.*)", command="kick"))
@icssbot.on(sudo_cmd(pattern="طرد(?: |$)(.*)", command="kick", allow_sudo=True))
async def kick(usr):
    if usr.fwd_from:
        return
    chat = await usr.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await eor(usr, NO_ADMIN)
        return
    user, reason = await get_user_from_event(usr)
    if not user:
        await eor(usr, "**تعذر جلب المستخدم.**")
        return
    icse = await eor(usr, "**جـاري طرد...**")
    try:
        await usr.client.kick_participant(usr.chat_id, user.id)
        await sleep(0.5)
    except Exception as e:
        await icse.edit(NO_PERM + f"\n{str(e)}")
        return
    if reason:
        await icse.edit(
            f"**- ❝ ⌊  تم طرد** [{user.first_name}](tg://user?id={user.id})  𓆰."
        )
    else:
        await icse.edit(
            f"**- ❝ ⌊  تم طرد** [{user.first_name}](tg://user?id={user.id})  𓆰."
        )
    if BOTLOG:
        await usr.client.send_message(
            BOTLOG_CHATID,
            "#طرد\n"
            f"المستخدم: [{user.first_name}](tg://user?id={user.id})\n"
            f"الدردشه: {usr.chat.title}(`{usr.chat_id}`)\n",
        )


# ====================================================== #


@icssbot.on(icss_cmd(pattern="تثبيت($| (.*))", command="pin"))
@icssbot.on(sudo_cmd(pattern="تثبيت($| (.*))", command="pin", allow_sudo=True))
async def pin(msg):
    if msg.fwd_from:
        return
    if not msg.is_private:
        await msg.get_chat()
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        return await edit_delete(msg, "**الرد على رسالة لتثبيتها.**", 5)
    options = msg.pattern_match.group(1)
    is_silent = False
    if options == "loud":
        is_silent = True
    try:
        await msg.client.pin_message(msg.chat_id, to_pin, notify=is_silent)
    except BadRequestError:
        return await ed(msg, NO_PERM, 5)
    except Exception as e:
        return await ed(msg, f"`{str(e)}`", 5)
    await edit_delete(msg, "**تم التثبيت بنجاح✔**", 3)
    user = await get_user_from_id(msg.sender_id, msg)
    if BOTLOG and not msg.is_private:
        try:
            await msg.client.send_message(
                BOTLOG_CHATID,
                "#تثبيت\n"
                f"الادمن: [{user.first_name}](tg://user?id={user.id})\n"
                f"الدردشه: {msg.chat.title}(`{msg.chat_id}`)\n",
                #                 f"LOUD: {is_silent}",
            )
        except:
            pass


# ====================================================== #


@icssbot.on(icss_cmd(pattern="الغاء تثبيت($| (.*))", command="unpin"))
@icssbot.on(sudo_cmd(pattern="الغاء تثبيت($| (.*))", command="unpin", allow_sudo=True))
async def pin(msg):
    if msg.fwd_from:
        return
    if not msg.is_private:
        await msg.get_chat()
    to_unpin = msg.reply_to_msg_id
    options = (msg.pattern_match.group(1)).strip()
    if not to_unpin and options != "الكل":
        await ed(
            msg,
            "**يمكنك الرد على رسالة لإلغاء تثبيتها أو استخدام .الغاء تثبيت الكل**",
            5,
        )
        return
    if to_unpin and not options:
        try:
            await msg.client.unpin_message(msg.chat_id, to_unpin)
        except BadRequestError:
            return await ed(msg, NO_PERM, 5)
        except Exception as e:
            return await ed(msg, f"`{str(e)}`", 5)
    elif options == "الكل":
        try:
            await msg.client.unpin_message(msg.chat_id)
        except BadRequestError:
            return await ed(msg, NO_PERM, 5)
        except Exception as e:
            return await ed(msg, f"`{str(e)}`", 5)
    else:
        return await ed(
            msg,
            "** - ❝ ⌊   يمكنك الرد على رسالة لإلغاء تثبيتها أو استخدام .الغاء تثبيت الكل 𓆰.**",
            5,
        )
    await ed(msg, "**تم إلغاء التثبيت بنجاح✔**", 3)
    user = await get_user_from_id(msg.sender_id, msg)
    if BOTLOG and not msg.is_private:
        try:
            await msg.client.send_message(
                BOTLOG_CHATID,
                "#الغاء_تثبيت\n"
                f"**الادمن : **[{user.first_name}](tg://user?id={user.id})\n"
                f"**الدردشه : **{msg.chat.title}(`{msg.chat_id}`)\n",
            )
        except:
            pass


CMD_HELP.update(
    {
        "admin": "**Plugin : **`admin`\
        \n\n  •  **Syntax : **`.setgpic` <reply to image>\
        \n  •  **Usage : **Changes the group's display picture\
        \n\n  •  **Syntax : **`.promote` <username/reply> <custom rank (optional)>\
        \n  •  **Usage : **Provides admin rights to the person in the chat.\
        \n\n  •  **Syntax : **`.demote `<username/reply>\
        \n  •  **Usage : **Revokes the person's admin permissions in the chat.\
        \n\n  •  **Syntax : **`.ban` <username/reply> <reason (optional)>\
        \n  •  **Usage : **Bans the person off your chat.\
        \n\n  •  **Syntax : **`.unban` <username/reply>\
        \n  •  **Usage : **Removes the ban from the person in the chat.\
        \n\n  •  **Syntax : **`.mute` <username/reply> <reason (optional)>\
        \n  •  **Usage : **Mutes the person in the chat, works on admins too.\
        \n\n  •  **Syntax : **`.unmute` <username/reply>\
        \n  •  **Usage : **Removes the person from the muted list.\
        \n\n  •  **Syntax : **`.pin `<reply> or `.pin loud`\
        \n  •  **Usage : **Pins the replied message in Group\
        \n\n  •  **Syntax : **`.unpin `<reply> or `.unpin all`\
        \n  •  **Usage : **Unpins the replied message in Group\
        \n\n  •  **Syntax : **`.kick `<username/reply> \
        \n  •  **Usage : **kick the person off your chat.\
        \n\n  •  **Syntax : **`.iundlt`\
        \n  •  **Usage : **display last 5 deleted messages in group."
    }
)
