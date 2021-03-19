"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 6
"""

from . import reply_id
from .IcssGif import *


@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ت6$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ت6$", allow_sudo=True
    )
)
async def tmgif(kimo):
    if kimo.fwd_from:
        return
    reply_to_id = await reply_id(kimo)
    if tm_gif6:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه السادسه 𓆰.**"
        await kimo.client.send_file(
            kimo.chat_id, tm_gif6, caption=tumc, reply_to=reply_to_id
        )
