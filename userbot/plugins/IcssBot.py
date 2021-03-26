# Icss - Userbot
# Owner - @rruuurr

from . import mention


@icss(
    icss_cmd(
       pattern="repo$"
    )
)
@icss(
    sudo_cmd(
       pattern="repo$", allow_sudo=True
    )
)
async def icsrepo(icsp):
    await eor(
        icsp,
        f"⌔∮ 𝙎𝙊𝙐𝙍𝘾𝙀 𝙄𝘾𝙎𝙎 - 𝙍𝙀𝙋𝙊 𓆪 \n"
        f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        f"- 𝙎𝙊𝙐𝙍𝘾𝙀 𝘿𝙀𝙑 ⪼ [𝘾𝙇𝙄𝘾𝙆 𝙃𝙀𝙍𝙀](t.me/rruuurr) ⩫ \n"
        f"- 𝙎𝙊𝙐𝙍𝘾𝙀 𝙍𝙀𝙋𝙊 ⪼ [𝘾𝙇𝙄𝘾𝙆 𝙃𝙀𝙍𝙀](https://github.com/ANL0KE/ICSS) ⩫",
    )


@icss(
    icss_cmd(
       pattern="رابط السورس$"
    )
)
@icss(
    sudo_cmd(
       pattern="رابط السورس$", allow_sudo=True
    )
)
async def icsrepo(icsp):
    await eor(
        icsp,
        f"**⌔∮ عزيزي {mention} ⇱**\n"
        f"**⌔∮ رابط سورس اكسس ↫ [هنا](https://github.com/ANL0KE/ICSS) ⇲**",
    )
