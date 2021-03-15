"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 5
"""

from . import reply_id

ICS_IMG = "https://telegra.ph/file/4e6d2784767f22c707883.mp4"
ICSS_TEXT = "𓆩𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑻𝑼𝑴𝑩𝑳𝑹 𝑮𝑰𝑭𓆪"


@icssbot.on(admin_cmd(outgoing=True, pattern="ت5$"))
@icssbot.on(sudo_cmd(pattern="ت5$", allow_sudo=True))
async def tmgif(tosh):
    if tosh.fwd_from:
        return
    reply_to_id = await reply_id(tosh)
    if ICS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه الخامسه 𓆰.**"
        await tosh.client.send_file(
            tosh.chat_id, ICS_IMG, caption=ics_c, reply_to=reply_to_id
        )
        await tosh.delete()
    else:
        await edit_or_reply(
            tosh,
            f"**{ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الخامسه 𓆰.**",
        )
