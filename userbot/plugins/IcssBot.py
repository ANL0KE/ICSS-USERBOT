from . import ALIVE_NAME

Tg = Config.TG_BOT_USERNAME
IC = ALIVE_NAME
DF = IC if IC else "Icss User"


@icssbot.on(admin_cmd(pattern="هها"))
async def icss(dev):
    await dev.edit(
        "⌔∮ 𝑰𝑪𝑺𝑺 𝑯𝑨𝑺 𝑩𝑬𝑵 DEPLOYED\n"
        "➖➖➖➖➖➖➖➖➖\n"
        "- مستخدم اكسس : {IC}\n"
        "- البوت الخاص بك : {Tg}\n"
        "➖➖➖➖➖➖➖➖➖\n"
        "- مطور السورس : @rruuurr\n"
        "➖➖➖➖➖➖➖➖➖"
    )
