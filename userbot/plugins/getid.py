# get id code for icss edit by @rruuurr

from telethon.utils import pack_bot_file_id


@icssbot.on(admin_cmd(pattern="(الايدي|id)( (.*)|$)"))
@icssbot.on(sudo_cmd(pattern="(الايدي|id)( (.*)|$)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(2)
    if input_str:
        try:
            p = await event.client.get_entity(input_str)
        except Exception as e:
            return await edit_delete(event, f"`{str(e)}`", 5)
        try:
            if p.first_name:
                return await edit_or_reply(
                    event, f"⪼ ايدي المستخدم `{input_str}` هو `{p.id}` 𓆰."
                )
        except:
            try:
                if p.title:
                    return await edit_or_reply(
                        event, f"⪼ ايدي الدردشة / القناة `{p.title}` هو `{p.id}` 𓆰."
                    )
            except:
                pass
        await edit_or_reply(event, "⪼ **أدخل إما اسم مستخدم أو الرد على المستخدم**")
    elif event.reply_to_msg_id:
        await event.get_input_chat()
        r_msg = await event.get_reply_message()
        if r_msg.media:
            bot_api_file_id = pack_bot_file_id(r_msg.media)
            await edit_or_reply(
                event,
                f"⪼ **ايدي الدردشه : **`{str(event.chat_id)}` 𓆰.\n**⪼ ايدي المستخدم : **`{str(r_msg.sender_id)}` 𓆰.\n⪼ **ايدي الميديا : **`{bot_api_file_id}` 𓆰.",
            )
        else:
            await edit_or_reply(
                event,
                f"⪼ **ايدي الدردشه : **`{str(event.chat_id)}` 𓆰.\n⪼ **ايدي المستخدم: **`{str(r_msg.sender_id)}` 𓆰.",
            )
    else:
        await edit_or_reply(event, f"⪼ **ايدي الدردشه : **`{str(event.chat_id)}` 𓆰.")


CMD_HELP.update(
    {
        "getid": "**Plugin : **`getid`\
    \n\n  •  **Syntax : **`.get_id` or `.id`\
    \n  •  **Function : **__if given input then shows id of that given chat/channel/user else if you reply to user then shows id of the replied user \
    along with current chat id and if not replied to user or given input then just show id of the chat where you used the command__"
    }
)
