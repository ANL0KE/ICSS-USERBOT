import time
from datetime import datetime as dt
from . import StartTime, mention
from .ping import get_readable_time as grt

@icssbot.on(
    icss_cmd(pattern="بنك$")
)
async def _(tosh):
    start = dt.now()
    e = await eor(tosh, "⌭")
    end = dt.now()
    ms = (end - start).microseconds / 1000
    grt((time.time() - StartTime))
    await e.edit(ToK.format(ms, mention))
