from . import bot
from .Config import Config

ICSI = Config.OWNER_ID or bot.uid
ICSN = Config.ALIVE_NAME
ICSD = str(ICSN) if ICSN else "Icss Userbot"
ICSB = Config.TG_BOT_USERNAME
DEV = "@rruuurr"
icsme = f"[{ICSD}](tg://user?id={ICSI})"
