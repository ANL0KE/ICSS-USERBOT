# Icss - Userbot
# Owner ~ <@rruuurr>

from . import Asstid
from telethon.utils import pack_bot_file_id

@asst_cmd("الايدي")
async def _(e):
    if e.reply_to_msg_id:
        await e.get_input_chat()
        R = await e.get_reply_message()
        if R.media:
            B = pack_bot_file_id(R.media)
            await e.reply(Asstid[0].form(str(e.chat_id), str(R.sender_id), B),
            )
        else:
            await e.reply(Asstid[1].format(str(e.chat_id), str(R.sender_id)),
            )
    else:
        await e.reply(Asstid[2].format(str(e.chat_id)))
    # end
