#   icss - UserBot
#  kimo: 
#     - strings for Icss - Userbot

from userbot.Config import Config # Ok - 🖤 

USERID = Config.OWNER_ID
Name = Config.ALIVE_NAME
DEFAULTUSER = str(Name) if Name else "Icss Userbot"
mention = f"[{Name}](tg://user?id={USERID})"

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

Quotly = [
    '**⌔∮ اهلا -** {} **قم برد على الرساله**',
    '**⌔∮ اهلا -** {} **التنسيق غير مدعوم**',
    '**⌔∮ جاري المعـالجه….**',
    '**⌔∮ قم بالرد على الرساله او قم بوضع النص قرب الامر**',
    '**⌔∮ اهلا -** {} **خطا في بناء الامر**',
    '**⌔∮ يرجى الغاء الحظر من البوت ~** @quotlybot'
]

Cmds = "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑪𝑶𝑴𝑴𝑨𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n **⌔∮ اهلاً بك عزيزي اختر الاوامر الاتيه :** \n ⪼ اوامر الادمن ~ م1 \n ⪼ اوامر التسليه ~ م2\n ⪼ اوامر الترحيب ~ م3\n ⪼ اوامر الردود ~ م4\n ⪼ اوامر الرفع ~ م5\n ⪼ اوامر الحمايه ~ م6\n ⪼ اوامر التلكراف ~ م7\n ⪼ اوامر الملصقات ~ م8\n ⪼ اوامر التاك ~ م9\n ⪼ اوامر الكشف ~ م10\n ⪼ اوامر المجموعه ~ م11\n ⪼ اوامر الترجمه ~ م12\n ⪼ اوامر البحث ~ م13\n ⪼ اوامر الانتحال ~ 14\n ⪼ اوامر النت ~ م15\n ⪼ اوامر البوت ~ م16\n ⪼ اوامر الحساب ~ م17\n ⪼ اوامر السورس ~ م18\n ⪼ اوامر الزغـرفه ~ م19\n ⪼ اوامر المتحركات ~ م20\n ⪼ اوامر الهمسه ~ م21\n ⪼ اوامر الالعاب ~ م22\n ⪼ اوامر الحاسبه ~ م23\n ⪼ اوامر هيروكو ~ م24\n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n 𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"

# Help String - Text when u type .help!
HelpString = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑯𝑬𝑳𝑷𝑬𝑹 𝑳𝑰𝑺𝑻 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ اهلا بك عزيزي {} في قائمه الانلاين:**\n\n**⪼ استخدم** `.help plugin name`\n**لاضهار الاوامر بدون الاستخدام.**\n\n**⪼ استخدم** `.info plugin name`\n**لاضهار الاوامر وطريقه استخدامها وفوائدها**"

# For Dev:
Devt = "𓄂╺  𝑫𝑬𝑽 𝑼𝑺𝑬𝑹\n╰──► {} ༗".format(DEVL)

# For Echo - EchoText:
Echo = [
    '**⌔∮ اهلا -** {}\n**⌔∮ انه موجود بلفعل في قائمه الازعاج**',
    '**⌔∮ هها هلو 🤍🎧 ،**',
    '**⌔∮ اهلا -** {} \n**⌔∮ قم برد على الرساله لكي تتم اضافته الى قائمه الازعاج**',
    '**⌔∮ اهلا -** {} \n**⌔∮ تم ايقاف امر الازعاج**',
    '**⌔∮ اهلا -** {} \n**⌔∮ هذا المستخدم غير مضاف الى قائمه الازعاج**',
    '𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑬𝑪𝑯𝑶 𝑳𝑰𝑺𝑻 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ قائمة المضافين للازعاج:**\n',
    '**- ايدي المستخدم :** `{}`\n**- ايدي الـمجموعه :** `{}`\n\n',
    '**⌔∮ اهلا - {} \n**⌔∮ لم تقم باضافه احد للقائمه**'
]
