import time

from . import StartTime, get_readable_time, mention, rd

@icss(
    icss_cmd(
       pattern="مده", outgoing=True
    )
)
@icss(
    sudo_cmd(
       pattern="مده", allow_sudo=True
    )
)
async def tim(lon):
    if lon.fwd_from:
        return
    await rd(lon)
    icst = await get_readable_time((time.time() - StartTime))
    await eor(
        lon, f"**{ICSST}**\n\n ⌔∮ المستخدم: {mention} \n⌔∮ المده: {icst}"
    )
