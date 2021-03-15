"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 7
"""

from . import reply_id

ICS_IMG = "https://telegra.ph/file/7fa9b1905df5840c7c77a.mp4"
ICSS_TEXT = "𓆩𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑻𝑼𝑴𝑩𝑳𝑹 𝑮𝑰𝑭𓆪"


@icssbot.on(admin_cmd(outgoing=True, pattern="ت6$"))
@icssbot.on(sudo_cmd(pattern="ت6$", allow_sudo=True))
async def tmgif(kimo):
    if kimo.fwd_from:
        return
    reply_to_id = await reply_id(kimo)
    if ICS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه السادسه 𓆰.**"
        await kimo.client.send_file(
            kimo.chat_id, ICS_IMG, caption=ics_c, reply_to=reply_to_id
        )
        await kimo.delete()
    else:
        await edit_or_reply(
            kimo,
            f"**{ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه السادسه 𓆰.**",
        )
