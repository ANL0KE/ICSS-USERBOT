import random

from telethon import events


@icssbot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    ics = event.pattern_match.group(1)
    if ics == "kk":
        await event.edit("┏━━━┓\n┃┏━━┛\n┃┗━━┓\n┃┏━━┛\n┃┃\n┗┛")


@icssbot.on(admin_cmd(pattern="تحديث", outgoing=True))
async def icss(ics):
    await ics.edit("**⪼ هذا الامر غير موجود اذا اردت معرفت السبب راسل المطور 𓆰**")


ahk = [
    "100%",
    "90%",
    "80%",
    "70%",
    "60%",
    "50%",
    "40%",
    "30%",
    "20%",
    "10%",
    "0%",
]


@icssbot.on(admin_cmd(pattern="نسبه نجاحك", outgoing=True))
async def icss(ics):
    uu = random.choice(ahk)
    return await ics.edit(f"**⌔∮ نسبه نجاحك هيه -** `{uu}`")


from telethon.tl.types import MessageEntityMentionName

ppp = [
    "100% 🔱💕.",
    "90%",
    "80%",
    "70%",
    "60%",
    "50%",
    "40%",
    "30%",
    "20%",
    "10%",
    "0%",
]


@icssbot.on(admin_cmd(pattern="نسبه الرجوله(?: |$)(.*)"))
@icssbot.on(sudo_cmd(pattern="نسبه الرجوله(?: |$)(.*)", allow_sudo=True))
async def permalink(mention):
    ioi = random.choice(ppp)
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await edit_or_reply(
            mention,
            f"⌔∮ نسبه الرجوله لـ [{custom}](tg://user?id={user.id}) هيه {ioi} ",
        )
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await edit_or_reply(
            mention,
            f"⌔∮ نسبه الرجوله لـ [{tag}](tg://user?id={user.id}) هيه {ioi} ",
        )


async def get_user_from_event(event):
    """ Get the user from argument or replied message. """
    args = event.pattern_match.group(1).split(":", 1)
    extra = None
    if event.reply_to_msg_id and len(args) != 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj, extra


async def ge(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj
