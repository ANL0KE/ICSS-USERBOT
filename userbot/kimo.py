# Hey Ther

from . import *
from .Config import Config

ICSI = bot.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ICSN = Config.ALIVE_NAME
ICSD = str(ICSN) if ICSN else "Icss Userbot"
ICSB = Config.TG_BOT_USERNAME
ICSE = "@rruuurr"
ICSM = f"[{ICSD}](tg://user?id={ICSI})"
