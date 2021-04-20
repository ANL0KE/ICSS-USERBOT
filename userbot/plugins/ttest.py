import datetime


@icssbot.on(
    icss_cmd(pattern="العمر$")
)
async def _(e):
    icst = e.txt
    yar = icst[6:11]
    Dbt = yar
    YearNow = datetime.now().year
    MyAge = (int(YearNow) - int(Dbt))
    await eor(e, "عمرك هوه {}".format(MyAge))
