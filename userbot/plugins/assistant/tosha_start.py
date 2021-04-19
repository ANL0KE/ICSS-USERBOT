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
from userbot.Config import Config
from . import *
from .. import mention
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
            await tgbot.send_message(event.chat_id, BOT_PIC,
                                  caption=startotherdis,
                                  buttons=[
                                      (Button.inline(
                                          "⚜️ ماذا استطيع ان افعل هنا ⚜️",
                                          data="wew"))]
                                  )
        else:
            await event.reply(startotherdis,
                                     buttons=[
                                         (Button.inline(
                                             "⚜️ ماذا استطيع ان افعل هنا ⚜️",
                                             data="wew"))]
                                     )
    elif LOAD_MYBOT == "True":
        if BOT_PIC:
            await tgbot.send_message(event.chat_id, BOT_PIC,
                                  caption=startotherena,
                                  buttons=[
                                      [Button.inline(
                                          "⚜️ 𝙄𝘾𝙎𝙎 - 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⁦⚜️", data="Icss")]
                                  ])
        else:
            await event.reply(startotherena,
                                     buttons=[
                                         [Button.inline(
                                             "⚜️ 𝙄𝘾𝙎𝙎 - 𝙐𝙎𝙀𝙍𝘽𝙊𝙏 ⁦⚜️", data="icss")]
                                     ])


# start-owner
@tgbot.on(events.NewMessage(pattern="^/start",
                            from_users=OWNER_ID))  # pylint: disable=oof
async def owner(event):
    await event.reply(startowner,
                             buttons=[
                                 [Button.inline(
                                     "⚜️ الاعدادات ⚜️", data="settings"),
                                  Button.inline(
                                     "⚜️ الزغرفه ⚜️", data="icszag")],
                                 [Button.inline("⚜️ الاذاعه ⚜️",
                                                data="toshbroad")],
                                 [Button.url("⚜️ الدعم ⚜️",
                                             "https://t.me/rruuurr")]
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
                             "⌔∮ ليس هناك الكثير للقيام به هنا.",
                             buttons=[
                                     [Button.inline(
                                         "⚜️ احصل على بوت اكسس بنفسك ⚜️", data="deployme")]
                             ])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icss"))
          )  # pylint: disable=oof
async def settings(event):
    await event.delete()
    await event.reply(f"⌔∮ انا اكسس مساعد {mention}. الشخصي تستطيع الاتصال بي عن طريق هذا البوت",
                             buttons=[
                                     [Button.inline(
                                         "⚜️ حصل على بوت اكسس بنفسك ⚜️", data="deployme")]
                             ])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"deployme"))
          )  # pylint: disable=oof
async def settings(event):
    await event.edit("** ⌔∮ هنا ستجد رابط اكسس ورابط التنصيب ايضا**:",
                     buttons=[
                         [Button.url("🔗 رابط السورس🔗", url="https://github.com/ANL0KE/ICSS-USERBOT")],
                         [Button.url("🔗 رابط التنصيب 🔗", url="https://dashboard.heroku.com/new?template=https%3A%2F%2Fgithub.com%2FANL0KE%2FICSSBACK")],
                         [Button.url("✨ الدعم ✨",
                                     url="https://t.me/rruuurr")]
                     ])


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"settings"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "** ⌔∮ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "⚜️ لنضام الحمايه ⚜️ ", data="pmbot")],
                                     [Button.inline(
                                         "⚜️ لتغير الايڤ وغيرها ⚜️ ⁦⁩", data="custom")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)


# icss zag - زغرفه اكسس
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icszag"))
          )  # Icss - Userbot
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "** ⌔∮ اختر احد خيارات الزغرفه : **",
                                 buttons=[
                                 [Button.inline(
                                     "اسماء انكلش 🍇", data="icsname"),
                                  Button.inline(
                                     "البايو 🍇", data="icspio1")],
                                 [Button.inline(
                                     "الاشهر 🍇 ⁦⁩", data="icsmonth"),
                                  Button.inline(
                                     "اسماء القنوات 🍇", data="chanlan")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)



# name zag - زغرفه الاسماء
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icsname"))
          ) 
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "** ⌔∮ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "اسماء شباب 🍇 ", data="boysna"),
                                      Button.inline(
                                         "║ رجوع ║ ⁦⁩", data="icazag"),
                                      Button.inline(
                                         "اسماء بنات 🍇", data="girlan")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)


# Boys zag - زغرفه اسماء الشباب
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"boysna"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "** ⌔∮ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "القائمه الاولى 🍇 ", data="boysna1"),
                                      Button.inline(
                                         "القائمه الثانيه 🍇", data="boysna2")],
                                     [Button.inline(
                                         "║ رجوع ║", data="icsname")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)



# Boys zag list1 - قائمه اسماء الشباب الاولى
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"boysna1"))
          )  # Icss - Userbot
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Boysna1, 
                                 buttons=[[Button.inline("║ رجوع ║", data="boysna")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


# Boys zag list2 - قائمه اسماء الشباب الثانيه
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"boysna2"))
          )  # Icss - Userbot
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Boysna2, 
                                 buttons=[[Button.inline("║ رجوع ║", data="boysna")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)



# girls zag - زغرفه اسماء البنات
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"girlan"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "** ⌔∮ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "القائمه الاولى 🍇 ", data="girlan1"),
                                      Button.inline(
                                         "القائمه الثانيه 🍇", data="girlan2")],
                                     [Button.inline(
                                         "║ رجوع ║", data="icsname")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)



# girls zag list1 - قائمه اسماء بنات الاولى
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"girlan1"))
          )  # Icss - Userbot
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Girlan1, 
                                 buttons=[[Button.inline("║ رجوع ║", data="girlan")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)



# girls zag list2 - قائمه اسماء بنات الثانيه
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"girlan2"))
          )  # Icss - Userbot
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 Girlan2, 
                                 buttons=[[Button.inline("║ رجوع ║", data="girlan")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


# Pio - البايو
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icspio1"))
          ) 
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ICSPIO1,
                                 buttons=[
                                     [Button.inline(
                                         " السابق ⫸", data="icspio5"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="icszag"),
                                      Button.inline(
                                         "⫷ التالي ", data="icspio2")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)



# Pio - البايو
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icspio2"))
          ) 
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ICSPIO2,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="icspio1"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="icszag"),
                                      Button.inline(
                                         "⫷ التالي", data="icspio3")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)



# Pio - البايو
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icspio3"))
          ) 
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ICSPIO3,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="icspio2"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="icszag"),
                                      Button.inline(
                                         "⫷ التالي", data="icspio4")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)



# Pio - البايو
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icspio4"))
          ) 
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ICSPIO4,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="icspio3"),
                                      Button.inline(
                                         "║ خروج ║ ⁦⁩", data="icszag"),
                                      Button.inline(
                                         "⫷ التالي", data="icspio5")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)



# Pio - البايو
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icspio5"))
          ) 
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 ICSPIO5,
                                 buttons=[
                                     [Button.inline(
                                         "السابق ⫸ ", data="icspio4"),
                                      Button.inline(
                                         "║ خروج ║⁦⁩", data="icszag"),
                                      Button.inline(
                                         "⫷ التالي", data="icspio1")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)


# Boys zag - زغرفه اسماء الشباب
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icsmonth"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "** ⌔∮ اختر احد الخيارات الاتيه. **",
                                 buttons=[
                                     [Button.inline(
                                         "المواليد 🍇 ", data="icsyear"),
                                      Button.inline(
                                         "الاشهر 🍇", data="months")],
                                     [Button.inline(
                                         "║ رجوع ║", data="icszag")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام البوت احصل على بوتك من @rruuurr", alert=True)


# Months - الاشهر
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"months"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id, 
                                 ICSMONT, 
                                 buttons=[[Button.inline("║ رجوع ║", data="icszag")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


# years - السنوات
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"icsyear"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id, 
                                 ICSYEAR, 
                                 buttons=[[Button.inline("║ رجوع ║", data="icsmonth")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


# channel names - اسماء القنوات
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"chanlan"))
          )  # pylint: disable=oof
async def settings(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id, 
                                 CHANLAN, 
                                 buttons=[[Button.inline("║ رجوع ║", data="icszag")]
                                 ])
    else:
        await event.answer("انت لا تستطيع استخدام هذا البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pmbot"))
          )  # pylint: disable=oof
async def pmbot(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 "**⌔∮ اختر احد اختيارات نضام الحمايه: **",
                                 buttons=[
                                     [Button.inline("⚜️ تفعيل | تعطيل ⚜️", data="onoff"), Button.inline(
                                         "⚜️ رسالة البدء ⚜️", data="cmssg")],
                                     [Button.inline("⚜️ صورة البوت ⚜️", data="btpic")],
                                     [Button.inline("⚜️ رجوع ⚜️", data="settings")]

                                 ])
    else:
        await event.answer("لا تستطيع استخدام البوت.", alert=True)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"onoff"))
          )  # pylint: disable=oof
async def pmbot(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        await tgbot.send_message(event.chat_id,
                                 f"** ⌔∮ اختر تفعيل او تعطيل لنضام الحمايه **.\n **- نضام الحمايه الان:** `{LOAD_MYBOT}`",
                                 buttons=[
                                     [Button.inline("⚜️ للتفعيل ⚜️", data="enable"), Button.inline(
                                         "⚜️ للتعطيل ⚜️", data="disable")],
                                     [Button.inline("⚜️ رجوع ⚜️", data="pmbot")]

                                 ])
    else:
        await event.answer("لا تستطيع استخدام البوت .", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"btpic"))
          )  # pylint: disable=oof
async def bot(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        async with event.client.conversation(OWNER_ID) as conv:
            await conv.send_message("**⌔∮ ارسل لي الصوره التي تضهر عندما يقوم شخص ببدء بوتك يجب ارسالها على شكل ملف :**")
            await conv.send_message("⌔∮ ارسل /cancel لالغاء وضع الصوره")
            response = await conv.get_response()
            try:
                themssg = response.message.message
                if themssg == "/cancel":
                    await conv.send_message("** ⌔∮ تم الالغاء **")
                    return
            except BaseException:
                pass
            media = await event.client.download_media(response, "Bot_Pic")
            try:
                x = upload_file(media)
                url = f"https://telegra.ph/{x[0]}"
                os.remove(media)
            except BaseException:
                return await conv.send_message("** ⌔∮ خطا **")
        tosh = "BOT_PIC"
        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\n رجاء ادخل الفار الاتي ` **HEROKU_APP_NAME**"
            return
        xx = await tgbot.send_message(event.chat_id, "** ⌔∮ يتم تغير صورة البوت انتظر قليلا**")
        heroku_var = app.config()
        heroku_var[tosh] = f"{url}"
        mssg = f"** ⌔∮ تم تغير صورة البوت انتظر قليلا**.\n"
        await xx.edit(mssg)
    else:
        await event.answer("لا تستطيع استخدام هذا البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"cmssg"))
          )  # pylint: disable=oof
async def custom(event):
    if event.sender_id == OWNER_ID:
        await event.reply("** ⌔∮ تستطيع تغير رساله البدء التي تضهر عندما يقوم شخص ببدء بوتك ارسل الان الرساله التي تريدها ** \n  - استخدم /cancel لالغاء هذا الخيار.")
        async with event.client.conversation(OWNER_ID) as conv:
            response = conv.wait_event(events.NewMessage(chats=OWNER_ID))
            response = await response
            themssg = response.message.message
            if themssg == "/cancel":
                await tgbot.send_message(event.chat_id, "** ⌔∮ تم الالغاء **.")
                return
            tosh = "TOSH_START"
            if Config.HEROKU_APP_NAME is not None:
                app = Heroku.app(Config.HEROKU_APP_NAME)
            else:
                mssg = "`**HEROKU**:" "\n رجاء ادخل الفار` **HEROKU_APP_NAME**"
                return
            heroku_var = app.config()
            heroku_var[tosh] = f"{themssg}"
            mssg = "** ⌔∮ تم تغير رسالة البدء جاري اعادة التشغيل انتظر قليلا**"
            await event.delete()
            await tgbot.send_message(event.chat_id, mssg)
    else:
        await event.answer("لا تستطيع استخدام البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"enable"))
          )  # pylint: disable=oof
async def enablee(event):
    if event.sender_id == OWNER_ID:
        tosh = "LOAD_MYBOT"
        if Config.HEROKU_APP_NAME is not None:
            app = Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg = "`**HEROKU**:" "\nرجاء ادخل الفار` **HEROKU_APP_NAME**"
            return
        heroku_var = app.config()
        heroku_var[tosh] = "True"
        mssg = "**⌔∮ تم تفعيل نضام الحمايه.**"
        await event.delete()
        await tgbot.send_message(event.chat_id, mssg)
    else:
        await event.answer("انت لا تستطيع استخدام البوت.", alert=True)


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
        mssg = "**⌔∮ تم تعطيل نضام الحمايه في الخاص.**"
        await event.delete()
        await tgbot.send_message(event.chat_id, mssg)
    else:
        await event.answer(" انت لا تستطيع استخدام البوت.", alert=True)


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"toshbroad"))
          )  # pylint: disable=oof
async def broadcast(event):
    if event.sender_id != OWNER_ID:
        await event.answer(" انت لا تستطيع استخدام البوت")
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
                         [Button.inline("⚜️ حماية الخاص ⚜️", data="pm_cus")],
                         [Button.inline("⚜️ للرجوع ⚜️", data="settings")]
                     ]
                     )
# fmt: off
@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alive_cus")))
async def alv(event):
    await event.edit("** ⌔∮ اختر احد الخيارات الخاصه بالايڤ:**",
                    buttons=[
                        [Button.inline("⚜️ لتغير نص الايڤ ⚜️", data="alv_txt")],
                        [Button.inline("⚜️ لتغير صورة الايڤ ⚜️", data="alv_pic")],
                        [Button.inline("⚜️ للرجوع ⚜️", data="custom")]
                    ])

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"alv_txt")))
async def a_txt(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        old_alv= Config.CUSTOM_ALIVE_TEXT if Config.CUSTOM_ALIVE_TEXT else None
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
                        [Button.inline("⚜️ لتغير صوره الحمايه ⚜️", data="pm_pic")],
                        [Button.inline("⚜️ للرجوع ⚜️", data="custom")]
                    ])

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"pm_txt")))
async def a_txt(event):
    if event.sender_id == OWNER_ID:
        await event.delete()
        old_alv= CUSTOM_PMPERMIT_TEXT 
        tosh="CUSTOM_PMPERMIT_TEXT"
        if Config.HEROKU_APP_NAME is not None:
            app=Heroku.app(Config.HEROKU_APP_NAME)
        else:
            mssg="`**HEROKU**:" "\nرجاء ادخل الفار الاتي` **HEROKU_APP_NAME**"
            return
        async with event.client.conversation(OWNER_ID) as conv:
            await conv.send_message("** ⌔∮ اعطني رساله التي تريد ان تكون رساله للحمايه في الخاص **\n ⌔∮ استخدم /cancel للالغاء❕.")
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
            await conv.send_message(" ⌔∮ ارسل /cancel للالغاء 🖤❕")
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
