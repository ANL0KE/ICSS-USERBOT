#    Icss - UserBot

import re
from userbot.plugins.assistant import *
from telethon import events, Button
import heroku3
import asyncio
import os
import requests
from userbot.plugins.assistant.sql_tosh.blacklist_sql import all_bl_users
from userbot.plugins.assistant.sql_tosh.userbase_sql import add_to_userbase, present_in_userbase, full_userbase
from datetime import datetime
from telethon import events
from userbot.Config import Config
from telegraph import Telegraph, upload_file

# =================== OWNER - ANL0KE =================== #
ALIVE_NAME = Config.ALIVE_NAME if Config.ALIVE_NAME else "@rruuurr"
CUSTOM_PMPERMIT_TEXT = Config.CUSTOM_PMPERMIT_TEXT
LOAD_MYBOT = Config.LOAD_MYBOT
Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
BOT_PIC = Config.BOT_PIC if Config.BOT_PIC else None
heroku_api = "https://api.heroku.com"
path = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.isdir(path):
    os.makedirs(path)
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]
# =================== OWNER - ANL0KE =================== #

# start-others
@tgbot.on(events.NewMessage(pattern="^/start"))  # pylint: disable=oof
async def start_all(event):
    if event.chat_id == OWNER_ID:
        return
    target = event.sender_id
    if present_in_userbase(target):
        pass
    else:
        try:
            add_to_userbase(target)
        except BaseException:
            pass
    if LOAD_MYBOT == "False":
        if BOT_PIC:
            await event.reply(BOT_PIC,
                                  caption=startotherdis,
                                  buttons=[
                                      (Button.inline(
                                          "What can I do here?",
                                          data="wew"))]
                                  )
        else:
            await event.reply(startotherdis,
                                     buttons=[
                                         (Button.inline(
                                             "What can I do here?",
                                             data="wew"))]
                                     )
    elif LOAD_MYBOT == "True":
        if BOT_PIC:
            await event.reply(BOT_PIC,
                                  caption=startotherena,
                                  buttons=[
                                      [Button.url(
                                          "Icss", url="https://github.com/ANL0KE/ICSS-USERBOT")],
                                      [Button.inline(
                                          "Whats this?", data="Icss")]
                                  ]
                                  )
        else:
            await event.reply(startotherena,
                                     buttons=[
                                         [Button.url(
                                             "Icss", url="https://github.com/ANL0KE/ICSS-USERBOT")],
                                         [Button.inline(
                                             "Whats this?", data="icss")]
                                     ]
                                     )

# start-owner


@tgbot.on(events.NewMessage(pattern="^/start",
                            from_users=OWNER_ID))  # pylint: disable=oof
async def owner(event):
    await event.reply(startowner,
                             buttons=[
                                 [Button.inline(
                                     "⚜️ الاعدادات ⚜️", data="settings"),
                                  Button.inline(
                                     "⚜️ الاحصائيات ⚜️", data="stats")],
                                 [Button.inline("⚜️ الاذاعه ⚜️",
                                                data="toshbroad")],
                                 [Button.url("⚜️ الدعم ⚜️",
                                             url="https://t.me/rruuurr")]
                             ])


@tgbot.on(events.NewMessage(pattern="^/logs",
                            from_users=OWNER_ID))  # pylint: disable=oof
async def logs(event):
    try:
        Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
        app = Heroku.app(Config.HEROKU_APP_NAME)
    except BaseException:
        await tgbot.send_message(event.chat_id, " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku var !")
        return
    with open('logs.txt', 'w') as log:
        log.write(app.get_log())
    ok = app.get_log()
    url = "https://del.dog/documents"
    r = requests.post(url, data=ok.encode("UTF-8")).json()
    url = f"https://del.dog/{r['key']}"
    await tgbot.send_file(
        event.chat_id,
        "logs.txt",
        reply_to=event.id,
        caption="**Heroku** Icss Logs",
        buttons=[
            [Button.url("💠 𝙑𝙄𝙀𝙒 𝙊𝙉𝙇𝙄𝙉𝙀 💠", f"{url}")],
            [Button.url("💠 𝘾𝙍𝘼𝙎𝙃𝙀𝘿 💠", "t.me/rruuurr")]
        ])
    await asyncio.sleep(5)
    return os.remove('logs.txt')


# callbacks


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"wew"))
          )  # pylint: disable=oof
async def settings(event):
    await event.delete()
    await tgbot.send_message(event.chat_id,
                             "There isn't much that you can do over here rn.",
                             buttons=[
                                     [Button.inline(
                                         "⌔∮ احصل على بوت اكسس بنفسك", data="deployme")]
                             ])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icss"))
          )  # pylint: disable=oof
async def settings(event):
    await event.delete()
    await tgbot.send_message(event.chat_id,
                             f"⌔∮ انا اكسس مساعد {ALIVE_NAME}. الشخصي تستطيع الاتصال بي عن طريق هذا البوت",
                             buttons=[
                                     [Button.inline(
                                         "⌔∮ احصل على بوت اكسس بنفسك", data="deployme")]
                             ])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deployme"))
          )  # pylint: disable=oof
async def settings(event):
    await event.edit("Browse through the available options:",
                     buttons=[
                         [(Button.url("🔗 رابط السورس🔗", url="https://github.com/ANL0KE/ICSS-USERBOT")),
                          (Button.url("🔗 رابط التنصيب 🔗", url="https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FANL0KE%2FICSSBACK"))],
                         [Button.url("✨ الدعم ✨",
                                     url="https://t.me/rruuurr")]
                     ])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"settings"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        ok = Config.TG_BOT_USERNAME
        if ok.startswith('@'):
            ok = ok.split('@')[1]
        await tgbot.send_message(event.chat_id,
                                 "** ⌔∮ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "𝙋𝙈 - 𝘽𝙊𝙏 ", data="pmbot")],
                                     [Button.inline(
                                         "𝘾𝙐𝙎𝙏𝙊𝙈𝙎 ⁦⁩", data="custom")],
                                     [Button.url(
                                         "𝙇𝙊𝙂𝙎 ", url=f"https://t.me/{ok}?start=logs")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        allu = len(full_userbase())
        blu = len(all_bl_users())
        pop = "Here is the stats for your bot:\nTotal Users = {}\nBlacklisted Users = {}".format(
            allu, blu)
        await event.answer(pop, alert=True)
    else:
        await event.answer("You can't use this bot.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmbot"))
          )  # pylint: disable=oof
async def pmbot(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "Here are the availabe settings for PM bot.",
                                 buttons=[
                                     [Button.inline("Enable/Disable", data="onoff"), Button.inline(
                                         "Custom Message", data="cmssg")],
                                     [Button.inline("Bot Pic", data="btpic")]
                                 ])
    else:
        await event.answer("You can't use this bot.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"onoff"))
          )  # pylint: disable=oof
async def pmbot(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 f"Turn the PM bot on or off.\nCurrently enabled: {LOAD_MYBOT}",
                                 buttons=[
                                     [Button.inline("Enable", data="enable"), Button.inline(
                                         "Disable", data="disable")]
                                 ])
    else:
        await event.answer("You can't use this bot.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"btpic"))
          )  # pylint: disable=oof
async def bot(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        async with event.client.conversation(OWNER_ID) as conv:
            await conv.send_message("Send the new pic you want to be shown when someone starts the bot:")
            await conv.send_message("Send /cancel to cancel the operation!")
            response = await conv.get_response()
            try:
                themssg = response.message.message
                if themssg == "/cancel":
                    await conv.send_message("Operation cancelled!!")
                    return
            except BaseException:
                pass
            media = await event.client.download_media(response, "Bot_Pic")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("Error!")
        telebot = "BOT_PIC"
        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(event.chat_id, "Changing your Bot Pic, please wait for a minute")
        heroku_var = app.config()
        heroku_var[telebot] = f"{url}"
        mssg = f"Successfully changed your bot pic. Please wait for a minute.\n"
        await xx.edit(mssg)
    else:
        await event.answer("You can't use this bot.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"cmssg"))
          )  # pylint: disable=oof
async def custom(event):
    if event.sender_id == OWNER_ID:
        await event.reply("You can change your PMBot start message here.\nSend the message you want to display when someone started the bot, /cancel to cancel the operation.")
        async with event.client.conversation(OWNER_ID) as conv:
            response = conv.wait_event(events.NewMessage(chats=OWNER_ID))
            response = await response
            themssg = response.message.message
            if themssg == "/cancel":
                await tgbot.send_message(event.chat_id, "Operation Cancelled.")
                return
            telebot = "PMBOT_START_MSSG"
            if Config.HEROKU_APP_NAME is not None:
                app = Heroku.app(Config.HEROKU_APP_NAME)
            else:
                mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
                return
            heroku_var = app.config()
            heroku_var[telebot] = f"{themssg}"
            mssg = "Changed the PMBot start message!!\n**Restarting now**, please give me a minute."
            await event.delete()
            await tgbot.send_message(event.chat_id, mssg)
    else:
        await event.answer("You can't use this bot.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"enable"))
          )  # pylint: disable=oof
async def enablee(event):
    if event.sender_id == OWNER_ID:
        telebot = "LOAD_MYBOT"
        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nPlease setup your` **HEROKU_APP_NAME**"
            return
        heroku_var = app.config()
        heroku_var[telebot] = "True"
        mssg = "Successfully turned on PM Bot. Restarting now, please give me a minute."
        await event.delete()
        await tgbot.send_message(event.chat_id, mssg)
    else:
        await event.answer("⌔∮ انت لا تستطيع استخدام البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"disable"))
          )  # pylint: disable=oof
async def dissable(event):
    if event.sender_id == OWNER_ID:
        tosh = "LOAD_MYBOT"
        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\n رجاء قم بادخال الفار ` **HEROKU_APP_NAME**"
            return
        heroku_var = app.config()
        heroku_var[tosh] = "False"
        mssg = "**⌔∮ تم تفعيل نضام الحمايه في الخاص.**"
        await event.delete()
        await tgbot.send_message(event.chat_id, mssg)
    else:
        await event.answer("⌔∮ انت لا تستطيع استخدام البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"toshbroad"))
          )  # pylint: disable=oof
async def broadcast(event):
    if event.sender_id != OWNER_ID:
        await event.answer("⌔∮ انت لا تستطيع استخدام البوت")
        return
    await tgbot.send_message(event.chat_id, "** ⌔∮ ارسل رساله للاذاعه بها **!\n  - ارسل /cancel لالغاء الاذاعه.")
    async with event.client.conversation(OWNER_ID) as conv:
        response = conv.wait_event(events.NewMessage(chats=OWNER_ID))
        response = await response
        themssg = response.message.message
    if themssg is None:
        await tgbot.send_message(event.chat_id, "⌔∮ هناك خطا ")
    if themssg == "/cancel":
        await tgbot.send_message(event.chat_id, "** ⌔∮ تم الغاء الاذاعه**")
        return
    targets = full_userbase()
    users_cnt = len(full_userbase())
    err = 0
    success = 0
    lmao = await tgbot.send_message(event.chat_id, "** ⌔∮ جاري الارسال الى {} مستخدم **.".format(users_cnt))
    start = datetime.now()
    for ok in targets:
        try:
            await tgbot.send_message(int(ok.chat_id), themssg)
            success += 1
            await asyncio.sleep(0.1)
        except Exception as e:
            err += 1
            try:
                await tgbot.send_message(Config.PRIVATE_GROUP_ID, f"** ⌔∮ خطا **\n{str(e)}\nخطا المستخدم: {chat_id}")
            except BaseException:
                pass
    end = datetime.now()
    ms = (end - start).seconds
    done_mssg = """
** ⌔∮ تم ارسال بنجاح**\n
 - تم الارسال الى `{}` مستخدم في `{}` ثانيه.\n
 - فشل الارسال الى `{}` مستخدم.\n
 - مجموع المستخدمين البوت الخاص بك: `{}`.\n
""".format(success, ms, err, users_cnt)
    await lmao.edit(done_mssg)
    try:
        await tgbot.send_message(Config.PRIVATE_GROUP_ID, f"**#الاذاعه**\n ⌔∮ تم ارسال بنجاح الى {success} مستخدم.")
    except BaseException:
        await tgbot.send_message(event.chat_id, "** ⌔∮ رجاء قم بانشاء كروب خاص لكي تستطيع استخدام هذا الخيار**.")


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"custom"))
          )  # pylint: disable=oof
async def custommm(event):
    await event.edit("** ⌔∮ اختر احد الخيارات الخاصه بتغير الاتي: **",
                     buttons=[
                         [Button.inline("⚜️ الايڤ ⚜️", data="alive_cus")],
                         [Button.inline("⚜️ حماية الخاص ⚜️", data="pm_cus")]
                     ]
                     )
# fmt: off
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive_cus")))
async def alv(event):
    await event.edit("** ⌔∮ اختر احد الخيارات الخاصه بالايڤ:**",
                    buttons=[
                        [Button.inline("⚜️ لتغير نص الايڤ ⚜️", data="alv_txt")],
                        [Button.inline("⚜️ لتغير صورة الايڤ ⚜️", data="alv_pic")]
                    ])

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alv_txt")))
async def a_txt(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        old_alv= Config.CUSTOM_ALIVE if Config.CUSTOM_ALIVE else "Default Alive message"
        tosh="CUSTOM_ALIVE_TEXT"
        if Config.HEROKU_APP_NAME_TEXT is not None:
            app=Heroku.app(Config.HEROKU_APP_NAME_TEXT)
        else:
            mssg="`**HEROKU**:" "\n ⌔∮ رجاء ادخل الفار` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(OWNER_ID) as conv:
            await conv.send_message("** ⌔∮ ارسل لي نص الذي تريده ليصبح نص الايڤ **\n** ⌔∮ /cancel للالغاء**")
            response=conv.wait_event(events.NewMessage(chats=OWNER_ID))
            response=await response
            themssg=response.message.message
            if themssg == None:
                await conv.send_message("** ⌔∮ خطا ⚜️**")
                return
            if themssg == "/cancel":
                return await conv.send_message("** ⌔∮ تم الالغاء **")
            heroku_var=app.config()
            xx = await tgbot.send_message(event.chat_id, "**⌔∮ يتم تغير نص الايڤ انتظر قليلا **")
            heroku_var[tosh]=f"{themssg}"
            mssg=f"** ⌔∮ تم تغير نص الايڤ من**\n  - `{old_alv}`\n** ⌔∮ الى **\n  - `{themssg}`\n"
            await xx.edit(mssg)
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr.", alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alv_pic"))
           )  # pylint: disable=C0321
async def alv_pic(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id, "** ⌔∮ ارسل لي الصوره الان **.")
        async with event.client.conversation(OWNER_ID) as conv:
            await conv.send_message("**⌔∮ ارسل /cancel للالغاء **")
            response = await conv.get_response()
            try:
                themssg=response.message.message
                if themssg == "/cancel":
                    await conv.send_message("** ⌔∮ تم الغاء الخيار**")
                    return
            except:
                pass
            media=await event.client.download_media(response, "Alive_Pic")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("**⌔∮ خطا ⚜️.**")
        tosh="ALIVE_PIC"
        if Config.HEROKU_APP_NAME is not None:
            app=Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg="`**HEROKU**:" "\n ⌔∮ رجاء ادخل الفار ` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(event.chat_id, "**⌔∮ يتم تغير الصوره انتظر قليلا**")
        heroku_var=app.config()
        heroku_var[tosh]=f"{url}"
        mssg=f"**⌔∮ تم تغير الصوره بنجاح انتظر قليلا **.\n"
        await xx.edit(mssg)
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr.", alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pm_cus")))
async def alv(event):
    await event.edit("** ⌔∮ اختر احد الخيارات الاتيه الخاصه بحماية الخاص:**",
                    buttons=[
                        [Button.inline("⚜️ لتغير رساله الحمايه ⚜️", data="pm_txt")],
                        [Button.inline("⚜️ لتغير صوره الحمايه ⚜️", data="pm_pic")]
                    ])

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pm_txt")))
async def a_txt(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        old_alv= CUSTOM_PMPERMIT_TEXT if CUSTOM_PMPERMIT_TEXT else "ᴅᴇғᴀᴜʟᴛ ᴘᴍsᴇᴄᴜʀɪᴛʏ ᴍᴇssᴀɢᴇ 𖠛"
        tosh="CUSTOM_PMPERMIT_TEXT"
        if Config.HEROKU_APP_NAME is not None:
            app=Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg="`**HEROKU**:" "\n⌔∮ رجاء ادخل الفار الاتي` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(OWNER_ID) as conv:
            await conv.send_message("** ⌔∮ اعطني رساله التي تريد ان تكون رساله للحمايه في الخاص **\n** ⌔∮ استخدم /cancel للالغاء❕.**")
            response=conv.wait_event(events.NewMessage(chats=OWNER_ID))
            response=await response
            themssg=response.message.message
            if themssg == None:
                await conv.send_message("**⌔∮ خطا ⁉️**")
                return
            if themssg == "/cancel":
                await conv.send_message("**⌔∮ تم الغاء الخيار !**")
            heroku_var=app.config()
            xx = await tgbot.send_message(event.chat_id, "**⌔∮ تم تغير رساله الحمايه بنجاح انتظر قليلاً 🖤❕.**")
            heroku_var[tosh]=f"{themssg}"
            mssg=f"**⌔∮ تم تغير رسالة الحمايه من**\n  - `{old_alv}`\n **⌔∮ الى **\n  - `{themssg}`\n"
            await xx.edit(mssg)
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pm_pic"))
           )  # pylint: disable=C0321
async def alv_pic(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id, "** ⌔∮ ارسل لي الصوره التي تريد وضعها في رساله الحمايه الخاصه بك **.")
        async with event.client.conversation(OWNER_ID) as conv:
            await conv.send_message("** ⌔∮ ارسل /cancel للالغاء 🖤❕**")
            response = await conv.get_response()
            try:
                themssg=response.message.message
                if themssg == "/cancel":
                    await conv.send_message("** ⌔∮ تم الالغاء ⚜️**")
                    return
            except:
                pass
            media=await event.client.download_media(response, "PM_PIC")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("** ⌔∮ خطا **")
        tosh="PMPERMIT_PIC"
        if Config.HEROKU_APP_NAME is not None:
            app=Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg="`**HEROKU**:" "\n ⌔∮ رجاء ادخل معلومات الفار ` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(event.chat_id, "** ⌔∮ يتم تغير صورة الحمايه الخاصه بك انتظر قليلا**")
        heroku_var=app.config()
        heroku_var[tosh]=f"{url}"
        mssg=f"**⌔∮ تم تغير صوره الحمايه الخاصه بك ✨**.\n"
        await xx.edit(mssg)
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr.", alert=True)

# fmt: on
