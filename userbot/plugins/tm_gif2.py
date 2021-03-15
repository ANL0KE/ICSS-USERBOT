"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 2
"""

from . import reply_id

ICS_IMG = "https://telegra.ph/file/6e707dc14cb918cd765fb.mp4"
ICSS_TEXT = "𓆩𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑻𝑼𝑴𝑩𝑳𝑹 𝑮𝑰𝑭𓆪"


@icssbot.on(admin_cmd(outgoing=True, pattern="ت2$"))
@icssbot.on(sudo_cmd(pattern="ت2$", allow_sudo=True))
async def tmgif(lon):
    if lon.fwd_from:
        return
    lonid = await reply_id(lon)
    if ICS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه الثانيه 𓆰.**"
        await lon.client.send_file(lon.chat_id, ICS_IMG, caption=ics_c, reply_to=lonid)
        await lon.delete()
    else:
        await edit_or_reply(
            lon,
            f"**{ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الثانيه 𓆰.**",
        )
