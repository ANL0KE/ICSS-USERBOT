#    IcssBot - UserBot
#    (c) @rruuurr


from userbot.Config import Config

@icssbot.on(icss_cmd(pattern="م22"))
async def wspr(kimo):
    await kimo.edit(
        "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑬𝑵𝑫𝑺 𓆪\n"
        "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        "**⌔∮ قائـمه اوامر الالعاب :** \n"
        "⪼ `.اكس او` \n"
        "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
    )

@icssbot.on(
    icss_cmd(
       pattern="اكس او$"
    )
)

async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
