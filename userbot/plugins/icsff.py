# icss fonts

icsff1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
icsff2 = ['𝙖','𝙗','𝙘','𝙙','𝙚','𝙛','𝙜','𝙝','𝙄','𝙟','𝙠','𝙡','𝙢','𝙣','𝙤','𝙥','𝙦','𝙧','𝙨','𝙩','𝙪','𝙫','𝙬','𝙭','𝙮','𝙯']



@icssbot.on(admin_cmd(pattern="ho ?(.*)"))
async def icsf2(ics):

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
            wcharacter = icsf2[icsf1.index(normiecharacter)]
            string = string.replace(normiecharacter, wcharacter)
    await ics.edit(string)
