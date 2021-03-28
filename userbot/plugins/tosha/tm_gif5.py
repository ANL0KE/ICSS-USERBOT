"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 5
"""

from .. import reply_id
from . import *

@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ت5$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ت5$", allow_sudo=True
    )
)
async def tmgif(tosh):
    if tosh.fwd_from:
        return
    reply_to_id = await reply_id(tosh)
    if tm_gif5:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الخامسه 𓆰.**"
        await tosh.client.send_file(
            tosh.chat_id, tm_gif5, caption=tumc, reply_to=reply_to_id
        )
