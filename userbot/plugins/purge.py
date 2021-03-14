from asyncio import sleep

from ..utils import errors_handler
from . import BOTLOG, BOTLOG_CHATID


@icssbot.on(admin_cmd(outgoing=True, pattern="تنظيف$"))
@icssbot.on(sudo_cmd(allow_sudo=True, pattern="تنظيف$"))
@errors_handler
async def fastpurger(purg):
    # For .purge command, purge all messages starting from the reply.
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0

    if purg.reply_to_msg_id is not None:
        async for msg in itermsg:
            msgs.append(msg)
            count += 1
            msgs.append(purg.reply_to_msg_id)
            if len(msgs) == 100:
                await purg.client.delete_messages(chat, msgs)
                msgs = []
    else:
        await edit_or_reply(
            purg,
            "**⪼ قم برد على اي رساله وسيتم حذف جميع الرسائل التي تليـها ༗ .**",
        )
        return

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "**⪼ اكتمل الحذف السريع ❕**\n⪼ حذف " + str(count) + " رساله 𓆰",
    )

    if BOTLOG:
        await purg.client.send_message(
            BOTLOG_CHATID,
            "#التنظيف \n⪼ تم تنظيف " + str(count) + " رساله بنجاح 𓆰",
        )
    await sleep(2)
    await done.delete()


CMD_HELP.update(
    {
        "purge": "**Plugin : **`purge`\
        \n\n**Syntax : **`.purge reply to message to start purge from there`\
        \n**Function : **__Purges all messages starting from the reply.__\
        \n\n**Syntax : **`.purgeme <x>`\
        \n**Function : **__Deletes x amount of your latest messages.__\
        \n\n**Syntax : **`.del reply to message to delete`\
        \n**Function : **__Deletes the message you replied to.__"
    }
)
