# Filters for ICSS edit by: @rruuurr
import re

from . import BOTLOG, BOTLOG_CHATID
from .sql_helper.filter_sql import (
    add_filter,
    get_filters,
    remove_all_filters,
    remove_filter,
)


@icssbot.on(admin_cmd(incoming=True))
async def filter_incoming_handler(handler):
    try:
        if (
            not (await handler.get_sender()).bot
            and (handler.sender_id) != handler.client.uid
        ):
            name = handler.raw_text
            filters = get_filters(handler.chat_id)
            if not filters:
                return
            for trigger in filters:
                pattern = r"( |^|[^\w])" + re.escape(trigger.keyword) + r"( |$|[^\w])"
                if re.search(pattern, name, flags=re.IGNORECASE):
                    if trigger.f_mesg_id:
                        msg_o = await handler.client.get_messages(
                            entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id)
                        )
                        await handler.reply(msg_o.message, file=msg_o.media)
                    elif trigger.reply:
                        await handler.reply(trigger.reply)
    except AttributeError:
        pass


@icssbot.on(admin_cmd(pattern="اضف رد (.*)"))
@icssbot.on(sudo_cmd(pattern="اضف رد (.*)", allow_sudo=True))
async def add_new_filter(new_handler):
    if new_handler.fwd_from:
        return
    keyword = new_handler.pattern_match.group(1)
    string = new_handler.text.partition(keyword)[2]
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG:
            await new_handler.client.send_message(
                BOTLOG_CHATID,
                f"#الردود\
            \n ⪼ ايدي الدردشه: {new_handler.chat_id}\
            \n ⪼ الرد: {keyword}\
            \n ⪼ يتم حفظ الرسالة التالية كبيانات رد على المستخدمين في الدردشه ، يرجى عدم حذفها !!",
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                new_handler,
                "`يتطلب حفظ الوسائط كرد على المرشح تعيين BOTLOG_CHATID.`",
            )
            return
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    success = "- ❝ الرد **{}** تم {} بنجاح 𓆰."
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(new_handler, success.format(keyword, "اضافته"))
    remove_filter(str(new_handler.chat_id), keyword)
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        return await edit_or_reply(new_handler, success.format(keyword, "تحديثه"))
    await edit_or_reply(new_handler, f"خطأ أثناء تعيين عامل التصفية لـ {keyword}")


@icssbot.on(admin_cmd(pattern="الردود$"))
@icssbot.on(sudo_cmd(pattern="الردود$", allow_sudo=True))
async def on_snip_list(event):
    if event.fwd_from:
        return
    OUT_STR = "** ⪼ لاتوجـد ردود في هذه الدردشه ༗،**"
    filters = get_filters(event.chat_id)
    for filt in filters:
        if OUT_STR == "** ⪼ لاتوجـد ردود في هذه الدردشه ༗،**":
            OUT_STR = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑰𝑪𝑺𝑺 𝑭𝑰𝑳𝑻𝑬𝑹𝑺 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**  ⪼ قائمـه الـردود في هذه الدردشـه :  **\n"
        OUT_STR += "⪼ {}  𓆰.\n".format(filt.keyword)
    await edit_or_reply(
        event,
        OUT_STR,
        caption="** ⪼ الردود المضـافه في هذه الدردشه ༗،**",
        file_name="filters.text",
    )


@icssbot.on(admin_cmd(pattern="حذف رد (.*)"))
@icssbot.on(sudo_cmd(pattern="حذف رد (.*)", allow_sudo=True))
async def remove_a_filter(r_handler):
    if r_handler.fwd_from:
        return
    filt = r_handler.pattern_match.group(1)
    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.edit("- ❝ الرد ↫ **{}** غير موجود 𓆰.".format(filt))
    else:
        await r_handler.edit("- ❝ الرد ↫ **{}** تم حذفه بنجاح 𓆰.".format(filt))


@icssbot.on(admin_cmd(pattern="مسح الردود$"))
@icssbot.on(sudo_cmd(pattern="مسح الردود$", allow_sudo=True))
async def on_all_snip_delete(event):
    if event.fwd_from:
        return
    filters = get_filters(event.chat_id)
    if filters:
        remove_all_filters(event.chat_id)
        await edit_or_reply(
            event,
            f"𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑰𝑪𝑺𝑺 𝑭𝑰𝑳𝑻𝑬𝑹𝑺 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ تم حذف جـميع ردود المضافهہ بنجاح .**",
        )
    else:
        await edit_or_reply(event, f"**⪼ لا توجد ردود في هذه المجموعه 𓆰،**")


CMD_HELP.update(
    {
        "filters": "**Plugin :**`filters`\
    \n\n  •  **Syntax :** `.الردود`\
    \n  •  **Usage: **Lists all active (of your userbot) filters in a chat.\
    \n\n  •  **Syntax :** `.اضف رد`  reply to a message with .filter <keyword>\
    \n  •  **Usage: **Saves the replied message as a reply to the 'keyword'.\
    \nThe bot will reply to the message whenever 'keyword' is mentioned. Works with everything from files to stickers.\
    \n\n  •  **Syntax :** `.حذف رد <keyword>`\
    \n  •  **Usage: **Stops the specified keyword.\
    \n\n  •  **Syntax :** `.rmfilters` \
    \n  •  **Usage: **Removes all filters of your userbot in the chat."
    }
)
