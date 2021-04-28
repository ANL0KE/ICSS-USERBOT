# Icss - Userbot
# translater for Icss - Userbot
# Owner ~ <@rruuurr>

from google_trans_new import google_translator
import requests
from PyDictionary import PyDictionary
from telethon import events
from telethon.tl import functions

@asst_cmd("ترجمه")
@owner
async def _(e):
    input_str = e.pattern_match.group(1)
    if e.reply_to_msg_id:
        previous_message = await e.get_reply_message()
        text = previous_message.message
        lan = input_str or "ar"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await e.reply("**⌔∮ ترجمه + كود اللغه وتقوم برد على الكبمه او الجمله \n**⌔∮ او **\n **- ترجمه كود اللغه| الكلمه او الجمله**")
        return
    text = text.strip()
    lan = lan.strip()
    translator = google_translator()  
    try:
        translated = translator.translate(text,lang_tgt=lan)  
        after_tr_text = translated
        detect_result = translator.detect(text)
        output_str = (
            "** ⌔∮ تمت الترجمه بواسطه بوت اكسس**: \n من {} الى {}\n"
            "{}"
        ).format(
            detect_result[0],
            lan,
            after_tr_text
        )
        await e.reply(output_str)
    except Exception as ex:
        await e.reply(str(ex))
