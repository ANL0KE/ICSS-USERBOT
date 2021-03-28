# KutGif for icss by: @rruuurr

from .. import reply_id
from . import *

@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ك4$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ك4$", allow_sudo=True
    )
)
async def kutgif(icss):
    if icss.fwd_from:
        return
    reply_to_id = await reply_id(icss)
    if kut_gif4:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه الرابعه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif4, caption=kutc, reply_to=reply_to_id
        )
