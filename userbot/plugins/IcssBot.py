# Icss - Userbot


ICSR = (
    " 𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪 \n",
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n",
    "⌔∮ UserName :- {mention}\n",
    "⌔∮ Source Dev :- [Click Here](t.me/rruuurr)\n",
    "⌔∮ Repo :- [Click Here](https://github.com/ANL0KE/ICSS)\n",
)


@icssbot.on(admin_cmd(pattern="repo (.*)"))
@icssbot.on(sudo_cmd(pattern="repo (.*)", allow_sudo=True))
async def icsrepo(icsp):
    await edit_or_reply(icsp, "{ICSR}")
