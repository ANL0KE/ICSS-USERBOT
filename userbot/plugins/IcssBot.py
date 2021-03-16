from . import ICSS_NAME, mention


Tg = Config.TG_BOT_USERNAME
IC = ICSS_NAME
DF = ICSS_NAME if ICSS_NAME else "Icss User"


@icssbot.on(admin_cmd(pattern="هها"))
async def icss(dev):
    await dev.edit(
        "⌔∮ 𝑰𝑪𝑺𝑺 𝑯𝑨𝑺 𝑩𝑬𝑵 DEPLOYED\n"
        "➖➖➖➖➖➖➖➖➖\n"
        "- مستخدم اكسس : {mention}\n" 
        "- البوت الخاص بك : {Tg}\n" 
        "➖➖➖➖➖➖➖➖➖\n"
        "- مطور السورس : @rruuurr\n"
        "➖➖➖➖➖➖➖➖➖"
    )

