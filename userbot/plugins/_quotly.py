"""
imported from nicegrill
modified by @mrconfused
edit by ~ @rruuurr
QuotLy: Avaible commands: .qbot
"""
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from . import Quotly, convert_tosticker, process
from userbot import bot

# ---------------------- #
UserId = bot.me.id
Name = bot.me.first_name
Mention = "[{}](tg://user?id={})".format(Name, UserId)
# ---------------------- #

@icssbot.on(icss_cmd(pattern="q(?: |$)(.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="q(?: |$)(.*)", allow_sudo=True))
async def _(e):
    if e.fwd_from:
        return
    reply = await e.get_reply_message()
    if not reply:
        await eor(e, Quotly[0].format(Mention))
        return
    fetchmsg = reply.message
    repliedreply = None
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await eor(e, Quotly[1].format(Mention))
        return
    ie = await eor(e, Quotly[2])
    user = (
        await event.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, icsmsg = await process(fetchmsg, user, e.client, reply, repliedreply)
    if not res:
        return
    outfi = os.path.join("./temp", "sticker.png")
    icsmsg.save(outfi)
    endfi = convert_tosticker(outfi)
    await e.client.send_file(e.chat_id, endfi, reply_to=reply)
    await ie.delete()
    os.remove(endfi)


@icssbot.on(icss_cmd(pattern="rq(?: |$)(.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="rq(?: |$)(.*)", allow_sudo=True))
async def _(e):
    if e.fwd_from:
        return
    reply = await e.get_reply_message()
    if not reply:
        await eor(e, Quotly[0].format(Mention))
        return
    fetchmsg = reply.message
    repliedreply = await reply.get_reply_message()
    if reply.media and reply.media.document.mime_type in ("mp4"):
        await eor(e, Quotly[1].format(Mention))
        return
    ie = await eor(e, Quotly[2])
    user = (
        await event.client.get_entity(reply.forward.sender)
        if reply.fwd_from
        else reply.sender
    )
    res, icsmsg = await process(fetchmsg, user, e.client, reply, repliedreply)
    if not res:
        return
    outfi = os.path.join("./temp", "sticker.png")
    icsmsg.save(outfi)
    endfi = convert_tosticker(outfi)
    await e.client.send_file(e.chat_id, endfi, reply_to=reply)
    await ie.delete()
    os.remove(endfi)


@icssbot.on(icss_cmd(pattern="qbot(?: |$)(.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="qbot(?: |$)(.*)", allow_sudo=True))
async def _(e):
    if e.fwd_from:
        return
    reply_to = await reply_id(e)
    input_str = e.pattern_match.group(1)
    reply = await e.get_reply_message()
    message = ""
    messages_id = []
    if reply:
        if input_str and input_str.isnumeric():
            messages_id.append(reply.id)
            async for message in e.client.iter_messages(
                e.chat_id,
                limit=(int(input_str) - 1),
                offset_id=reply.id,
                reverse=True,
            ):
                if message.id != e.id:
                    messages_id.append(message.id)
        elif input_str:
            message = input_str
        else:
            messages_id.append(reply.id)
    elif input_str:
        message = input_str
    else:
        return await ed(e, Quotly[3])
    chat = "@QuotLyBot"
    ie = await eor(e, Quotly[2])
    async with e.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            if messages_id != []:
                await e.client.forward_messages(chat, messages_id, e.chat_id)
            elif message != "":
                await e.client.send_message(conv.chat_id, message)
            else:
                return await ed(ie, Quotly[4].format(Mention))
            response = await response
        except YouBlockedUserError:
            await ie.edit(Quotly[5])
            return
        await e.client.send_read_acknowledge(conv.chat_id)
        await ie.delete()
        await e.client.send_message(
            e.chat_id, response.message, reply_to=reply_to
        )


CMD_HELP.update(
    {
        "quotly": "**Plugin :** `quotly`\
        \n\n**•  Syntax : **`.q reply to messge`\
        \n**•  Function : **__Makes your message as sticker quote__\
        \n\n**•  Syntax : **`.rq reply to messge`\
        \n**•  Function : **__Makes your message along with the previous replied message as sticker quote__\
        \n\n**•  Syntax : **`.qbot reply to messge`\
        \n**•  Function : **__Makes your message as sticker quote by @quotlybot__\
        "
    }
)
