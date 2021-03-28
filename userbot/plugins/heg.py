import time

from . import StartTime, mention
from . imporr relly_id as rd
from . import get_readable_time as grt

@icssbot.on(
    icss_cmd(
       pattern="مده", outgoing=True
    )
)
@icssbot.on(
    sudo_cmd(
       pattern="مده", allow_sudo=True
    )
)
async def tim(lon):
    if lon.fwd_from:
        return
    await rd(lon)
    icst = await grt((time.time() - StartTime))
    await eor(
        lon, f"**{ICSST}**\n\n ⌔∮ المستخدم: {mention} \n⌔∮ المده: {icst}"
    )
