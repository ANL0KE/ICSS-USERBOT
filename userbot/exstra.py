#  Icss - Userbot
#  For Extras plugins

import sys
import importlib
import logging
from pathlib import Path

from . import (
    CMD_HELP, 
    CMD_LIST,
    LOGS, 
    SUDO_LIST,
    ext,
    bot
)
from .Config import Config
from .helpers.progress import CancelProcess

def load_extras(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/extras/{shortname}.py")
        name = "userbot.extras.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print(f"{ext} " + shortname)

    else:
        import userbot.utils

        from .helpers.tools import media_type
        from .helpers.utils import (
            _format,
            _icsstools,
            _icssutils,
            install_pip,
            reply_id,
        )
        from .tosh import ed, eor

        path = Path(f"userbot/extras/{shortname}.py")
        name = "userbot.extras.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.Config = Config
        mod.tgbot = bot.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.rd = reply_id
        mod.admin_cmd = admin_cmd
        mod.icss_cmd = admin_cmd
        mod.ed = ed
        mod.edit_delete = ed
        mod.eor = eor
        mod.edit_or_reply = eor
        mod.logger = logging.getLogger(shortname)
        sys.modules["uniborg.util"] = userbot.utils
        mod.icssbot = bot
        spec.loader.exec_module(mod)
        sys.modules["userbot.plugins.Admin." + shortname] = mod
        print(f"{ext} " + shortname)
