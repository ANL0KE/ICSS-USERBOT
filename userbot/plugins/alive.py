"""
©icss - @rruuurr
  - Alive Code For Icss
  - Commend: .السورس
  - Commend: .البوت
"""


import time
from platform import python_version
from telethon import version
from userbot.kimo import *

from . import ALIVE_NAME, StartTime, get_readable_time, icsv, mention
from . import reply_id as rd

DEFAULTUSER = ALIVE_NAME or "ICSS"
ICSS_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/499596b18292c0e43ac56.jpg"
ICSS_TEXT = Config.CUSTOM_ALIVE_TEXT or "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪"
ICSEM = Config.CUSTOM_ALIVE_EMOJI or "  ⌔∮ "


@icssbot.on(admin_cmd(outgoing=True, pattern="السورس$"))
@icssbot.on(sudo_cmd(pattern="السورس$", allow_sudo=True))
async def ica(icss):
    if icss.fwd_from:
        return
    ics_id = await rd(icss)
    icsupt = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if ICSS_IMG:
        ics_c = f"**{ICSS_TEXT}**\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 \n"
        ics_c += f"**{ICSEM} قاعدة البيانات ↫** `{check_sgnirts}`\n"
        ics_c += f"**{ICSEM} اصدار التليثون  ↫** `{version.__version__}\n`"
        ics_c += f"**{ICSEM} اصدار اڪسس ↫** `{icsv}`\n"
        ics_c += f"**{ICSEM} اصدار البايثون ↫** `{python_version()}\n`"
        #        ics_c += f"**{ICSEM} مدة التشغيل ↫** `{icsupt}\n`"
        ics_c += f"**{ICSEM} المستخدم ↫** {mention}\n"
        ics_c += f"**{ICSEM} مطور السورس ↫** [اضغط هنا](t.me/rruuurr) 𓆰.\n"
        ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        await icss.client.send_file(
            icss.chat_id, ICSS_IMG, caption=ics_c, reply_to=ics_id
        )
        await icss.delete()
    else:
        await eor(
            icss,
            f"**{ICSS_TEXT}**\n\n"
            f"**{ICSEM} قاعدة البيانات ↫**  `{check_sgnirts}`\n"
            f"**{ICSEM} اصدار التليثون  ↫** `{version.__version__}\n`"
            f"**{ICSEM} اصدار اڪسس ↫** `{icsv}`\n"
            f"**{ICSEM} اصدار البايثون  ↫** `{python_version()}\n`"
            f"**{ICSEM} مدة التشغيل ↫** `{icsupt}\n`"
            f"**{ICSEM} المستخدم ↫** {mention}\n",
        )


@bot.on(admin_cmd(outgoing=True, pattern="البوت$"))
@bot.on(sudo_cmd(pattern="البوت$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    icsbot = Config.TG_BOT_USERNAME
    icsi = await rd(alive)
    ics_caption = f"**⌔∮ بوت اكسس يعمل بنجاح - {ICSB}**\n"
    ics_caption += f"**  - اصدار التليثون :** `{version.__version__}\n`"
    ics_caption += f"**  - اصدار اكسس :** `{icsv}`\n"
    ics_caption += f"**  - اصدار البايثون :** `{python_version()}\n`"
    ics_caption += f"**  - المستخدم :** {mention}\n"
    results = await bot.inline_query(icsbot, ics_caption)  # pylint:disable=E0602
    await results[0].click(alive.chat_id, reply_to=icsi, hide_via=True)
    await alive.delete()



def check_data_base_heal_th():
    is_database_working = False
    output = "لم يتم تعيين قاعدة بيانات"
    if not Config.DB_URI:
        return is_database_working, output
    from userbot.plugins.sql_helper import SESSION

    try:
        SESSION.execute("SELECT 1")
    except Exception as e:
        output = f"❌ {str(e)}"
        is_database_working = False
    else:
        output = "تعمل بنجاح"
        is_database_working = True
    return is_database_working, output


CMD_HELP.update(
    {
        "alive": "**Plugin :** `alive`\
      \n\n  •  **Syntax : **`.السووس` \
      \n  •  **Function : **لعرض معلومات السورس\
      \n\n  •  **Syntax : **`.البوت` \
      \n  •  **Function : **لعرض معلومات البوت.__\
      \nقم باضافه `ALIVE_PIC` var لعرض الصوره او الفيديو عند كتابتك لامر السورس"
    }
)
