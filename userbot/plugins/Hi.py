# Hi

from .ALIVE_NAME import mention

DEFULTUSER = ALIVE_NAME or "ICSS"
TG_BOT = Config.TG_BOT_USERNAME


@icssbot.on(admin_cmd(pattern="هها"))
async def icss(dev):
    await edit_or_reply(
        dev,
        "⌔∮ 𝑰𝑪𝑺𝑺 𝑯𝑨𝑺 𝑫𝑬𝑷𝑳𝑶𝒀𝑬𝑫\n",
        "➖➖➖➖➖➖➖➖➖\n",
        "- 𝑼𝒔𝒆𝒓𝑵𝒂𝒎𝒆 : {mention}\n",
        "- 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 : {TG_BOT}\n",
        "➖➖➖➖➖➖➖➖➖\n",
        "- 𝑺𝒖𝒑𝒑𝒐𝒓𝒕: @rruuurr\n",
        "➖➖➖➖➖➖➖➖➖",
    )
