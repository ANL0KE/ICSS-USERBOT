from . import ALIVE_NAME, BOT_USERNAME, mention

DEFULTUSER = ALIVE_NAME or "ICSS"


@icssbot.on(admin_cmd(pattern="هها"))
async def icss(hehe):
    await edit_or_reply(
        hehe, Hi
        f"⌔∮ 𝑰𝑪𝑺𝑺 𝑯𝑨𝑺 𝑫𝑬𝑷𝑳𝑶𝒀𝑬𝑫\n"
        f"➖➖➖➖➖➖➖➖➖\n"
        f"- 𝑼𝒔𝒆𝒓𝑵𝒂𝒎𝒆 : {mention}\n"
        f"- 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 : {BOT_USERNAME}\n"
        f"➖➖➖➖➖➖➖➖➖\n"
        f"- 𝑺𝒖𝒑𝒑𝒐𝒓𝒕: @rruuurr\n"
        f"➖➖➖➖➖➖➖➖➖",
    )
