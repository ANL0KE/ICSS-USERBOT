"""
©icss : @rruuurr
  - Welcome Code For Icss
  - Add Welcome Commend   : .ترحيب
  - list Welcome Commend  : .الترحيب
  - Remove Welcome Commend: .حذف ترحيب
"""

from telethon import events

from userbot.plugins.sql_helper.welcome_sql import (
    add_welcome_setting,
    get_current_welcome_settings,
    rm_welcome_setting,
    update_previous_welcome,
)

from . import BOTLOG_CHATID, LOGS


@icssbot.on(events.ChatAction)
async def _(event):
    cws = get_current_welcome_settings(event.chat_id)
    if (
        cws
        and (event.user_joined or event.user_added)
        and not (await event.get_user()).bot
    ):
        if Config.CLEAN_WELCOME:
            try:
                await bot.delete_messages(event.chat_id, cws.previous_welcome)
            except Exception as e:
                LOGS.warn(str(e))
        a_user = await event.get_user()
        chat = await event.get_chat()
        me = await bot.get_me()
        title = chat.title or "this chat"
        participants = await bot.get_participants(chat)
        count = len(participants)
        mention = "<a href='tg://user?id={}'>{}</a>".format(
            a_user.id, a_user.first_name
        )
        my_mention = "<a href='tg://user?id={}'>{}</a>".format(me.id, me.first_name)
        first = a_user.first_name
        last = a_user.last_name
        fullname = f"{first} {last}" if last else first
        username = f"@{a_user.username}" if a_user.username else mention
        userid = a_user.id
        my_first = me.first_name
        my_last = me.last_name
        my_fullname = f"{my_first} {my_last}" if my_last else my_first
        my_username = f"@{me.username}" if me.username else my_mention
        file_media = None
        current_saved_welcome_message = None
        if cws:
            if cws.f_mesg_id:
                msg_o = await event.client.get_messages(
                    entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id)
                )
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws.reply:
                current_saved_welcome_message = cws.reply
        current_message = await event.reply(
            current_saved_welcome_message.format(
                mention=mention,
                title=title,
                count=count,
                first=first,
                last=last,
                fullname=fullname,
                username=username,
                userid=userid,
                my_first=my_first,
                my_last=my_last,
                my_fullname=my_fullname,
                my_username=my_username,
                my_mention=my_mention,
            ),
            file=file_media,
            parse_mode="html",
        )
        update_previous_welcome(event.chat_id, current_message.id)


@icssbot.on(admin_cmd(pattern=r"ترحيب ?(.*)"))
@icssbot.on(sudo_cmd(pattern=r"ترحيب ?(.*)", allow_sudo=True))
async def save_welcome(event):
    if event.fwd_from:
        return
    msg = await event.get_reply_message()
    string = "".join(event.text.split(maxsplit=1)[1:])
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await bot.send_message(
                BOTLOG_CHATID,
                f"#الترحيب\
                \n ⪼ ايدي الدردشة: {event.chat_id}\
                \n ⪼ يتم حفظ الرسالة التالية كملاحظة ترحيب لـ {event.chat.title}, لا تحذف هذه الرسالة !!",
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID, messages=msg, from_peer=event.chat_id, silent=True
            )
            msg_id = msg_o.id
        else:
            await edit_or_reply(
                event,
                "**يتطلب حفظ الوسائط كجزء من الملاحظة الترحيبية تعيين BOTLOG_CHATID.**",
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "** ⪼ تم {} التـرحيب في هذه الدردشـه 𓆰، **"
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("حفـظ"))
    rm_welcome_setting(event.chat_id)
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        return await edit_or_reply(event, success.format("تحـديث"))
    await edit_or_reply("خطأ أثناء تعيين الترحيب في هذه المجموعة")


@icssbot.on(admin_cmd(pattern="حذف ترحيب$"))
@icssbot.on(sudo_cmd(pattern="حذف ترحيب$", allow_sudo=True))
async def del_welcome(event):
    if event.fwd_from:
        return
    if rm_welcome_setting(event.chat_id) is True:
        await edit_or_reply(
            event,
            "** ⪼ تم حـذف الترحيب في هـذه الدردشـه 𓆰،**",
        )
    else:
        await edit_or_reply(
            event,
            "** ⪼ ليس هناك اي ترحــيب فـي الـدردشــة 𓆰،**",
        )


@icssbot.on(admin_cmd(pattern="الترحيب$"))
@icssbot.on(sudo_cmd(pattern="الترحيب$", allow_sudo=True))
async def show_welcome(event):
    if event.fwd_from:
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await edit_or_reply(
            event,
            "** ⪼ لاتوجد رساله ترحيب محفوظة هنا 𓆰،**",
        )
        return
    if cws.f_mesg_id:
        msg_o = await bot.get_messages(entity=BOTLOG_CHATID, ids=int(cws.f_mesg_id))
        await edit_or_reply(
            event, "** ⪼ أرحب حاليًا بالمستخدمين الجدد بهذه الرساله الترحيبية 𓆰.🜝**"
        )
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws.reply:
        await edit_or_reply(
            event, "** ⪼ أرحب حاليًا بالمستخدمين الجدد بهذه الرساله الترحيبية.🜝**"
        )
        await event.reply(cws.reply)


CMD_HELP.update(
    {
        "welcome": "**Plugin :** `welcome`\
\n\n  •  **Syntax :** `.savewelcome` <welcome message> or reply to a message with .savewelcome\
\n  •  **Function :** Saves the message as a welcome note in the chat.\
\n\n  •  Available variables for formatting welcome messages :\
\n`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`\
\n\n  •  **Syntax :** `.listwelcome`\
\n  •  **Function :** Check whether you have a welcome note in the chat.\
\n\n  •  **Syntax :** `.clearwelcome`\
\n  •  **Function :** Deletes the welcome note for the current chat.\
"
    }
)
