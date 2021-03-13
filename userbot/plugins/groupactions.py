from asyncio import sleep

from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl import functions
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)

from . import BOTLOG, BOTLOG_CHATID

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


@icssbot.on(admin_cmd(outgoing=True, pattern="kickme$"))
async def kickme(leave):
    await leave.edit("Nope, no, no, I go away")
    await leave.client.kick_participant(leave.chat_id, "me")


@icssbot.on(admin_cmd(pattern="تفليش بلطرد?(.*)"))
@icssbot.on(sudo_cmd(pattern="تفليش بلطرد?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await edit_or_reply(event, "**⪼ هل هذا كروب ! 𓆰**")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(event, "**⪼ تحتاج الى ان تكون مشرف في المجموعه 𓆰**")
        return
    result = await event.client(
        functions.channels.GetParticipantRequest(
            channel=event.chat_id, user_id=event.client.uid
        )
    )
    if not result.participant.admin_rights.ban_users:
        return await edit_or_reply(
            event, "⪼ يبدو أنك لم تقم بحظر إذن المستخدمين في هذه المجموعة 𓆰"
        )
    catevent = await edit_or_reply(event, "**╮ ❐ جـاري طرد الكل 𓅫╰**")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client.kick_participant(event.chat_id, user.id)
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await catevent.edit(
        f"**⪼ لقد أكملت بنجاح عملية طرد** {success} **عضو من** {total} **عضو 𓆰**"
    )


@icssbot.on(admin_cmd(pattern="تفليش بلحظر?(.*)"))
@icssbot.on(sudo_cmd(pattern="تفليش بلحظر?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if not event.is_group:
        await edit_or_reply(event, "**⪼ هل هذا كروب ! 𓆰**")
        return
    chat = await event.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_or_reply(event, "**⪼ تحتاج الى ان تكون مشرف في المجموعه 𓆰**")
        return
    result = await event.client(
        functions.channels.GetParticipantRequest(
            channel=event.chat_id, user_id=event.client.uid
        )
    )
    if not result:
        return await edit_or_reply(
            event, "⪼ يبدو أنك لا تملك اصلاحية حظر المستخدمين في هذه المجموعة 𓆰"
        )
    catevent = await edit_or_reply(event, "**╮ ❐ جـاري حظر الكل 𓅫╰**")
    admins = await event.client.get_participants(
        event.chat_id, filter=ChannelParticipantsAdmins
    )
    admins_id = [i.id for i in admins]
    total = 0
    success = 0
    async for user in event.client.iter_participants(event.chat_id):
        total += 1
        try:
            if user.id not in admins_id:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
                success += 1
                await sleep(0.5)
        except Exception as e:
            LOGS.info(str(e))
            await sleep(0.5)
    await catevent.edit(
        f"**⪼ لقد أكملت بنجاح عملية حظر** {success} **عضو من** {total} **عضو 𓆰**"
    )


@icssbot.on(admin_cmd(pattern="رفع الحظر ?(.*)"))
@icssbot.on(sudo_cmd(pattern="رفع الحظر ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        LOGS.info("TODO: Not yet Implemented")
    else:
        if event.is_private:
            return False
        et = await edit_or_reply(event, "**↫ البحث في قوائم المشاركين ⇲**")
        p = 0
        async for i in event.client.iter_participants(
            event.chat_id, filter=ChannelParticipantsKicked, aggressive=True
        ):
            rights = ChatBannedRights(until_date=0, view_messages=False)
            try:
                await event.client(
                    functions.channels.EditBannedRequest(event.chat_id, i, rights)
                )
            except Exception as ex:
                await et.edit(str(ex))
            else:
                p += 1
        await et.edit("⪼ {} **↫** {} **رفع الحظر عنهم**".format(event.chat_id, p))


@icssbot.on(admin_cmd(pattern="الاحصائيات ?(.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="الاحصائيات ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return False
    input_str = event.pattern_match.group(1)
    if input_str:
        chat = await event.get_chat()
        if not chat.admin_rights and not chat.creator:
            await edit_or_reply(event, "**⪼ يجب ان تكون مشرف اولاً 𓆰**")
            return False
    p = 0
    b = 0
    c = 0
    d = 0
    e = []
    m = 0
    n = 0
    y = 0
    w = 0
    o = 0
    q = 0
    r = 0
    et = await edit_or_reply(event, "**↫ البحث في قوائم المشاركين ⇲**")
    async for i in event.client.iter_participants(event.chat_id):
        p += 1
        #
        # Note that it's "reversed". You must set to ``True`` the permissions
        # you want to REMOVE, and leave as ``None`` those you want to KEEP.
        rights = ChatBannedRights(until_date=None, view_messages=True)
        if isinstance(i.status, UserStatusEmpty):
            y += 1
            if "y" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastMonth):
            m += 1
            if "m" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusLastWeek):
            w += 1
            if "w" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
                    break
        if isinstance(i.status, UserStatusOffline):
            o += 1
            if "o" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusOnline):
            q += 1
            if "q" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
                    break
                else:
                    c += 1
        if isinstance(i.status, UserStatusRecently):
            r += 1
            if "r" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
                    break
        if i.bot:
            b += 1
            if "b" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if not status:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
                    break
                else:
                    c += 1
        elif i.deleted:
            d += 1
            if "d" in input_str:
                status, e = await ban_user(event.chat_id, i, rights)
                if status:
                    c += 1
                else:
                    await et.edit("**↫ احتاج الى صلاحيات المشرف اولا ⇲**")
                    e.append(str(e))
        elif i.status is None:
            n += 1
    if input_str:
        required_string = """𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺  - 𝑮𝑹𝑼𝑶𝑷 𝑫𝑨𝑻𝑨 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
**⌔∮ المطرودين {} / {} المستخدمين 
**⌔∮ الحسابات المحذوفه :** {}
**⌔∮ اخر ظهور منذ زمن طويل :** {}
**⌔∮ اخر ظهور منذ شهر :** {}
**⌔∮ اخر ظهور منذ اسبوع :** {}
**⌔∮ متصل :** {}
**⌔∮ غير متصل :** {}
**⌔∮ اخر ظهور منذ قليل :** {}
**⌔∮ البوتات :** {}
𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"""
        await et.edit(required_string.format(c, p, d, y, m, w, o, q, r, b, n))
        await sleep(5)
    await et.edit(
        """𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺  - 𝑮𝑹𝑼𝑶𝑷 𝑫𝑨𝑻𝑨 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻
**⌔∮ العدد : ** {} مستخدم 
**⌔∮ الحسابات المحذوفه :** {}
**⌔∮ اخر ظهور منذ زمن طويل :** {}
**⌔∮ اخر ظهور منذ شهر :** {}
**⌔∮ اخر ظهور منذ اسبوع :** {}
**⌔∮ متصل :** {}
**⌔∮ غير متصل :** {}
**⌔∮ اخر ظهور منذ قليل :** {}
**⌔∮ البوتات :** {}
𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻""".format(
            p, d, y, m, w, o, q, r, b, n
        )
    )


@icssbot.on(admin_cmd(pattern=f"zombies ?(.*)"))
@icssbot.on(sudo_cmd(pattern="zombies ?(.*)", allow_sudo=True))
async def rm_deletedacc(show):
    con = show.pattern_match.group(1).lower()
    del_u = 0
    del_status = "`No zombies or deleted accounts found in this group, Group is clean`"
    if con != "clean":
        event = await edit_or_reply(
            show, "`Searching for ghost/deleted/zombie accounts...`"
        )
        async for user in show.client.iter_participants(show.chat_id):
            if user.deleted:
                del_u += 1
                await sleep(0.5)
        if del_u > 0:
            del_status = f"__Found__ **{del_u}** __ghost/deleted/zombie account(s) in this group,\
                           \nclean them by using__ `.zombies clean`"
        await event.edit(del_status)
        return
    chat = await show.get_chat()
    admin = chat.admin_rights
    creator = chat.creator
    if not admin and not creator:
        await edit_delete(show, "`I am not an admin here!`", 5)
        return
    event = await edit_or_reply(
        show, "`Deleting deleted accounts...\nOh I can do that?!?!`"
    )
    del_u = 0
    del_a = 0
    async for user in show.client.iter_participants(show.chat_id):
        if user.deleted:
            try:
                await show.client.kick_participant(show.chat_id, user.id)
                await sleep(0.5)
                del_u += 1
            except ChatAdminRequiredError:
                await edit_delete(event, "`I don't have ban rights in this group`", 5)
                return
            except UserAdminInvalidError:
                del_a += 1
    if del_u > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s)"
    if del_a > 0:
        del_status = f"Cleaned **{del_u}** deleted account(s) \
        \n**{del_a}** deleted admin accounts are not removed"
    await edit_delete(event, del_status, 5)
    if BOTLOG:
        await show.client.send_message(
            BOTLOG_CHATID,
            f"#CLEANUP\
            \n{del_status}\
            \nCHAT: {show.chat.title}(`{show.chat_id}`)",
        )


async def ban_user(chat_id, i, rights):
    try:
        await bot(functions.channels.EditBannedRequest(chat_id, i, rights))
        return True, None
    except Exception as exc:
        return False, str(exc)


CMD_HELP.update(
    {
        "groupactions": "**Plugin : **`groupactions`\
    \n\n•  **Syntax : **`.kickme`\
    \n•  **Function : **__Throws you away from that chat_\
    \n\n•  **Syntax : **`.kickall`\
    \n•  **Function : **__To kick all users except admins from the chat__\
    \n\n•  **Syntax : **`.banall`\
    \n•  **Function : **__To ban all users except admins from the chat__\
    \n\n•  **Syntax : **`.unbanall`\
    \n•  **Function : **__Unbans everyone who are blocked in that group __\
    \n\n•  **Syntax : **`.ikuck`\
    \n•  **Function : **__stats of the group like no of users no of deleted users.__\
    \n\n•  **Syntax : **`.zombies`\
    \n•  **Function : **__Searches for deleted accounts in a group. Use `.zombies clean` to remove deleted accounts from the group.__"
    }
)
