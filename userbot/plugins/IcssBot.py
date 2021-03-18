# Icss - Userbot
# Owner - @rruuurr

from . import mention


@icssbot.on(admin_cmd(pattern="repo$"))
@icssbot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def icsrepo(icsp):
    await edit_or_reply(
        icsp,
        f"⌔∮ 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑹𝑬𝑷𝑶 𓆪 \n"
        f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        f"- 𝑺𝑶𝑼𝑹𝑪𝑬 𝑫𝑬𝑽 ⪼ [𝑪𝑳𝑰𝑪𝑲 𝑯𝑬𝑹𝑬](t.me/rruuurr)\n"
        f"- 𝑺𝑶𝑼𝑹𝑪𝑬 𝑹𝑬𝑷𝑶 ⪼ [𝑪𝑳𝑰𝑪𝑲 𝑯𝑬𝑹𝑬](https://github.com/ANL0KE/ICSS)\n",
    )

@icssbot.on(admin_cmd(pattern="رابط السورس$"))
@icssbot.on(sudo_cmd(pattern="رابط السورس$", allow_sudo=True))
async def icsrepo(icsp):
    await edit_or_reply(
        icsp,
        f"⌔∮ عزيزي {mention} ⇱\n"
        f"⌔∮ رابط سورس اكسس ↫ [هنا](https://github.com/ANL0KE/ICSS) ⇲",
    )
