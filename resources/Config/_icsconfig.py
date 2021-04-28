#    ICSS - USERBOT
#    CONFIGS - VARS

import os
from telethon.tl.types import ChatBannedRights


class Config(object):
    LOGGER = True

    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    DB_URI = os.environ.get("DATABASE_URL", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") or os.environ.get(
        "TG_BOT_TOKEN_BF_HER", None
    )
    TG_BOT_USERNAME = os.environ.get("TG_BOT_USERNAME") or os.environ.get(
        "TG_BOT_USER_NAME_BF_HER", None
    )
    LOAD_MYBOT = os.environ.get("LOAD_MYBOT", "True")
    TOSH_START = os.environ.get("TOSH_START", None)
    TZ = os.environ.get("TZ", "Asia/Baghdad")
    UPSTREAM_REPO = os.environ.get(
        "UPSTREAM_REPO", "https://github.com/ANL0KE/ICSS-USERBOT.git"
    )

    AUTONAME = os.environ.get("AUTONAME", None)
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID") or 0)
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID") or 0)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    MAX_FLOOD_IN_PMS = int(os.environ.get("MAX_FLOOD_IN_PMS", 5))
    PM_LOGGER_GROUP_ID = int(
        os.environ.get("PM_LOGGER_GROUP_ID")
        or os.environ.get("PM_LOGGR_BOT_API_ID")
        or 0
    )
    SUDO_USERS = {int(x) for x in os.environ.get("SUDO_USERS", "").split()}

    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL") or 0)
    CUSTOM_ALIVE_TEXT = os.environ.get("CUSTOM_ALIVE_TEXT", None)
    CUSTOM_ALIVE_EMOJI = os.environ.get("CUSTOM_ALIVE_EMOJI", None)
    CUSTOM_PMPERMIT = os.environ.get("CUSTOM_PMPERMIT", None)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "Icss - UserBot")
    CLEAN_WELCOME = os.environ.get("CLEAN_WELCOME", True)
    THUMB_IMAGE = os.environ.get(
        "THUMB_IMAGE", "https://telegra.ph/file/e294951013fdb88359650.jpg"
    )
    UB_BLACK_LIST_CHAT = {
        int(x) for x in os.environ.get("UB_BLACK_LIST_CHAT", "").split()
    }
    NO_LOAD = [x for x in os.environ.get("NO_LOAD", "").split()]
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    BOT_PIC = os.environ.get("BOT_PIC", None)
    BOT_HANDLER = os.environ.get("BOT_HANDLER", "^;")
    PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
    DIGITAL_PIC = os.environ.get("DIGITAL_PIC", None)
    DEFAULT_PIC = os.environ.get("DEFAULT_PIC", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    DEFAULT_NAME = os.environ.get("DEFAULT_NAME", None)
    CUSTOM_PMPERMIT_TEXT = os.environ.get("CUSTOM_PMPERMIT_TEXT", None)
    NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD", 7)
    )
    NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD = int(
        os.environ.get("NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD", 3)
    )
    EMOJI_TO_DISPLAY_IN_HELP = os.environ.get("EMOJI_TO_DISPLAY_IN_HELP", "•")
    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r"\.")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\.")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "./downloads")
    TEMP_DIR = os.environ.get("TEMP_DIR", "./temp/")
    CUSTOM_STICKER_PACKNAME = os.environ.get("CUSTOM_STICKER_PACKNAME", None)
    CHANGE_TIME = int(os.environ.get("CHANGE_TIME", 60))
    ANTISPAMBOT_BAN = os.environ.get("ANTISPAMBOT_BAN", False)
    DUAL_LOG = os.environ.get("DUAL_LOG", False)

    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)
    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
    G_DRIVE_AUTH_TOKEN_DATA = os.environ.get("G_DRIVE_AUTH_TOKEN_DATA", None)
    G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK", None)
    TG_2STEP_VERIFICATION_CODE = os.environ.get("TG_2STEP_VERIFICATION_CODE", None)
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IN")
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    LYDIA_API_KEY = os.environ.get("LYDIA_API_KEY", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)
    DEEP_AI = os.environ.get("DEEP_AI", None)

    MAX_MESSAGE_SIZE_LIMIT = 4095
    LOAD = []
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get(
        "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
    )
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
