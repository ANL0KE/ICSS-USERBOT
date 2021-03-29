#  ICSS - USERBOT
#  TELE - @NIIIN2
#  OWNER - KIMO


import time
from datetime import datetime
from ..Config import Config

OWNER_ID = Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME if Config.ALIVE_NAME else "@rruuurr"
# start-other disabled
startotherdis = f"Hi there. I am {ALIVE_NAME}'s bot. Nice to see you here."
# start-other enabled
if Config.PBS_MSSG is None:
    MSSG = f"Hi there, I am {ALIVE_NAME}'s personal bot.\nYou can contact him through me 😌.\nHave a nice time!"
else:
    MSSG = Config.PBS_MSSG
startotherena = MSSG

# start-owner
startowner = f"Welcome back {ALIVE_NAME}. Choose the options available from below:"

# for ping
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


xstart = datetime.now()
xend = datetime.now()
ms = (xend - xstart).microseconds / 1000
ping = f"🏓Pong\nPing speed: {ms}"
