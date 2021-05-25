# for plugins:
from resources.Formation.plugins import *
from userbot import bot
from userbot.tosh import *

# For format M:
O = bot.me.id
Name = bot.me.first_name
M = "[{}](tg://user?id={})".format(Name, O)


# for Calc text - HelpText & Quotly text
from userbot.tosh import (
    Calc,
    C,
    HelpString,
    Quotly,
    Echo
)

