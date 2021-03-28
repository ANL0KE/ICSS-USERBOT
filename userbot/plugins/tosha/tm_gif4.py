"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 4
"""


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
async def tmgif(lon):
    if lon.fwd_from:
        return
    reply_to_id = await reply_id(lon)
    if tm_gif4:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الرابعه 𓆰.**"
        await lon.client.send_file(
            lon.chat_id, tm_gif4, caption=tumc, reply_to=reply_to_id
        )
