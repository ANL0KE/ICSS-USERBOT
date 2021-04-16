# -------------------- #
#    Icss - UserBot    #
#    Owner - @rruuurr  #
# -------------------- #

import asyncio
import html
import os
import re
from math import ceil

from telethon import Button, custom, events, functions
from telethon.tl.functions.users import GetFullUserRequest

from . import ALIVE_NAME, CMD_HELP, CMD_LIST, CUSTOM_PMPERMIT, bot
from ..Config import Config

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "IcssBot User"


CUSTOM_HELP_EMOJI = os.environ.get("CUSTOM_HELP_EMOJI", "⚡")
HELP_ROWS = int(os.environ.get("HELP_ROWS", 5))
HELP_COLOUMNS = int(os.environ.get("HELP_COLOUMNS", 3))

if Config.TG_BOT_USER_NAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)  
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Icss - Userbot"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "© IcssBot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
        elif event.query.user_id == bot.uid and query == "stats":
            result = builder.article(
                title="Stats",
                text=f"**Icss Stats For [{DEFAULTUSER}](tg://user?id={myid})**\n\n__Bot is functioning normally, master!__\n\n(c) @rruuurr",
                buttons=[
                    [custom.Button.inline("Stats", data="statcheck")],
                    [Button.url("Repo", "https://github.com/ANL0KE/ICSS-USERBOT")],
                    [
                        Button.url(
                            "Dev",
                            "https://t.me/rruuurr",
                        )
                    ],
                ],
            )
        elif event.query.user_id == bot.uid and query == "repo":
            result = builder.article(
                title="Repository",
                text=f"IcssBot - Telegram Userbot.",
                buttons=[
                    [Button.url("Repo", "https://github.com/ANL0KE/ICSS-USERBOT")],
                    [Button.url("Support", "https://t.me/rruuurr")],
                ],
            )
        else:
            result = builder.article(
                "Source Code",
                text="**Welcome to IcssBot**\n\n`Click below buttons for more`",
                buttons=[
                    [custom.Button.url("Creator", "https://t.me/NIIIN2")],
                    [
                        custom.Button.url(
                            "Source Code‍", "https://github.com/ANL0KE/ICSS-USERBOT"
                        ),
                        custom.Button.url(
                            "Deploy",
                            "https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FANL0KE%2FICSSBACK",
                        ),
                ],
                link_preview=False,
            )
        await event.answer([result] if result else None)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit(
                "**⌔∮ تم اغلاق القائمه **", buttons=[Button.inline("اعادة فتح القائمه", data="reopen")]
            )
        else:
            reply_pop_up_alert = "⌔∮ احصل على بوت اكسس خاص بك من @rruuurr "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"statcheck")))
    async def rip(event):
        text = telestats
        await event.answer(text, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  
            data=re.compile(rb"helpme_prev\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1, CMD_LIST, "helpme"  
            )
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "⌔∮ احصل على بوت اكسس خاص بك من @rruuurr!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(
        events.callbackquery.CallbackQuery(  
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            plugin_name = event.data_match.group(1).decode("UTF-8")
            help_string = ""
            help_string += f"⌔∮ الاوامر الموجوده في {plugin_name} - \n"
            try:
                if plugin_name in CMD_HELP:
                    for i in CMD_HELP[plugin_name]:
                        help_string += i
                    help_string += "\n"
                else:
                    for i in CMD_LIST[plugin_name]:
                        help_string += i
                        help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} has no detailed info.\nUse .help {}".format(
                    plugin_name, plugin_name
                )
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "\n استخدم .unload {} لحذف هذه الاضافه\n\
                © IcssBot".format(
                plugin_name
            )
            if len(help_string) >= 140:
                oops = "⌔∮ القائمه جدا طويله !\n⌔∮ اذهب الى الرسائل المحفوظه!"
                await event.answer(oops, cache_time=0, alert=True)
                help_string += "\n\nسيتم حذف هذا تلقائيًا خلال دقيقة واحدة‌‌!"
                if bot is not None and event.query.user_id == bot.uid:
                    ok = await bot.send_message("me", help_string)
                    await asyncio.sleep(60)
                    await ok.delete()
            else:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
        else:
            reply_pop_up_alert = "⌔∮ احصل على بوت اكسس خاص بك من @rruuurr!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = HELP_ROWS
    number_of_cols = HELP_COLOUMNS
    kim = CUSTOM_HELP_EMOJI
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(kim, x, kim), data="us_plugin_{}".format(x)
        )
        for x in helpable_plugins
    ]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "⫷ السابق", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("║ اغلاق ║", data="close"),
                custom.Button.inline(
                    "التالي ⫸", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


async def userinfo(event):
    target = await event.client(GetFullUserRequest(event.query.user_id))
    first_name = html.escape(target.user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    return first_name
