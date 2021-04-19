# icss - UserBot

from .Config import Config

USERID = Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Icss Userbot"
mention = f"[{DEFAULTUSER}](tg://user?id={USERID})"

Plugin = "\"userbot/plugins/{}.py\""
Admin = "\"userbot/plugins/Admin/{}.py\""
Animation = "\"userbot/plugins/animations/{}.py\""
Tosh = "\"userbot/plugins/tosha/{}.py\""
Assistant = "\"userbot/plugins/assistant/{}.py\""

Xtbot = "\"TG_BOT_TOKEN\""
Xt = "TG_BOT_TOKEN"
Xe = "STRING_SESSION"

A = Config.APP_ID
H = Config.API_HASH
B = Config.TG_BOT_TOKEN
N = Config.NO_LOAD

TOSHA = Config.PRIVATE_GROUP_BOT_API_ID
TBOT = Config.TG_BOT_USERNAME
DEVL = "@rruuurr"

MSGE = (
   f"𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑼𝑷𝑫𝑨𝑻𝑬 𝑴𝑺𝑮 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ المستخدم -** {mention}\n**⌔∮ البوت - {TBOT}**\n**⌔∮ للمساعده - {DEVL}**\n**اكتب .بنك لتحقق اذا ما كان البوت يعمل**"
)

Masg = "⫷ المستخدم: {} - البوت: {} ⫸"
IS = "⫷ لايمكن تحميل - {} بسبب {} ⫸"

#- TOSH is the most beautiful girl in the world -#
ICSJ = "<ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ>"
ASSISTANT = "<ⵧⵧⵧⵧⵧⵧ⫷ - ICSS ASSISTANT - ⫸ⵧⵧⵧⵧⵧⵧ>"
KIMOTOSHA = "<ⵧⵧⵧⵧⵧⵧⵧⵧ⫷ - ICSS TOSHA - ⫸ⵧⵧⵧⵧⵧⵧⵧ>"
ANIMATIONS = "<ⵧⵧⵧⵧⵧⵧ⫷ - ICSS ANIMATIONS - ⫸ⵧⵧⵧⵧⵧ>"
ADMIN = "<ⵧⵧⵧⵧⵧ⫷ - ICSS ADMIN TOOLS - ⫸ⵧⵧⵧⵧⵧ>"
ICSW = "<ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ>"
# --- MESSI IS THE BEST PLAYER IN THE WORLD --- #

Tlk = " تم استرداد ⫸"

Plg = "userbot/plugins/*.py"
Adm = "userbot/plugins/Admin/*.py"
Inm = "userbot/plugins/animations/*.py"
Tsh = "userbot/plugins/tosha/*.py"
Ast = "userbot/plugins/assistant/*.py"
