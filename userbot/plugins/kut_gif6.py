# KutGif for icss by: @rruuurr

from . import reply_id
from .IcssGif import *

@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ك6$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ك6$", allow_sudo=True
    )
)
async def kutgif(icss):
    if icss.fwd_from:
        return
    reply_to_id = await reply_id(icss)
    if kut_gif6:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه السادسه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif6, caption=kutc, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            icss,
            f"**{KUTTE}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه السادسه 𓆰.**",
        )
