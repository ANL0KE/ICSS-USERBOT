import time
from telethon import events
from datetime import datetime
from . import Ping
from .. import StartTime

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

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

@tgbot.on(
    events.NewMessage(pattern=("بنك"))
)
async def _(e):
    Start = datetime.now()
    End = datetime.now()
    Ms = (end - start).microseconds / 1000
    UpTime = get_readable_time((time.time() - StartTime))
    await e.reply(Ping.format(Ms, UpTime))
