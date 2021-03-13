# fonts for icss edit by: @rruuurr

from . import fonts


@icssbot.on(admin_cmd(pattern="زغرفه1(?: |$)(.*)", command="fmusical"))
@icssbot.on(sudo_cmd(pattern="زغرفه1(?: |$)(.*)", command="fmusical", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            musicalcharacter = fonts.musicalfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, musicalcharacter)
    await edit_or_reply(event, string)


@icssbot.on(admin_cmd(pattern="زغرفه2(?: |$)(.*)", command="ancient"))
@icssbot.on(sudo_cmd(pattern="زغرفه2(?: |$)(.*)", command="ancient", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normalfontcharacter in string:
        if normalfontcharacter in fonts.normalfont:
            ancientcharacter = fonts.ancientfont[
                fonts.normalfont.index(normalfontcharacter)
            ]
            string = string.replace(normalfontcharacter, ancientcharacter)
    await edit_or_reply(event, string)


@icssbot.on(admin_cmd(pattern="زغرفه3(?: |$)(.*)", command="vapor"))
@icssbot.on(sudo_cmd(pattern="زغرفه3(?: |$)(.*)", command="vapor", allow_sudo=True))
async def vapor(vpr):
    reply_text = []
    textx = await vpr.get_reply_message()
    message = vpr.pattern_match.group(1)
    if message:
        pass
    elif textx:
        message = textx.text
    else:
        await edit_or_reply(vpr, "`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
        return

    for charac in message:
        if 0x21 <= ord(charac) <= 0x7F:
            reply_text.append(chr(ord(charac) + 0xFEE0))
        elif ord(charac) == 0x20:
            reply_text.append(chr(0x3000))
        else:
            reply_text.append(charac)

    await edit_or_reply(vpr, "".join(reply_text))


@icssbot.on(admin_cmd(pattern="زغرفه4(?: |$)(.*)", command="smallcaps"))
@icssbot.on(sudo_cmd(pattern="زغرفه4(?: |$)(.*)", command="smallcaps", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smallcapscharacter = fonts.smallcapsfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smallcapscharacter)
    await edit_or_reply(event, string)


@icssbot.on(admin_cmd(pattern="زغرفه5(?: |$)(.*)", command="blackbf"))
@icssbot.on(sudo_cmd(pattern="زغرفه5(?: |$)(.*)", command="blackbf", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblesblackcharacter = fonts.bubblesblackfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblesblackcharacter)
    await edit_or_reply(event, string)


@icssbot.on(admin_cmd(pattern="زغرفه6(?: |$)(.*)", command="bubbles"))
@icssbot.on(sudo_cmd(pattern="زغرفه6(?: |$)(.*)", command="bubbles", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblescharacter = fonts.bubblesfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, bubblescharacter)
    await edit_or_reply(event, string)


@icssbot.on(admin_cmd(pattern="زغرفه7(?: |$)(.*)", command="tanf"))
@icssbot.on(sudo_cmd(pattern="زغرفه7(?: |$)(.*)", command="tanf", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            tantextcharacter = fonts.tantextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, tantextcharacter)
    await edit_or_reply(event, string)


@icssbot.on(admin_cmd(pattern="زغرفه8(?: |$)(.*)", command="boxf"))
@icssbot.on(sudo_cmd(pattern="زغرفه8(?: |$)(.*)", command="boxf", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            littleboxtextcharacter = fonts.littleboxtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, littleboxtextcharacter)
    await edit_or_reply(event, string)


@icssbot.on(admin_cmd(pattern="زغرفه9(?: |$)(.*)", command="smothtext"))
@icssbot.on(sudo_cmd(pattern="زغرفه9(?: |$)(.*)", command="smothtext", allow_sudo=True))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text
    if not args:
        await edit_or_reply(event, "What I am Supposed to change give text")
        return
    string = "  ".join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smothtextcharacter = fonts.smothtextfont[
                fonts.normaltext.index(normaltextcharacter)
            ]
            string = string.replace(normaltextcharacter, smothtextcharacter)
    await edit_or_reply(event, string)


CMD_HELP.update(
    {
        "fonts": """**Plugin : **`fonts`

**⌔∮ الاوامر الموجوده في ملف fonts: **
  •  `.زغرفه1`
  •  `.زغرفه2`
  •  `.زغرفه3`
  •  `.زغرفه4`
  •  `.زغرفه5`
  •  `.زغرفه6`
  •  `.زغرفه7`
  •  `.زغرفه8`
  •  `.زغرفه9`

**Function : **__Reply the command to the text message or give input along with command to convert that text to given font style__"""
    }
)
