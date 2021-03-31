#  ICSS - USERBOT
#  TELE - @NIIIN2
#  OWNER - KIMO


import time
from datetime import datetime
from userbot.Config import Config
from .. import mention

# Kimo
K = "https://t.me/rruuurr"
D = "** ⌔∮ مطور بوت اكسس**"

# about the bot
TOSH = "**⌔∮ اهلا بك هذا هو بوت اكسس وسورس اكسس وهذا السورس او يوزر بوت هو عربي توجد الكثير من الاضافات المهمه ولغير مهمه والممتعه ايضا وتوجد الزغرفه والمتحركات ولكثير من الاضافات الاخرى ويمكنك من خلال هذا البوت تغير #رسالة_الخاص او الحمايه وايضا تغير #صوره_الخاص اي عند مراسلتك من قبل شخص ستظهر له الصوره مع الرساله التي وضعتها في البدايه اذا تحب ذالك ويمكنك ايضا تغير #ونص_الايڤ و #صوره_الايڤ وايضا تغير #رسالة_البدء اي عند بدء بوتك من قبل شخص اخر ستظهر له هذه الرساله والكثير ينتظرك 💕⚜️.**"

OWNER_ID = Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME if Config.ALIVE_NAME else "@rruuurr"
# start-other disabled
startotherdis = f"**⌔∮ اهلا بك انا مساعد {mention} سعيد برؤيتك هنا**"
# start-other enabled
if Config.TOSH_START is None:
    MSSG = f"**⌔∮ اهلا بك انا مساعد {mention} تستطيع التواصل معه من خلالي**"
else:
    MSSG = Config.TOSH_START
startotherena = MSSG

# start-owner
startowner = f"** ⌔∮ اهلا بك مجدداً {ALIVE_NAME}. اختر احد الخيارات الاتيه:**"

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
