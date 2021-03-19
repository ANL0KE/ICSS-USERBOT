"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 3
"""

from . import reply_id
from .IcssGif import *

@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ت3$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ت3$", allow_sudo=True
    )
)
async def tmgif(i):
    if i.fwd_from:
        return
    sic_id = await reply_id(i)
    if tm_gif3:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الثالثه 𓆰.**"
        await i.client.send_file(i.chat_id, tm_gif3, caption=tumc, reply_to=sic_id)
