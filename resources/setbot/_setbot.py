#    Copyright (C) KIMO ~ ANL0KE 2021
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


import asyncio
import telethon.utils
from userbot import LOGS, bot

from resources.Formation.assistant import SetMsg, SteDec, SetAbt
from userbot.tosh import TOSHA, TBOT

async def setbot():
        try:
            entit = await bot.get_entity(TBOT)
            if entit.photo == None:
               LOGS.info(SetMsg[0])
               UL = TBOT
               if bot.me.username == None:
                   first_name = bot.me.first_name
               else:
                   first_name = f"@{bot.me.username}"
               await bot.send_message(TOSHA, SetMsg[0])
               await asyncio.sleep(1)
               await bot.send_message("@botfather", "/cancel")
               await asyncio.sleep(1)
               await bot.send_message("@botfather", "/start")
               await asyncio.sleep(1)
               await bot.send_message("@botfather", "/setuserpic")
               await asyncio.sleep(1)
               await bot.send_message("@botfather", UL)
               await asyncio.sleep(1)
               await bot.send_file("@botfather", "userbot/extras/ex_7.jpeg")
               await asyncio.sleep(2)
               await bot.send_message("@botfather", "/setabouttext")
               await asyncio.sleep(1)
               await bot.send_message("@botfather", UL)
               await asyncio.sleep(1)
               await bot.send_message("@botfather", SetAbt.format(first_name))
               await asyncio.sleep(2)
               await bot.send_message("@botfather", "/setdescription")
               await asyncio.sleep(1)
               await bot.send_message("@botfather", UL)
               await asyncio.sleep(1)
               await bot.send_message("@botfather", SetDec.format(first_name))
               await asyncio.sleep(2)
               await bot.send_message("@botfather", "/start")
               await asyncio.sleep(1)
               await bot.send_message(TOSHA, SetMsg[1])
               LOGS.info(SetMsg[2])
        except Exception as e:
            LOGS.info(str(e))

# End For icss bot Only
# Owner ~ ANL0KE
# Tele ~ @NIIIN2
