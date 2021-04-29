from userbot.plugins.assistant.sql_tosh.blacklist_sql import all_bl_users
from userbot.plugins.assistant.sql_tosh.userbase_sql import full_userbase
from telethon import events
from userbot.plugins import TOSHA_ID


@asst.on(events.NewMessage(pattern="^/stats", from_users=OWNER_ID))
async def _(e):
    allu = len(full_userbase())
    blu = len(all_bl_users())
    await asst.send_message(e.chat_id,
                             "Here is the stats for your bot:\nTotal Users = {}\nBlacklisted Users = {}".format(allu, blu)
                             )
