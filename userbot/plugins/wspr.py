from . import reply_id as rd
from .Tosh import T
from userbot.kimo import *


WPIC = "https://telegra.ph/file/dfd7fc05a81748a87761c.jpg"


@icssbot.on(icss_cmd(pattern="م21"))
async def wspr(kimo):
    return await eor(kimo, T)


# Wespr - همسه
@icssbot.on(icss_cmd(outgoing=True, pattern="الهمسه$"))
async def kimo(lon):
    if lon.fwd_from:
        return
    ld = await rd(lon)
    if WPIC:
        ics_c = f"اذا تريد ترسل همسه من خلال البوت الخاص بك يجب كتابه اولا #معرف_البوت ثم #secret ثم تكتب #معرف_الي_تريد_تهمسله ثم #الرساله وستضهر ايقونه وتضغط عليها وبس 🖤✨.\n"
        ics_c += f"**- قم بنسخ :**\n `{ICSB} secret @NIIIN2 الرساله`"
        await lon.client.send_file(lon.chat_id, WPIC, caption=ics_c, reply_to=ld)



@bot.on(admin_cmd(pattern="همسه ?(.*)"))
async def wspr(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    bu = "@nnbbot"
    if event.reply_to_msg_id:
        reply_to_id = await event.get_reply_message()
    tap = await bot.inline_query(bu, wwwspr) 
    await tap[0].click(event.chat_id)
    await event.delete()
