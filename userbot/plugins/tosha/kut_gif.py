# KutGif for icss by: @rruuurr

from .. import reply_id as rd
from . import *


@icssbot.on(icss_cmd(outgoing=True, pattern="ك1$"))
@icssbot.on(sudo_cmd(pattern="ك1$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    Ti = await rd(icss)
    if kut_gif:
        icss_caption = f"**{KUTTE}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الاولى 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif, caption=icss_caption, reply_to=Ti
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ك2$"))
@icssbot.on(sudo_cmd(pattern="ك2$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    th = await rd(icss)
    if kut_gif2:
        icss_caption = f"**{KUTTE}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الثانيه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif2, caption=icss_caption, reply_to=th
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ك3$"))
@icssbot.on(sudo_cmd(pattern="ك3$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    kh = await rd(icss)
    if kut_gif3:
        icss_caption = f"**{KUTTE}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**↫ المتـحركه الثالثه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif3, caption=icss_caption, reply_to=kh
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ك4$"))
@icssbot.on(sudo_cmd(pattern="ك4$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    wh = await rd(icss)
    if kut_gif4:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه الرابعه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif4, caption=kutc, reply_to=wh
        )

@icssbot.on(icss_cmd(outgoing=True, pattern="ك5$"))
@icssbot.on(sudo_cmd(pattern="ك5$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    ih = await rd(icss)
    if kut_gif5:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه الخامسه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif5, caption=kutc, reply_to=ih
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ك6$"))
@icssbot.on(sudo_cmd(pattern="ك6$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    uh = await rd(icss)
    if kut_gif6:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه السادسه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif6, caption=kutc, reply_to=uh
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ك7$"))
@icssbot.on(sudo_cmd(pattern="ك7$", allow_sudo=True))
async def kutgif(icss):
    if icss.fwd_from:
        return
    oh = await rd(icss)
    if kut_gif7:
        kutc = f"**{KUTTE}**\n"
        kutc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kutc += f"**↫ المتـحركه السابعه 𓆰.**"
        await icss.client.send_file(
            icss.chat_id, kut_gif7, caption=kutc, reply_to=oh
        )

