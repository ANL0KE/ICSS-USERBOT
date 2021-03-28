"""
©icss : @rruuurr
  - Tumblr Gif -1
  - Tumblr Gif -2
  - Tumblr Gif -3
  - Tumblr Gif -4
  - Tumblr Gif -5
  - Tumblr Gif -6
  - Tumblr Gif -7

"""


from .. import reply_id as rd 
from . import *

@icssbot.on(icss_cmd(outgoing=True, pattern="ت1$"))
@icssbot.on(sudo_cmd(pattern="ت1$", allow_sudo=True))
async def tmgif(kim):
    if kim.fwd_from:
        return
    kimid = await rd(kim)
    if tm_gif:
        kim_c = f"**{TMTE}**\n"
        kim_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        kim_c += f"**↫ المتـحركه الاولى 𓆰.**"
        await kim.client.send_file(kim.chat_id, tm_gif, caption=kim_c, reply_to=kimid)


@icssbot.on(icss_cmd(outgoing=True, pattern="ت2$"))
@icssbot.on(sudo_cmd(pattern="ت2$", allow_sudo=True))
async def tmgif(lon):
    if lon.fwd_from:
        return
    lonid = await rd(lon)
    if tm_gif2:
        ics_c = f"**{TMTE}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        ics_c += f"**↫ المتـحركه الثانيه 𓆰.**"
        await lon.client.send_file(lon.chat_id, tm_gif2, caption=ics_c, reply_to=lonid)


@icssbot.on(icss_cmd(outgoing=True, pattern="ت3$"))
@icssbot.on(sudo_cmd(pattern="ت3$", allow_sudo=True))
async def tmgif(i):
    if i.fwd_from:
        return
    sic_id = await rd(i)
    if tm_gif3:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الثالثه 𓆰.**"
        await i.client.send_file(i.chat_id, tm_gif3, caption=tumc, reply_to=sic_id)


@icssbot.on(icss_cmd(outgoing=True, pattern="ت4$"))
@icssbot.on(sudo_cmd(pattern="ت4$", allow_sudo=True))
async def tmgif(lon):
    if lon.fwd_from:
        return
    reply_to_id = await rd(lon)
    if tm_gif4:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الرابعه 𓆰.**"
        await lon.client.send_file(
            lon.chat_id, tm_gif4, caption=tumc, reply_to=reply_to_id
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ت5$"))
@icssbot.on(sudo_cmd(pattern="ت5$", allow_sudo=True))

async def tmgif(tosh):
    if tosh.fwd_from:
        return
    reply_to_id = await rd(tosh)
    if tm_gif5:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه الخامسه 𓆰.**"
        await tosh.client.send_file(
            tosh.chat_id, tm_gif5, caption=tumc, reply_to=reply_to_id
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ت6$"))
@icssbot.on(sudo_cmd(pattern="ت6$", allow_sudo=True))

async def tmgif(kimo):
    if kimo.fwd_from:
        return
    reply_to_id = await rd(kimo)
    if tm_gif6:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه السادسه 𓆰.**"
        await kimo.client.send_file(
            kimo.chat_id, tm_gif6, caption=tumc, reply_to=reply_to_id
        )


@icssbot.on(icss_cmd(outgoing=True, pattern="ت7$"))
@icssbot.on(sudo_cmd(pattern="ت7$", allow_sudo=True))
async def tmgif(ics):
    if ics.fwd_from:
        return
    reply_to_id = await rd(ics)
    if tm_gif7:
        tumc = f"**{TMTE}**\n"
        tumc += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        tumc += f"**↫ المتـحركه السابعه 𓆰.**"
        await ics.client.send_file(
            ics.chat_id, tm_gif7, caption=tumc, reply_to=reply_to_id
        )
