# ©icss - @rruuurr.
""" لانشاء بوت او كروب او قناة """

from telethon.tl import functions


@icssbot.on(admin_cmd(pattern="انشئ (بوت|كروب|قناة) (.*)"))  # pylint:disable=E0602
@icssbot.on(sudo_cmd(pattern="انشئ (بوت|كروب|قناة) (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    type_of_group = event.pattern_match.group(1)
    group_name = event.pattern_match.group(2)
    if type_of_group == "قناة":
        descript = "**⌔∮ هذه القناة اختبار تم انشائها بواسطه بوت اكسس**"
    else:
        descript = "**⌔∮ هذا كروب اختبار تم انشائه بواسطه بوت اكسس**"
    event = await edit_or_reply(event, "**⌔∮ جاري الانشاء. **")
    if type_of_group == "بوت":
        try:
            result = await event.client(
                functions.messages.CreateChatRequest(  # pylint:disable=E0602
                    users=["@sarah_robot"],
                    # Not enough users (to create a chat, for example)
                    # Telegram, no longer allows creating a chat with ourselves
                    title=group_name,
                )
            )
            created_chat_id = result.chats[0].id
            await event.client(
                functions.messages.DeleteChatUserRequest(
                    chat_id=created_chat_id, user_id="@sarah_robot"
                )
            )
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "**⌔∮ الكروب `{}` تم انشائه بنجاح.** انضم {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    elif type_of_group in ["كروب", "قناة"]:
        try:
            r = await event.client(
                functions.channels.CreateChannelRequest(
                    title=group_name,
                    about=descript,
                    megagroup=type_of_group != "قناة",
                )
            )

            created_chat_id = r.chats[0].id
            result = await event.client(
                functions.messages.ExportChatInviteRequest(
                    peer=created_chat_id,
                )
            )
            await event.edit(
                "**⌔∮ القناة `{}` تم انشائها بنجاح.** انضم {}".format(
                    group_name, result.link
                )
            )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(str(e))
    else:
        await event.edit("**⌔∮ حدث خطأ :**")


CMD_HELP.update(
    {
        "create": "**SYNTAX :** `.create b`\
    \n**USAGE : **Creates a super group and send you link\
    \n\n**SYNTAX : **`.create g`\
    \n**USAGE : **Creates a private group and sends you link\
    \n\n**SYNTAX : **`.create c`\
    \n**USAGE : **Creates a Channel and sends you link\
    \n\nhere the bot accout is owner\
    "
    }
)
