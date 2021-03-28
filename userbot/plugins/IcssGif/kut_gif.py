# KutGif for icss by: @rruuurr

from .. import reply_id
from . import *


@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ك1$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ك1$", allow_sudo=True
    )
)
async def kutgif(icss):
    if icss.fwd_from:
        return
    reply_to_id = await reply_id(icss)
    if kut_gif:
        icss_caption = f"**{KUTTE}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الاولى 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif, caption=icss_caption, reply_to=reply_to_id
        )
