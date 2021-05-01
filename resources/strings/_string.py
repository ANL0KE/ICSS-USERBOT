#   icss - UserBot
#  kimo: 
#     - strings for Icss - Userbot

from userbot.Config import Config # Ok - 🖤 

USERID = Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Icss Userbot"
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"

Plugin = "userbot/plugins/{}.py"
Admin = "userbot/plugins/Admin/{}.py"
Animation = "userbot/plugins/animations/{}.py"
Tosh = "userbot/plugins/tosha/{}.py"
Assistant = "userbot/plugins/assistant/{}.py"
AssistantPm = "userbot/plugins/assistant/PmTosh/{}.py"

Xtbot = "\"TG_BOT_TOKEN\""
Xt = "TG_BOT_TOKEN"
Xe = "STRING_SESSION"

A = Config.APP_ID
H = Config.API_HASH
B = Config.TG_BOT_TOKEN
N = Config.NO_LOAD

Start = (
    """
    <------------------------------------>
         يتم تحميل ملفات السورس اكسس
    <------------------------------------>
    """
)

TOSHA = Config.PRIVATE_GROUP_BOT_API_ID
TBOT = Config.TG_BOT_USERNAME
T = Config.COMMAND_HAND_LER or "."
DEVL = "@rruuurr"

C = "**⌔∮ المعادله ⪼** {}\n  **- الحل ⪼** {}"
Calc = (
    "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑨𝑳𝑪𝑼𝑳𝑨𝑻𝑶𝑹 𓆪\n"
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    "**⌔∮ قائـمه اوامر الحاسبه :** \n"
    "⪼ `.حاسبه` + المعادله \n"
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
)

kk = [
   "╭━━━╮\n┃╭━━╯\n┃╰━━╮\n┃╭━━╯\n┃┃\n╰╯",
   "┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛"
]

urs = "**⌔∮ نسبة نجاحك هيه -** {}"
Fl = [
   "+100% 🔱🖤", "100% 🖤", "95%", "90%","85%", "80%", "75%", "70%", "65%", "60%", "55%", 
   "50%", "45%", "40%", "35%", "30%", "25%", "20%", "15%", "10%", "0%", "-0%"
]

MSGE = (
   f"𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ المستخدم -** {mention}\n**⌔∮ البوت - {TBOT}**\n**⌔∮ للمساعده - {DEVL}**\n**اكتب {T}بنك لتحقق اذا ما كان البوت يعمل**"
)

Tlk = " تم استرداد ⫸"
IS = "⫷ لايمكن تحميل - {} بسبب {} ⫸"

#- TOSH is the most beautiful girl in the world -#
ICSJ = "<ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ>"
StartLoaded = "<ⵧⵧⵧⵧⵧⵧ⫷ - ICSS PLUGINS - ⫸ⵧⵧⵧⵧⵧⵧ>"
ASSISTANT = "<ⵧⵧⵧⵧⵧⵧ⫷ - ICSS ASSISTANT - ⫸ⵧⵧⵧⵧⵧⵧ>"
KIMOTOSHA = "<ⵧⵧⵧⵧⵧⵧⵧⵧ⫷ - ICSS TOSHA - ⫸ⵧⵧⵧⵧⵧⵧⵧ>"
ANIMATIONS = "<ⵧⵧⵧⵧⵧⵧ⫷ - ICSS ANIMATIONS - ⫸ⵧⵧⵧⵧⵧ>"
ADMIN = "<ⵧⵧⵧⵧⵧ⫷ - ICSS ADMIN TOOLS - ⫸ⵧⵧⵧⵧⵧ>"
ASSISTANTPM = "<ⵧⵧⵧⵧⵧ⫷ - ICSS ASSISTANT PM - ⫸ⵧⵧⵧⵧⵧ>"
ICSW = "<ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ>"
# --- MESSI IS THE BEST PLAYER IN THE WORLD --- #

Plg = "userbot/plugins/*.py"
Adm = "userbot/plugins/Admin/*.py"
Inm = "userbot/plugins/animations/*.py"
Tsh = "userbot/plugins/tosha/*.py"
Ast = "userbot/plugins/assistant/*.py"
Pmt = "userbot/plugins/assistant/PmTosh/*.py"

Message = (
"""       ⫷ بوت اكسس يعمل بنجاح الان ⫸
   ⫷ المستخدم: {} - البوت: {} ⫸
⫷ @rruuurr - اذا كنت بحاجه الى مساعده فتوجه الى ⫸"""
)

Mesg = [
    '⫷ يتم تحميل انلاين اكسس ⫸',
    '⫷ اكتمل تنزيل انلاين اكسس بدون اخطاء ⫸',
    '⫷ يتم بدء بوت اكسس ⫸',
    '⫷ اكتمل بدء بوت اكسس ⫸'
]

Cmds = "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ اهلاً بك عزيزي اختر الاوامر الاتيه :** \n ⪼ اوامر الادمن ~ م1 \n ⪼ اوامر التسليه ~ م2\n ⪼ اوامر الترحيب ~ م3\n ⪼ اوامر الردود ~ م4\n ⪼ اوامر الرفع ~ م5\n ⪼ اوامر الحمايه ~ م6\n ⪼ اوامر التلكراف ~ م7\n ⪼ اوامر الملصقات ~ م8\n ⪼ اوامر التاك ~ م9\n ⪼ اوامر الكشف ~ م10\n ⪼ اوامر المجموعه ~ م11\n ⪼ اوامر الترجمه ~ م12\n ⪼ اوامر البحث ~ م13\n ⪼ اوامر الانتحال ~ 14\n ⪼ اوامر النت ~ م15\n ⪼ اوامر البوت ~ م16\n ⪼ اوامر الحساب ~ م17\n ⪼ اوامر السورس ~ م18\n ⪼ اوامر الزغـرفه ~ م19\n ⪼ اوامر المتحركات ~ م20\n ⪼ اوامر الهمسه ~ م21\n ⪼ اوامر الالعاب ~ م22\n ⪼ اوامر الحاسبه ~ م23\n ⪼ اوامر هيروكو ~ م24\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
# +======================================================+
# +======================================================+

alv = (
"""
**©icss - @rruuurr
  - Plugin Alive** 
  - **Commend:** `.السورس`
  - **Function:** لعرض معلومات السورس
"""
)

import time
from platform import python_version
from telethon import version
from resources.strings import *

from resources.Formation.plugins import ALIVE_NAME, icsv, mention
from resources.Formation.plugins import reply_id as rd

DEFAULTUSER = ALIVE_NAME or "ICSS"
ICSS_IMG = Config.ALIVE_PIC or "https://telegra.ph/file/499596b18292c0e43ac56.jpg"
ICSS_TEXT = Config.CUSTOM_ALIVE_TEXT or "𓆩 𝑾𝑬𝑳𝑪𝑶𝑴𝑬 𝑻𝑶 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𓆪"
ICSEM = Config.CUSTOM_ALIVE_EMOJI or "  ⌔∮ "

_, check_sgnirts = check_data_base_heal_th()

ics_c = f"**{ICSS_TEXT}**\n"
ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 \n"
ics_c += f"**{ICSEM} قاعدة البيانات ↫** `{check_sgnirts}`\n"
ics_c += f"**{ICSEM} اصدار التليثون  ↫** `{version.__version__}\n`"
ics_c += f"**{ICSEM} اصدار اڪسس ↫** `{icsv}`\n"
ics_c += f"**{ICSEM} اصدار البايثون ↫** `{python_version()}\n`"
ics_c += f"**{ICSEM} المستخدم ↫** {mention}\n"
ics_c += f"**{ICSEM} مطور السورس ↫** [اضغط هنا](t.me/rruuurr) 𓆰.\n"
ics_c += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        

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

# +======================================================+
# +======================================================+
