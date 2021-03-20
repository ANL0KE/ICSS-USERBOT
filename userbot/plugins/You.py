#    IcssBot - UserBot
#    Copyright (C) 2020 IcssBot
#    (c) @xditya edit by @rruuurr


from telethon import events, Button
import heroku3
import asyncio
import os
import requests
from telegraph import Telegraph, upload_file

##################--CONSTANTS--##################
LOAD_MYBOT = Config.TG_BOT_USERNAME
Heroku = Config.HEROKU_API_KEY
BOT_PIC = Config.ALIVE_PIC if Config.ALIVE_PIC else None
heroku_api = "https://api.heroku.com"
path = Config.TMP_DOWNLOAD_DIRECTORY
if not os.path.isdir(path):
    os.makedirs(path)
telegraph = Telegraph()
r = telegraph.create_account(short_name=Config.TELEGRAPH_SHORT_NAME)
auth_url = r["auth_url"]
################--CONSTANTS-END-#################

# start-others


@tgbot.on(
    events.NewMessage(
       pattern="^/st"
     )
)  # pylint: disable=oof
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
            await tgbot.send_file(event.chat_id,
                                  BOT_PIC,
                                  caption=startotherdis,
                                  buttons=[
                                      (Button.inline(
                                          "What can I do here?",
                                          data="wew"))]
                                  )
        else:
            await tgbot.send_message(event.chat_id,
                                     startotherdis,
                                     buttons=[
                                         (Button.inline(
                                             "What can I do here?",
                                             data="wew"))]
                                     )
    elif LOAD_MYBOT == "True":
        if BOT_PIC:
            await tgbot.send_file(event.chat_id,
                                  BOT_PIC,
                                  caption=startotherena,
                                  buttons=[
                                      [Button.url(
                                          "ICSS - USERBOT", url="https://github.com/ANL0KE/ICSS")],
                                      [Button.inline(
                                          "Whats this?", data="ICSS - USERBOT")]
                                  ]
                                  )
        else:
            await tgbot.send_message(event.chat_id,
                                     startotherena,
                                     buttons=[
                                         [Button.url(
                                             "ICSS - USERBOT", url="https://github.com/xditya/TeleBot")],
                                         [Button.inline(
                                             "Whats this?", data="ICSS - USERBOT")]
                                     ]
                                     )

# start-owner


@tgbot.on(
    events.NewMessage(
       pattern="^/st", from_users=OWNER_ID
    )
)  # pylint: disable=oof
async def owner(event):
    await tgbot.send_message(event.chat_id,
                             startowner,
                             buttons=[
                                 [Button.inline(
                                     "Settings ⚙️", data="settings"),
                                  Button.inline(
                                     "Stats ⚙️", data="stats")],
                                 [Button.inline("Broadcast",
                                                data="telebroad")],
                                 [Button.url("Support",
                                             url="https://t.me/TeleBotSupport")]
                             ])


@tgbot.on(
    events.NewMessage(
       pattern="^/st logs", from_users=OWNER_ID
    )
)  # pylint: disable=oof
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
        caption="**Heroku** TeleBot Logs",
        buttons=[
            [Button.url("View Online", f"{url}")],
            [Button.url("Crashed?", "t.me/rruuurr")]
        ])
    await asyncio.sleep(5)
    return os.remove('logs.txt')

