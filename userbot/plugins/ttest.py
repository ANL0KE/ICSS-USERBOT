from datetame import datetime

@icssbot.on(
    icss_cmd(pattern="ها")
)
async def _(e):
    icst = e.txt
    yar = icst[4:9]
    if not yar:
       await eor(e, "هها هلو")
    YearNow = datetime.now().year
    MyAge = (int(YearNow) - int(yar))
    await eor(e, "عمرك هوه {}".format(MyAge))
