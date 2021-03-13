# blacklist code for icss by @rruuurr

"""اوامر المنع
.منع كلمه
.الكلمات المحظوره
.الغاء منع"""

import re

from telethon import events

import userbot.plugins.sql_helper.blacklist_sql as sql


@icssbot.on(events.NewMessage(incoming=True))
async def on_new_message(event):
    # TODO: exempt admins from locks
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception:
                await event.reply("** - ◁︱انا لا املك صلاحية الحذف❗️،**")
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@icssbot.on(admin_cmd(pattern="منع كلمه ((.|\n)*)"))
@icssbot.on(sudo_cmd(pattern="منع كلمه ((.|\n)*)", allow_sudo=True))
async def on_add_black_list(event):
    text = event.pattern_match.group(1)
    to_blacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    for trigger in to_blacklist:
        sql.add_to_blacklist(event.chat_id, trigger.lower())
    await edit_or_reply(
        event,
        "** - ◁︱تم {} منع الڪلمه ༗،**".format(len(to_blacklist)),
    )


@icssbot.on(admin_cmd(pattern="الغاء منع ((.|\n)*)"))
@icssbot.on(sudo_cmd(pattern="الغاء منع ((.|\n)*)", allow_sudo=True))
async def on_delete_blacklist(event):
    text = event.pattern_match.group(1)
    to_unblacklist = list(
        {trigger.strip() for trigger in text.split("\n") if trigger.strip()}
    )

    successful = sum(
        1
        for trigger in to_unblacklist
        if sql.rm_from_blacklist(event.chat_id, trigger.lower())
    )

    await edit_or_reply(
        event,
        f"** - ◁︱تم {successful} / {len(to_unblacklist)} الغاء منع الڪلمه ༗،**",
    )


@icssbot.on(admin_cmd(pattern="الكلمات المحظوره$"))
@icssbot.on(sudo_cmd(pattern="الكلمات المحظوره$", allow_sudo=True))
async def on_view_blacklist(event):
    all_blacklisted = sql.get_chat_blacklist(event.chat_id)
    OUT_STR = "𓆩 𝑺𝑼𝑶𝑹𝑪𝑬 𝑰𝑪𝑺𝑺  -  𝑩𝑳𝑨𝑪𝑲𝑳𝑰𝑺𝑻 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⪼ قائمه الكلمات المحظوره :**\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"⪼ {trigger} 𓆰.\n"
    else:
        OUT_STR = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺  -  𝑩𝑳𝑨𝑪𝑲𝑳𝑰𝑺𝑻 𓆪\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n** - ◁︱لا توجد ڪلمات محظوره قم باضافة ڪلمه من خلال امر**. `.منع كلمه` 𓆰."
    if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption="Blacklists in the Current Chat",
                reply_to=event,
            )
            await event.delete()
    else:
        await edit_or_reply(event, OUT_STR)


CMD_HELP.update(
    {
        "blacklist": "**blacklist**\
    \n**Syntax : **`.addblacklist` <word/words>\
    \n**Usage : **The given word or words will be added to blacklist in that specific chat if any user sends then the message gets deleted.\
    \n\n**Syntax : **`.rmblacklist` <word/words>\
    \n**Usage : **The given word or words will be removed from blacklist in that specific chat\
    \n\n**Syntax : **`.listblacklist`\
    \n**Usage : **Shows you the list of blacklist words in that specific chat\
    \n\n**Note : **if you are adding more than one word at time via this, then remember that new word must be given in a new line that is not [hi hello]. It must be as\
    \n[hi \n hello]"
    }
)
