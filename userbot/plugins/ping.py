# ping for icss
# by: @rruuurr

import time
from datetime import datetime

from . import StartTime, get_readable_time, mention, reply_id


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for event in range(len(time_list)):
        time_list[event] = str(time_list[event]) + time_suffix_list[event]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


# Dev: @rruuurr


@icssbot.on(admin_cmd(pattern="بنك$"))
@icssbot.on(sudo_cmd(pattern="بنك$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    event = await edit_or_reply(event, "⌭")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await reply_id(event)
    get_readable_time((time.time() - StartTime))
    await event.edit(
        f"⌔∮ **سرعه الاستجابه ↫** `{ms}` ** ⇲**\n ⌔∮ **المستخدم ↫** {mention} **⇱**"
    )
