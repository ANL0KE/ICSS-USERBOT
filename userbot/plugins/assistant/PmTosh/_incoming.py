from userbot.plugins.assistant.sql_tosh.users_sql import add_user_to_db
from userbot.plugins.assistant.sqltosh.blacklist_sql import check_is_black_list
from telethon import events
from userbot.plugins import TOSHA_ID

# if incoming
@asst.on(events.NewMessage(func=lambda e: e.is_private))
async def _(e):
    incoming = e.raw_text
    who = e.sender_id
    if check_is_black_list(who):
        return
    if incoming.startswith("/"):
        pass
    elif who == TOSHA_ID:
        return
    else:
        await e.get_sender()
        e.chat_id
        to = await e.forward_to(TOSHA_ID)
        add_user_to_db(to.id, who, e.id)
