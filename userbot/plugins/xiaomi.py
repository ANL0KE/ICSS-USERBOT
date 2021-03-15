from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError


@icssbot.on(admin_cmd(pattern="firmware(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="firmware(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    firmware = f"firmware"
    icse = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{firmware} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await icse.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@icssbot.on(admin_cmd(pattern="vendor(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="vendor(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    vendor = f"vendor"
    icse = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{vendor} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await icse.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@icssbot.on(admin_cmd(pattern="specs(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="specs(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    specs = f"specs"
    icse = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{specs} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await icse.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@icssbot.on(admin_cmd(pattern="fastboot(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="fastboot(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    fboot = f"fastboot"
    icse = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{fboot} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await icse.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@icssbot.on(admin_cmd(pattern="recovery(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="recovery(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    recovery = f"recovery"
    icse = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{recovery} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await icse.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@icssbot.on(admin_cmd(pattern="pb(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="pb(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    pitch = f"pb"
    icse = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{pitch} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await icse.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


@icssbot.on(admin_cmd(pattern="of(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="of(?: |$)(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    link = event.pattern_match.group(1)
    ofox = f"of"
    icse = await edit_or_reply(event, "```Processing```")
    async with event.client.conversation("@XiaomiGeeksBot") as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=774181428)
            )
            await conv.send_message(f"/{ofox} {link}")
            respond = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await icse.edit("```Unblock @XiaomiGeeksBot plox```")
            return
        else:
            await icse.delete()
            await event.client.forward_messages(event.chat_id, respond.message)


CMD_HELP.update(
    {
        "xiaomi": "**Plugin :** `Xiaomi`\
        \n\n__**For Xiaomeme devices only!**__\
        \n\n**Syntax :** `.firmware` (codename)\
        \n**Function : **Get lastest Firmware\
        \n\n**Syntax :** `.vendor` (codename)\
        \n**Function : **Get lastest Vendor\
        \n\n**Syntax :** `.pb` (codename)\
        \n**Function : **Get latest PBRP\
        \n\n**Syntax :** `.specs` (codename)\
        \n**Function : **Get quick spec information about device\
        \n\n**Syntax :** `.fastboot` (codename)\
        \n**Function : **Get latest fastboot MIUI\
        \n\n**Syntax :** `.recovery` (codename)\
        \n**Function : **Get latest recovery MIUI\
        \n\n**Syntax :** `.of` (codename)\
        \n**Function : **Get latest ORangeFox Recovery"
    }
)
