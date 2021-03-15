"""
©icss : @rruuurr
  - Tumblr Gif
  - Tumblr Gif = 4
"""


from . import reply_id

ICS_IMG = "https://telegra.ph/file/dccf11fffd3abda4a4f29.mp4"
ICSS_TEXT = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑼𝑻𝑬 𝑮𝑰𝑭 𓆪"


@icssbot.on(admin_cmd(outgoing=True, pattern="ك4$"))
@icssbot.on(sudo_cmd(pattern="ك4$", allow_sudo=True))
async def tmgif(lon):
    if lon.fwd_from:
        return
    reply_to_id = await reply_id(lon)
    if ICS_IMG:
        ics_c = f"**{CUSTOM_ICSS_TEXT}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه الرابعه 𓆰.**"
        await lon.client.send_file(
            lon.chat_id, ICS_IMG, caption=ics_c, reply_to=reply_to_id
        )
        await lon.delete()
    else:
        await edit_or_reply(
            lon,
            f"**{CUSTOM_ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الرابعه 𓆰.**",
        )
