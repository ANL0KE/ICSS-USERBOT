import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "ICSS"
ICSS_IMG = "https://telegra.ph/file/78185fe07950955f07e74.mp4"
CUSTOM_ICSS_TEXT = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑼𝑻𝑬 𝑮𝑰𝑭 𓆪"
EMOJI = "  ↫ "


@icssbot.on(admin_cmd(outgoing=True, pattern="ك3$"))
@icssbot.on(sudo_cmd(pattern="ك3$", allow_sudo=True))
async def kutgif(icss):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(icss)
    await get_readable_time((time.time() - StartTime))
    if ICSS_IMG:
        icss_caption = f"**{CUSTOM_ICSS_TEXT}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الثالثه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, CAT_IMG=ICSS_IMG, caption=icss_caption, reply_to=reply_to_id
        )
        await icss.delete()
    else:
        await edit_or_reply(
            icss,
            f"**{CUSTOM_ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الثالثه 𓆰.**",
        )
