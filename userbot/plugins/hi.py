from . import ALIVE_NAME, mention, BOT_USERNAME

DEFULTUSER = ALIVE_NAME or "ICSS"

Hi = (
    f"⌔∮ 𝑰𝑪𝑺𝑺 𝑯𝑨𝑺 𝑫𝑬𝑷𝑳𝑶𝒀𝑬𝑫\n"
    f"➖➖➖➖➖➖➖➖➖\n"
    f"- 𝑼𝒔𝒆𝒓𝑵𝒂𝒎𝒆 : {mention}\n"
    f"- 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 : {BOT_USERNAME}\n"
    f"➖➖➖➖➖➖➖➖➖\n"
    f"- 𝑺𝒖𝒑𝒑𝒐𝒓𝒕: @rruuurr\n"
    f"➖➖➖➖➖➖➖➖➖"
)


@icssbot.on(admin_cmd(pattern="هها"))
async def icss(dev):
    await div.edit(Hi)
