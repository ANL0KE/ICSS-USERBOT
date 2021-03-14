import time

from . import StartTime, get_readable_time, reply_id

DEFAULTUSER = "ICSS"
CAT_IMG = "https://telegra.ph/file/787f0c1d759a8b4faa0fc.mp4"
CUSTOM_ICSS_TEXT = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑼𝑻𝑬 𝑮𝑰𝑭 𓆪"
EMOJI = "  ↫ "


@icssbot.on(admin_cmd(outgoing=True, pattern="ك7$"))
@icssbot.on(sudo_cmd(pattern="ك7$", allow_sudo=True))
async def amireallyalive(icss):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(icss)
    await get_readable_time((time.time() - StartTime))
    if CAT_IMG:
        cat_caption = f"**{CUSTOM_ICSS_TEXT}**\n"
        cat_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        cat_caption += f"**↫ المتـحركه السابعه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, CAT_IMG, caption=cat_caption, reply_to=reply_to_id
        )
        await icss.delete()
    else:
        await edit_or_reply(
            icss,
            f"**{CUSTOM_ICSS_TEXT}**\n"
            f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
            f"**↫ المتـحركه السابعه 𓆰.**",
        )
