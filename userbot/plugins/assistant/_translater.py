# Icss - Userbot
# translater for Icss - Userbot
# Owner ~ <@rruuurr>

from googletrans import Translator, LANGUAGES

Tr = "ar"

@asst_cmd("ترجمه")
@owner
async def _(e):
    Translator()
    textx = await e.get_reply_message()
    message = e.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await e.reply("**⌔∮ قم باعطائي الكلمه او قم برد عليها لكي اقوم بترجمتها**")
        return
    try:
        reply_text = await getTranslate(deEmojify(message), dest=Tr)
    except ValueError:
        await e.reply("** ⌔∮ كود اللغه غير صحيح !**")
        return
    source_lan = LANGUAGES[f"{reply_text.src.lower()}"]
    transl_lan = LANGUAGES[f"{reply_text.dest.lower()}"]
    reply_text = f"⌔∮ **تمت الترجمه من {source_lan.title()}({reply_text.src.lower()}) الى {transl_lan.title()}({reply_text.dest.lower()}) :**\n  - {reply_text.text}"
    await e.reply(reply_text)

async def getTranslate(text, **kwargs):
    translator = Translator()
    result = None
    for _ in range(10):
        try:
            result = translator.translate(text, **kwargs)
        except Exception:
            translator = Translator()
            await sleep(0.1)
    return result
