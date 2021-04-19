# ©icss - @rruuurr

from telethon.tl.functions.messages import SaveDraftRequest


@icssbot.on(admin_cmd(pattern="ردود$"))
@icssbot.on(sudo_cmd(pattern="ردود$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("**⌔∮ يتم حساب الردود.**")
    count = -1
    message = event.message
    while message:
        reply = await message.get_reply_message()
        if reply is None:
            await event.client(
                SaveDraftRequest(
                    await event.get_input_chat(), "", reply_to_msg_id=message.id
                )
            )
        message = reply
        count += 1
    await event.edit(f"**⌔∮ ردود الرساله :** {count}")


CMD_HELP.update(
    {
        "chain": """**Plugin :**`chain`
        
  • **Syntax : **`.chain reply to message`
  • **Function : **__Reply this command to any converstion(or message) so that it finds chain length of that message__"""
    }
)
