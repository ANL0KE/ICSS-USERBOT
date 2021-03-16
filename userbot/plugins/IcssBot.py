# Icss - Userbot


from . import mention


@icssbot.on(admin_cmd(pattern="repo$"))
@icssbot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def icsrepo(icsp):
    await edit_or_reply(
        icsp,
        f" 𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪 \n"
        f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        f"⌔∮ UserName :- {mention}\n"
        f"⌔∮ Source Dev :- [Click Here](t.me/rruuurr)\n"
        f"⌔∮ Repo :- [Click Here](https://github.com/ANL0KE/ICSS)\n",
    )
