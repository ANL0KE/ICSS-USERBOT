# Heroku manager for icssbot

import asyncio
import math
import os

import heroku3
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
heroku_api = "https://api.heroku.com"
HEROKU_APP_NAME = Config.HEROKU_APP_NAME
HEROKU_API_KEY = Config.HEROKU_API_KEY

Heroku_cmd = (
    "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑯𝑬𝑹𝑶𝑲𝑼 𝑽𝑨𝑹𝑺 𓆪\n"
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    "**⌔∮ قائـمه اوامر هيروكو :** \n"
    "⪼ `.set var` + الفار + المتغير\n"
    "⪼ `.get var` + الفار لعرض ما في المتغير \n"
    "⪼ `.del var` + الفار لحذف الفار \n"
    "⪼ `.استخدامي` \n"
    "𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    "𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙞𝘾𝙎𝙎 - [𝘿𝙀𝙑](t.me/rruuurr) 𓆪"
)

@icss.on(icss_cmd(pattern=r"(set|get|del) var (.*)", outgoing=True))
@icss.on(sudo_cmd(pattern=r"(set|get|del) var (.*)", allow_sudo=True))
async def variable(var):
    if Config.HEROKU_API_KEY is None:
        return await ed(
            var,
            "⌔∮ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    if Config.HEROKU_APP_NAME is not None:
        app = Heroku.app(Config.HEROKU_APP_NAME)
    else:
        return await ed(
            var,
            "⌔∮ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    exe = var.pattern_match.group(1)
    heroku_var = app.config()
    if exe == "get":
        ics = await edit_or_reply(var, "**⌔∮ جاري الحصول على المعلومات. **")
        await asyncio.sleep(1.0)
        try:
            variable = var.pattern_match.group(2).split()[0]
            if variable in heroku_var:
                return await ics.edit(
                    "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
                    f"\n **⌔∮** `{variable} = {heroku_var[variable]}` .\n"
                )
            return await ics.edit(
                "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑮𝑶𝑵𝑭𝑰𝑮 𝑽𝑨𝑹𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
                f"\n **⌔∮ خطا :**\n-> {variable} غيـر موجود. "
            )
        except IndexError:
            configs = prettyjson(heroku_var.to_dict(), indent=2)
            with open("configs.json", "w") as fp:
                fp.write(configs)
            with open("configs.json", "r") as fp:
                result = fp.read()
                if len(result) >= 4096:
                    await bot.send_file(
                        var.chat_id,
                        "configs.json",
                        reply_to=var.id,
                        caption="`Output too large, sending it as a file`",
                    )
                else:
                    await ics.edit(
                        "`[HEROKU]` ConfigVars:\n\n"
                        "================================"
                        f"\n```{result}```\n"
                        "================================"
                    )
            os.remove("configs.json")
            return
    elif exe == "set":
        variable = "".join(var.text.split(maxsplit=2)[2:])
        ics = await edit_or_reply(var, "**⌔∮ جاري اعداد المعلومات**")
        if not variable:
            return await ics.edit("⌔∮ .set var `<ConfigVars-name> <value>`")
        value = "".join(variable.split(maxsplit=1)[1:])
        variable = "".join(variable.split(maxsplit=1)[0])
        if not value:
            return await ics.edit("⌔∮ .set var `<ConfigVars-name> <value>`")
        await asyncio.sleep(1.5)
        if variable in heroku_var:
            await ics.edit("**⌔∮ تم تغيـر** `{}` **:**\n **- المتغير :** `{}`".format(variable, value))
        else:
            await ics.edit("**⌔∮ تم اضافه** `{}` **:** \n**- المضاف اليه :** `{}`".format(variable, value))
        heroku_var[variable] = value
    elif exe == "del":
        ics = await edit_or_reply(var, "⌔∮ الحصول على معلومات لحذف المتغير. ")
        try:
            variable = var.pattern_match.group(2).split()[0]
        except IndexError:
            return await ics.edit("⌔∮ يرجى تحديد `Configvars` تريد حذفها. ")
        await asyncio.sleep(1.5)
        if variable not in heroku_var:
            return await ics.edit(f"⌔∮ `{variable}`**  غير موجود**")

        await ics.edit(f"**⌔∮** `{variable}`  **تم حذفه بنجاح. **")
        del heroku_var[variable]


@icss.on(icss_cmd(pattern="استخدامي$", outgoing=True))
@icss.on(sudo_cmd(pattern="استخدامي$", allow_sudo=True))
async def dyno_usage(dyno):
    """
    Get your account Dyno Usage
    """
    if HEROKU_APP_NAME is None:
        return await ed(
            dyno,
            "⌔∮ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_APP_NAME` اسم التطبيق اذا كنت لاتعلم.",
        )
    if HEROKU_API_KEY is None:
        return await ed(
            dyno,
            "⌔∮ اضبط Var المطلوب في Heroku على وظيفة هذا بشكل طبيعي `HEROKU_API_KEY` اذا كنت لاتعلم اين يوجد فقط اذهب الى حسابك في هيروكو ثم الى الاعدادات ستجده بالاسفل انسخه ودخله في الفار. ",
        )
    dyno = await edit_or_reply(dyno, "**⌔∮ جاري المعـالجه..**")
    useragent = (
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/80.0.3987.149 Mobile Safari/537.36"
    )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": useragent,
        "Authorization": f"Bearer {Config.HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    path = "/accounts/" + user_id + "/actions/get-quota"
    r = requests.get(heroku_api + path, headers=headers)
    if r.status_code != 200:
        return await dyno.edit("⌔∮ خطا:** شي سيء قد حدث **\n" f" ⌔∮ `{r.reason}`\n")
    result = r.json()
    quota = result["account_quota"]
    quota_used = result["quota_used"]

    # - Used -
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    # - Current -
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    await asyncio.sleep(1.5)
    return await dyno.edit(
        "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑫𝒀𝑵𝑶 𝑼𝑺𝑨𝑮𝑬 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
        f"**⌔∮ اسم التطبيق في هيروكو :**\n"
        f"**    - معرف اشتراكك ⪼ {Config.HEROKU_APP_NAME}**"
        f"\n\n"
        f" **⌔∮ مدة اسـتخدامك لبوت اكسس : **\n"
        f"     -  `{AppHours}`**ساعه**  `{AppMinutes}`**دقيقه**  "
        f"**⪼**  `{AppPercentage}`**%**"
        "\n\n"
        " **⌔∮ الساعات المتبقيه لاستخدامك : **\n"
        f"     -  `{hours}`**ساعه**  `{minutes}`**دقيقه**  "
        f"**⪼**  `{percentage}`**%**"
    )


@icss.on(icss_cmd(pattern="herokulogs$", outgoing=True))
@icss.on(sudo_cmd(pattern="herokulogs$", allow_sudo=True))
async def _(dyno):
    if HEROKU_APP_NAME is None:
        return await ed(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_APP_NAME`.",
        )
    if HEROKU_API_KEY is None:
        return await ed(
            dyno,
            "Set the required var in heroku to function this normally `HEROKU_API_KEY`.",
        )
    try:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
    except BaseException:
        return await dyno.reply(
            " Please make sure your Heroku API Key, Your App name are configured correctly in the heroku"
        )
    data = app.get_log()
    key = (
        requests.post("https://nekobin.com/api/documents", json={"content": data})
        .json()
        .get("result")
        .get("key")
    )
    url = f"https://nekobin.com/{key}"
    reply_text = f"Recent 100 lines of heroku logs: [here]({url})"
    await edit_or_reply(dyno, reply_text)


def prettyjson(obj, indent=2, maxlinelength=80):
    items, _ = getsubitems(
        obj,
        itemkey="",
        islast=True,
        maxlinelength=maxlinelength - indent,
        indent=indent,
    )
    return indentitems(items, indent, level=0)

@icss.on(
    icss_cmd(pattern="م24")
)
async def cmd(hero):
    await eor(hero, Heroku_cmd)

CMD_HELP.update(
    {
        "heroku": "Info for Module to Manage Heroku:**\n\n`.استخدامي`\nاستخدامي:__لعرض ساعات استخدامي الحاليه والمتبقيه.__\n\n`.set var <NEW VAR> <VALUE>`\nUsage: __add new variable or update existing value variable__\n**!!! WARNING !!!, after setting a variable the bot will restart.**\n\n`.get var or .get var <VAR>`\nUsage: __get your existing varibles, use it only on your private group!__\n**This returns all of your private information, please be cautious...**\n\n`.del var <VAR>`\nUsage: __delete existing variable__\n**!!! WARNING !!!, after deleting variable the bot will restarted**\n\n`.herokulogs`\nUsage:sends you recent 100 lines of logs in heroku"
    }
)
