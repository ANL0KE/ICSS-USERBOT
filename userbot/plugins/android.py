# ©SOURCE ICSS
# @rruuurr

import json
import re

from bs4 import BeautifulSoup
from requests import get

GITHUB = "https://github.com"
DEVICES_DATA = (
    "https://raw.githubusercontent.com/androidtrackers/"
    "certified-android-devices/master/devices.json"
)


@icssbot.on(admin_cmd(pattern=r"ميكاسك"))
@icssbot.on(sudo_cmd(pattern=r"ميكاسك", allow_sudo=True))
async def kakashi(magisk):
    if magisk.fwd_from:
        return
    magisk_repo = "https://raw.githubusercontent.com/topjohnwu/magisk_files/"
    magisk_dict = {
        "⦁ **مستقر**": magisk_repo + "master/stable.json",
        "⦁ **بيتا**": magisk_repo + "master/beta.json",
        "⦁ **كاناري**": magisk_repo + "canary/canary.json",
    }
    releases = "**Latest Magisk Releases**\n\n"
    for name, release_url in magisk_dict.items():
        data = get(release_url).json()
        if "canary" in release_url:
            data["app"]["link"] = magisk_repo + "canary/" + data["app"]["link"]
            data["magisk"]["link"] = magisk_repo + "canary/" + data["magisk"]["link"]
            data["uninstaller"]["link"] = (
                magisk_repo + "canary/" + data["uninstaller"]["link"]
            )

        releases += (
            f'{name}: [ZIP v{data["magisk"]["version"]}]({data["magisk"]["link"]}) | '
            f'[APK v{data["app"]["version"]}]({data["app"]["link"]}) | '
            f'[Uninstaller]({data["uninstaller"]["link"]})\n'
        )
    await edit_or_reply(magisk, releases)


@icssbot.on(admin_cmd(outgoing=True, pattern=r"الجهاز(?: |$)(\S*)"))
@icssbot.on(sudo_cmd(pattern=r"الجهاز(?: |$)(\S*)", allow_sudo=True))
async def device_info(request):
    if request.fwd_from:
        return
    # get android device basic info from its codename
    textx = await request.get_reply_message()
    codename = request.pattern_match.group(1)
    if codename:
        pass
    elif textx:
        codename = textx.text
    else:
        await edit_or_reply(request, "`Usage: .device <codename> / <model>`")
        return
    data = json.loads(
        get(
            "https://raw.githubusercontent.com/androidtrackers/"
            "certified-android-devices/master/by_device.json"
        ).text
    )
    results = data.get(codename)
    if results:
        reply = f"**⌔∮ جاري البحث عن نتائج {codename}**:\n\n"
        for item in results:
            reply += (
                f"**الماركه**: {item['brand']}\n"
                f"**الاسم**: {item['name']}\n"
                f"**الموديل**: {item['model']}\n\n"
            )
    else:
        reply = f"**⌔∮ لم استطع العثور على نتائج {codename}!**\n"
    await edit_or_reply(request, reply)


@icssbot.on(admin_cmd(outgoing=True, pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)"))
@icssbot.on(sudo_cmd(pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)", allow_sudo=True))
async def codename_info(request):
    if request.fwd_from:
        return
    # search for android codename
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()

    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(" ")[0]
        device = " ".join(textx.text.split(" ")[1:])
    else:
        await edit_or_reply(request, "`Usage: .codename <brand> <device>`")
        return

    data = json.loads(
        get(
            "https://raw.githubusercontent.com/androidtrackers/"
            "certified-android-devices/master/by_brand.json"
        ).text
    )
    devices_lower = {k.lower(): v for k, v in data.items()}  # Lower brand names in JSON
    devices = devices_lower.get(brand)
    results = [
        i
        for i in devices
        if i["name"].lower() == device.lower() or i["model"].lower() == device.lower()
    ]
    if results:
        reply = f"**Search results for {brand} {device}**:\n\n"
        if len(results) > 8:
            results = results[:8]
        for item in results:
            reply += (
                f"**Device**: {item['device']}\n"
                f"**Name**: {item['name']}\n"
                f"**Model**: {item['model']}\n\n"
            )
    else:
        reply = f"`Couldn't find {device} codename!`\n"
    await edit_or_reply(request, reply)


@icssbot.on(admin_cmd(outgoing=True, pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)"))
@icssbot.on(sudo_cmd(pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)", allow_sudo=True))
async def devices_specifications(request):
    if request.fwd_from:
        return
    # Mobile devices specifications
    textx = await request.get_reply_message()
    brand = request.pattern_match.group(1).lower()
    device = request.pattern_match.group(2).lower()
    if brand and device:
        pass
    elif textx:
        brand = textx.text.split(" ")[0]
        device = " ".join(textx.text.split(" ")[1:])
    else:
        await edit_or_reply(request, "`Usage: .specs <brand> <device>`")
        return
    all_brands = (
        BeautifulSoup(
            get("https://www.devicespecifications.com/en/brand-more").content, "lxml"
        )
        .find("div", {"class": "brand-listing-container-news"})
        .findAll("a")
    )
    brand_page_url = None
    try:
        brand_page_url = [
            i["href"] for i in all_brands if brand == i.text.strip().lower()
        ][0]
    except IndexError:
        await edit_or_reply(request, f"`{brand} is unknown brand!`")
        return
    devices = BeautifulSoup(get(brand_page_url).content, "lxml").findAll(
        "div", {"class": "model-listing-container-80"}
    )
    device_page_url = None
    try:
        device_page_url = [
            i.a["href"]
            for i in BeautifulSoup(str(devices), "lxml").findAll("h3")
            if device in i.text.strip().lower()
        ]
    except IndexError:
        await edit_or_reply(request, f"`can't find {device}!`")
        return
    if len(device_page_url) > 2:
        device_page_url = device_page_url[:2]
    reply = ""
    for url in device_page_url:
        info = BeautifulSoup(get(url).content, "lxml")
        reply = "\n" + info.title.text.split("-")[0].strip() + "\n"
        info = info.find("div", {"id": "model-brief-specifications"})
        specifications = re.findall(r"<b>.*?<br/>", str(info))
        for item in specifications:
            title = re.findall(r"<b>(.*?)</b>", item)[0].strip()
            data = (
                re.findall(r"</b>: (.*?)<br/>", item)[0]
                .replace("<b>", "")
                .replace("</b>", "")
                .strip()
            )
            reply += f"**{title}**: {data}\n"
    await edit_or_reply(request, reply)


@icssbot.on(admin_cmd(outgoing=True, pattern=r"twrp(?: |$)(\S*)"))
@icssbot.on(sudo_cmd(pattern=r"twrp(?: |$)(\S*)", allow_sudo=True))
async def twrp(request):
    if request.fwd_from:
        return
    # get android device twrp
    textx = await request.get_reply_message()
    device = request.pattern_match.group(1)
    if device:
        pass
    elif textx:
        device = textx.text.split(" ")[0]
    else:
        await edit_or_reply(request, "`Usage: .twrp <codename>`")
        return
    url = get(f"https://dl.twrp.me/{device}/")
    if url.status_code == 404:
        reply = f"`Couldn't find twrp downloads for {device}!`\n"
        await edit_or_reply(request, reply)
        return
    page = BeautifulSoup(url.content, "lxml")
    download = page.find("table").find("tr").find("a")
    dl_link = f"https://dl.twrp.me{download['href']}"
    dl_file = download.text
    size = page.find("span", {"class": "filesize"}).text
    date = page.find("em").text.strip()
    reply = (
        f"**Latest TWRP for {device}:**\n"
        f"[{dl_file}]({dl_link}) - __{size}__\n"
        f"**Updated:** __{date}__\n"
    )
    await edit_or_reply(request, reply)


CMD_HELP.update(
    {
        "android": "**Plugin : **`android`\
\n\n  •  **Syntax : **`.magisk`\
\n  •  **Function :** __Get latest Magisk releases__\
\n\n  •  **Syntax : **`.device <codename>`\
\n  •  **Function :** __Get info about android device codename or model.__\
\n\n  •  **Syntax : **`.codename <brand> <device>`\
\n  •  **Function :** __Search for android device codename.__\
\n\n  •  **Syntax : **`.specs <brand> <device>`\
\n  •  **Function :** __Get device specifications info.__\
\n\n  •  **Syntax : **`.twrp <codename>`\
\n  •  **Function : **__Get latest twrp download for android device.__"
    }
)
