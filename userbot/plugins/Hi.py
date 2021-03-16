from . import mention


@icssbot.on(admin_cmd(pattern="هها"))
async def icss(dev):
    await dev.edit(
        "⌔∮ 𝑰𝑪𝑺𝑺 𝑯𝑨𝑺 𝑫𝑬𝑷𝑳𝑶𝒀𝑬𝑫\n"
        "➖➖➖➖➖➖➖➖➖\n"
        "- 𝑼𝒔𝒆𝒓𝑵𝒂𝒎𝒆 : {mention}\n"
        "- 𝑨𝒔𝒔𝒊𝒔𝒕𝒂𝒏𝒕 : {Config.TG_BOT_USERNAME}\n" 
        "➖➖➖➖➖➖➖➖➖\n"
        "- 𝑺𝒖𝒑𝒑𝒐𝒓𝒕: @rruuurr\n"
        "➖➖➖➖➖➖➖➖➖"
    )
