# alive - ©icss

import time
from platform import python_version

from telethon import version

from . import ALIVE_NAME, StartTime, get_readable_time, icssversion, mention, reply_id

DEFAULTUSER = ALIVE_NAME or "ICSS"
ICSS_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/499596b18292c0e43ac56.jpg"
ICSS_TEXT = Config.CUSTOM_ALIVE_TEXT or "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪"
E_ICSS = Config.CUSTOM_ALIVE_EMOJI or "  - ❝ ⌊ "


@icssbot.on(admin_cmd(outgoing=True, pattern="السورس$"))
@icssbot.on(sudo_cmd(pattern="السورس$", allow_sudo=True))
async def icssalive(icss):
    if icss.fwd_from:
        return
    reply_to_id = await reply_id(icss)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    if ICSS_IMG:
        icss_caption = f"**{ICSS_TEXT}**\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        icss_caption += f"**{E_ICSS} قاعدة البيانات ↫** `{check_sgnirts}`\n"
        icss_caption += f"**{E_ICSS} اصدار التليثون  ↫** `{version.__version__}\n`"
        icss_caption += f"**{E_ICSS} اصدار اڪسس ↫** `{icssversion}`\n"
        icss_caption += f"**{E_ICSS} اصدار البايثون ↫** `{python_version()}\n`"
        #        icss_caption += f"**{EMOJI} مدة التشغيل ↫** `{uptime}\n`"
        icss_caption += f"**{E_ICSS} المستخدم ↫** {mention}\n"
        icss_caption += f"**{E_ICSS} مطور السورس ↫** [اضغط هنا](t.me/rruuurr) 𓆰.\n"
        icss_caption += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𝐢𝐜𝐬𝐬ⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        await icss.client.send_file(
            icss.chat_id, ICSS_IMG, caption=icss_caption, reply_to=reply_to_id
        )
        await icss.delete()
    else:
        await edit_or_reply(
            icss,
            f"**{ICSS_TEXT}**\n\n"
            f"**{E_ICSS} قاعدة البيانات ↫**  `{check_sgnirts}`\n"
            f"**{E_ICSS} اصدار التليثون  ↫** `{version.__version__}\n`"
            f"**{E_ICSS} اصدار اڪسس ↫** `{icssversion}`\n"
            f"**{E_ICSS} اصدار البايثون  ↫** `{python_version()}\n`"
            f"**{E_ICSS} مدة التشغيل ↫** `{uptime}\n`"
            f"**{E_ICSS} المستخدم ↫** {mention}\n",
        )


@icssbot.on(admin_cmd(outgoing=True, pattern="البوت$"))
@icssbot.on(sudo_cmd(pattern="البوت$", allow_sudo=True))
async def icssalive(icss):
    if icss.fwd_from:
        return
    tgbotusername = Config.TG_BOT_USERNAME
    reply_to_id = await reply_id(icss)
    icss_caption = f"𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪\n"
    icss_caption += f"**  - اصدار التليثون ↫** `{version.__version__}\n`"
    icss_caption += f"**  - اصدار اكسس ↫** `{icssversion}`\n"
    icss_caption += f"**  - اصدار البايثون ↫** `{python_version()}\n`"
    icss_caption += f"**  - المستخدم ↫** {mention}\n"
    results = await bot.inline_query(
        tgbotusername, icss_caption
    )  # pylint:disable=E0602
    await results[0].click(icss.chat_id, reply_to=reply_to_id, hide_via=True)
    await icss.delete()


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
