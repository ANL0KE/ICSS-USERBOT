"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif 2
"""

from .. import reply_id
from . import *

@icssbot.on(
    admin_cmd(
       outgoing=True, pattern="ت2$"
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="ت2$", allow_sudo=True
    )
)
async def tmgif(lon):
    if lon.fwd_from:
        return
    lonid = await reply_id(lon)
    if tm_gif2:
        ics_c = f"**{TMTE}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه الثانيه 𓆰.**"
        await lon.client.send_file(lon.chat_id, tm_gif2, caption=ics_c, reply_to=lonid)
