import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "ICSS"
CAT_IMG = "https://telegra.ph/file/dccf11fffd3abda4a4f29.mp4"
CUSTOM_ICSS_TEXT = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑼𝑻𝑬 𝑮𝑰𝑭 𓆪"
EMOJI = "  ↫ "


@icssbot.on(admin_cmd(outgoing=True, pattern="ك4$"))
@icssbot.on(sudo_cmd(pattern="ك4$", allow_sudo=True))
async def amireallyalive(icss):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)
    await get_readable_time((time.time() - StartTime))
    if ICSS_IMG:
        icss_caption = f"**{CUSTOM_ICSS_TEXT}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الرابعه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, CAT_IMG=ICSS_IMG, caption=icss_caption, reply_to=reply_to_id
        )
        await icss.delete()
    else:
        await edit_or_reply(
            icss,
            f"**{CUSTOM_ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه الرابعه 𓆰.**",
        )
