# icss fonts

from icsfont import *


@icssbot.on(admin_cmd(pattern="ho ?(.*)"))
async def icsf9(ics):

    kim = ics.pattern_match.group(1)
    if not kim:
        get = await ics.get_reply_message()
        kim = get.text
    if not kim:
        await ics.edit("What I am Supposed to Weebify? Please Give Text Sir")
        return
    string = "".join(kim).lower()
    for normiecharacter in string:
        if normiecharacter in icsf1:
            wcharacter = icsf9[icsf1.index(normiecharacter)]
            string = string.replace(normiecharacter, wcharacter)
    await ics.edit(string)
