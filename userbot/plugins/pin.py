from telethon import functions
from telethon.errors import (
    BadRequestError,
    ImageProcessFailedError,
    PhotoCropSizeSmallError,
)
from telethon.errors.rpcerrorlist import UserAdminInvalidError, UserIdInvalidError
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChatAdminRights, ChatBannedRights

from ..utils import errors_handler
from . import BOTLOG, BOTLOG_CHATID, LOGS, get_user_from_event


@icssbot.on(
    icss_cmd(
       pattern="تثبيت($| (.*))", command="pin"
    )
)
@icssbot.on(
    sudo_cmd(pattern="تثبيت($| (.*))", command="pin", allow_sudo=True)
)
@errors_handler
async def pin(msg):
    if msg.fwd_from:
        return
    if not msg.is_private:
        await msg.get_chat()
    to_pin = msg.reply_to_msg_id
    if not to_pin:
        return await ed(msg, "**الرد على رسالة لتثبيتها.**", 5)
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
    await ed(msg, "**تم التثبيت بنجاح✔**", 3)
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


@icssbot.on(
    icss_cmd(
       pattern="الغاء تثبيت($| (.*))", command="unpin"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="الغاء تثبيت($| (.*))", 
       command="unpin", 
       allow_sudo=True, 
    )
)
@errors_handler
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
            "**⌔∮   يمكنك الرد على رسالة لإلغاء تثبيتها أو استخدام .الغاء تثبيت الكل 𓆰.**",
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

