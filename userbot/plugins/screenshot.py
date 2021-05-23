"""
Edit: @rruuurr
"""
import io
import traceback
from datetime import datetime

from selenium import webdriver
from validators.url import url


@icssbot.on(admin_cmd(pattern="سكرين (.*)"))
@icssbot.on(sudo_cmd(pattern="سكرين (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.CHROME_BIN is None:
        await edit_or_reply(event, "⌔∮ تحتاج إلى تثبيت جوجل كروم. توقف الوحدة.")
        return
    icsevent = await edit_or_reply(event, "**⪼ جـاري اخذ لقطـه شاشـه ⱒ**")
    start = datetime.now()
    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        # https://stackoverflow.com/a/53073789/4723940
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.CHROME_BIN
        await event.edit("** ⪼ جـاري اخذ لقطـه شاشـه ⱒ.**")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        input_str = event.pattern_match.group(1)
        inputstr = input_str
        icsurl = url(inputstr)
        if not icsurl:
            inputstr = "http://" + input_str
            icsurl = url(inputstr)
        if not icsurl:
            await icsevent.edit("**⪼ ادخل عنوان او رابط للالتقـاط ༗**")
            return
        driver.get(inputstr)
        await icsevent.edit("**⪼ جاري حساب ابعاد الصفـحه ༗**")
        height = driver.execute_script(
            "return Math.max(document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight);"
        )
        width = driver.execute_script(
            "return Math.max(document.body.scrollWidth, document.body.offsetWidth, document.documentElement.clientWidth, document.documentElement.scrollWidth, document.documentElement.offsetWidth);"
        )
        driver.set_window_size(width + 100, height + 100)
        # Add some pixels on top of the calculated dimensions
        # for good measure to make the scroll bars disappear
        im_png = driver.get_screenshot_as_png()
        # saves screenshot of entire page
        await icsevent.edit("**⪼ ا ڪـٓـتمل الالتـٰقـاط ༗**")
        driver.close()
        message_id = None
        if event.reply_to_msg_id:
            message_id = event.reply_to_msg_id
        end = datetime.now()
        ms = (end - start).seconds
        tosh = f"**الرابط : **{input_str} \n**استغرق :** `{ms} ثانيه`"
        await icsevent.delete()
        with io.BytesIO(im_png) as out_file:
            out_file.name = input_str + ".PNG"
            await event.client.send_file(
                event.chat_id,
                out_file,
                caption=tosh,
                force_document=True,
                reply_to=message_id,
                allow_cache=False,
                silent=True,
            )
    except Exception:
        await icsevent.edit(f"`{traceback.format_exc()}`")


CMD_HELP.update(
    {
        "screenshot": "**Plugin : **`screenshot`\
        \n\n**Syntax : **`.ss <url>`\
        \n**Function : **__Takes a screenshot of a website and sends the screenshot.__\
        \n\n**Syntax : **`.scapture <url>`\
        \n**Function : **__Takes a screenshot of a website and sends the screenshot need to set config var for this.__"
    }
)
