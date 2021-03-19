"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 7
"""

from . import reply_id
from .IcssGif import *

@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ت7$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ت7$", allow_sudo=True
    )
)
async def tmgif(ics):
    if ics.fwd_from:
        return
    reply_to_id = await reply_id(ics)
    if tm_gif7:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه السابعه 𓆰.**"
        await ics.client.send_file(
            ics.chat_id, tm_gif7, caption=tumc, reply_to=reply_to_id
        )
