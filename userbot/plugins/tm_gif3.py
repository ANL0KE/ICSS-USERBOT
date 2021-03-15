"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 7
"""

from . import reply_id

ICS_IMG = "https://telegra.ph/file/ecf8aa1a881954a9ed196.mp4"
ICSS_TEXT = "𓆩𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑻𝑼𝑴𝑩𝑳𝑹 𝑮𝑰𝑭𓆪"


@icssbot.on(admin_cmd(outgoing=True, pattern="ت3$"))
@icssbot.on(sudo_cmd(pattern="ت3$", allow_sudo=True))
async def tmgif(i):
    if i.fwd_from:
        return
    sic_id = await reply_id(i)
    if ICS_IMG:
        ics_c = f"**{CUSTOM_ICSS_TEXT}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه الثالثه 𓆰.**"
        await i.client.send_file(
            i.chat_id, ICS_IMG, caption=ics_c, reply_to=sic_id
        )
        await i.delete()
    else:
        await edit_or_reply(
            i,
            f"**{CUSTOM_ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الثالثه 𓆰.**",
        )
