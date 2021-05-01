#    Icss - UserBot    #
#    Owner - @rruuurr  #

import io
import json
import math
import os
import re
import time

from telethon import Button, custom, events

from . import CMD_LIST, icsa

TOSH = Config.ALIVE_PIC or None
BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)\]\<buttonurl:(?:/{0,2})(.+?)(:same)?\>)")

if Config.TG_BOT_USERNAME is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        tosh = re.compile("secret (.*) (.*)")
        match = re.findall(tosh, query)
        if query.startswith("**IcssBot") and event.query.user_id == bot.uid:
            buttons = [
                (
                    custom.Button.inline("Stats", data="stats"),
                    Button.url("Repo", "https://github.com/ANL0KE/ICSS-USERBOT"),
                )
            ]
            if TOSH and TOSH.endswith((".jpg", ".png")):
                result = builder.photo(
                    TOSH,
                    text=query,
                    buttons=buttons,
                )
            elif TOSH:
                result = builder.document(
                    TOSH,
                    title="Icss Alive",
                    text=query,
                    buttons=buttons,
                )
            else:
                result = builder.article(
                    title="Icss Alive",
                    text=query,
                    buttons=buttons,
                )
            await event.answer([result] if result else None)
        elif event.query.user_id == bot.uid and query.startswith("𓆩"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "©IcssBot Help",
                text="{}\n\n⌔∮ عدد الاضافات : {}**".format(query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
        elif event.query.user_id == bot.uid and query.startswith("Inline buttons"):
            markdown_note = query[14:]
            prev = 0
            note_data = ""
            buttons = []
            for match in BTN_URL_REGEX.finditer(markdown_note):
                n_escapes = 0
                to_check = match.start(1) - 1
                while to_check > 0 and markdown_note[to_check] == "\\":
                    n_escapes += 1
                    to_check -= 1
                # if even, not escaped -> create button
                if n_escapes % 2 == 0:
                    buttons.append(
                        (match.group(2), match.group(3), bool(match.group(4)))
                    )
                    note_data += markdown_note[prev : match.start(1)]
                    prev = match.end(1)
                elif n_escapes % 2 == 1:
                    note_data += markdown_note[prev:to_check]
                    prev = match.start(1) - 1
                else:
                    break
            else:
                note_data += markdown_note[prev:]
            message_text = note_data.strip()
            tl_ib_buttons = ibuild_keyboard(buttons)
            result = builder.article(
                title="Inline creator",
                text=message_text,
                buttons=tl_ib_buttons,
                link_preview=False,
            )
            await event.answer([result] if result else None)
        elif event.query.user_id == bot.uid and match:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./userbot", "secrets.txt")
            try:
                jsondata = json.load(open(secret))
            except Exception:
                jsondata = False
            try:
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        Kimo = f"@{u.username}"
                    else:
                        Kimo = f"[{u.first_name}](tg://user?id={u.id})"
                except ValueError:
                    Kimo = f"[user](tg://user?id={u})"
            except ValueError:
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    Kimo = f"@{u.username}"
                else:
                    Kimo = f"[{u.first_name}](tg://user?id={u.id})"
                u = int(u.id)
            except Exception:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [
                custom.Button.inline("اضهار الرساله 🔐", data=f"secret_{timestamp}")
            ]
            result = builder.article(
                title="✨ ارسال الهمسه ✨",
                text=f"**⌔∮ هذه الهمسه الى {Kimo} هو الوحيد الذي يستطيع رؤيتها.**",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))

    @tgbot.on(
        events.callbackquery.CallbackQuery(
            data=re.compile(rb"helpme_next\((.+?)\)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid: 
            current_page_number = int(event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(current_page_number + 1, CMD_LIST, "helpme")
            await event.edit(buttons=buttons)
        else:
            reply_pop_up_alert = "⌔∮ عليك الحصول على بوت اكسس للحصول عليه اذهب الى @rruuurr. "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

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
            reply_pop_up_alert = "⌔∮ عليك الحصول على بوت اكسس للحصول عليه اذهب الى @rruuurr. "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"secret_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
        if os.path.exists("./userbot/secrets.txt"):
            jsondata = json.load(open("./userbot/secrets.txt"))
            try:
                message = jsondata[f"{timestamp}"]
                userid = message["userid"]
                ids = [userid, bot.uid]
                if event.query.user_id in ids:
                    encrypted_tcxt = message["text"]
                    reply_pop_up_alert = encrypted_tcxt
                else:
                    reply_pop_up_alert = "⌔∮ عليك الحصول على بوت اكسس للحصول عليه اذهب الى @rruuurr. "
            except KeyError:
                reply_pop_up_alert = "⌔∮ هذه الرسالة لم تعد موجودة في خادم بوت"
        else:
            reply_pop_up_alert = "⌔∮ هذه الرساله لو تعد موجوده "
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
            try:
                for i in CMD_LIST[plugin_name]:
                    help_string += i
                    help_string += "\n"
            except BaseException:
                pass
            if help_string == "":
                reply_pop_up_alert = "{} غير مجديه".format(plugin_name)
            else:
                reply_pop_up_alert = help_string
            reply_pop_up_alert += "استخدم .unload {} لحذف هذه الاضافه ".format(
                plugin_name
            )
            try:
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            except BaseException:
                with io.BytesIO(str.encode(reply_pop_up_alert)) as out_file:
                    out_file.name = "{}.txt".format(plugin_name)
                    await event.client.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption=plugin_name,
                    )
        else:
            reply_pop_up_alert = "⌔∮ عليك الحصول على بوت اكسس للحصول عليه اذهب الى @rruuurr. "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            await event.edit("**⌔∮ تم اغلاق القائمه**")
        else:
            reply_pop_up_alert = "⌔∮ عليك الحصول على بوت اكسس للحصول عليه اذهب الى @rruuurr. "
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats")))
    async def on_plug_in_callback_query_handler(event):
        statstext = await icsa()
        reply_pop_up_alert = statstext
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    helpable_plugins = [p for p in loaded_plugins if not p.startswith("_")]
    helpable_plugins = sorted(helpable_plugins)
    modules = [
        custom.Button.inline(
            "{} {} {}".format(
                Config.EMOJI_TO_DISPLAY_IN_HELP, x, Config.EMOJI_TO_DISPLAY_IN_HELP
            ),
            data="us_plugin_{}".format(x),
        )
        for x in helpable_plugins
    ]
    if number_of_cols == 1:
        pairs = list(zip(modules[::number_of_cols]))
    elif number_of_cols == 2:
        pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    else:
        pairs = list(
            zip(
                modules[::number_of_cols],
                modules[1::number_of_cols],
                modules[2::number_of_cols],
            )
        )
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    elif len(modules) % number_of_cols == 2:
        pairs.append((modules[-2], modules[-1]))
    max_num_pages = math.ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[
            modulo_page * number_of_rows : number_of_rows * (modulo_page + 1)
        ] + [
            (
                custom.Button.inline(
                    "السابق ⫸", data="{}_prev({})".format(prefix, modulo_page)
                ),
                custom.Button.inline("║ اغلاق ║", data="close"),
                custom.Button.inline(
                    "⫷ التالي ", data="{}_next({})".format(prefix, modulo_page)
                ),
            )
        ]
    return pairs


def ibuild_keyboard(buttons):
    keyb = []
    for btn in buttons:
        if btn[2] and keyb:
            keyb[-1].append(Button.url(btn[0], btn[1]))
        else:
            keyb.append([Button.url(btn[0], btn[1])])
    return keyb
