"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 7
"""

from . import reply_id

ICSS_IMG = "https://telegra.ph/file/6efa916e79bdf7fe3fba4.mp4"
ICSS_TEXT = "𓆩𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑻𝑼𝑴𝑩𝑳𝑹 𝑮𝑰𝑭𓆪"


@icssbot.on(admin_cmd(outgoing=True, pattern="ت7$"))
@icssbot.on(sudo_cmd(pattern="ت7$", allow_sudo=True))
async def tmgif(ics):
    if ics.fwd_from:
        return
    reply_to_id = await reply_id(ics)
    if ICSS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه السابعه 𓆰.**"
        await ics.client.send_file(
            ics.chat_id, ICSS_IMG, caption=ics_c, reply_to=reply_to_id
        )
        await ics.delete()
    else:
        await edit_or_reply(
            ics,
            f"**{ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه السابعه 𓆰.**",
        )
