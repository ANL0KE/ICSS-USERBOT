from .Config import Config

USERID = Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Icss Userbot"
ICSBOT = Config.TG_BOT_USERNAME
DEV = "@rruuurr"
icsme = f"[{DEFAULTUSER}](tg://user?id={USERID})"
