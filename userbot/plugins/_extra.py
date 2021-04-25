# Icss - Userbot
# kimo: 
#   - for extra thing for Userbot

import random
from ..tosh import Fl, kk, urs, usre
from telethon import events
from telethon.tl.types import MessageEntityMentionName

L = random.choice(Fl)  
K = random.choice(kk)
  
# ^--------------------------------^
@icssbot.on(icss_cmd(pattern="kk"))
async def _(tosh):
    await eor(tosh, K)

# ^--------------------------------^

@icssbot.on(
    icss_cmd(pattern="نسبه نجاحك")
)
async def icss(ics):
    await eor(ics, urs.format(L))

# ^--------------------------------^

@icssbot.on(
    icss_cmd(pattern="نسبه الرجوله")
)
async def permalink(mention):
    user, custom = await get_user_from_event(mention)
    if not user:
        return
    if custom:
        await eor(mention, "⌔∮ نسبه الرجوله لــ [{}](tg://user?id={}) هيه {}".format(custom, user.id, L))
    else:
        tag = (
            user.first_name.replace("\u2060", "") if user.first_name else user.username
        )
        await eor(mention, "⌔∮ نسبه الرجوله لــ [{}](tg://user?id={}) هيه {}".format(tag, user.id, L))

async def get_user_from_event(event):
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
            await event.edit("{}".format(usre))
            return
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity("user")
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
# ^--------------------------------^
# extra_1 end:.
