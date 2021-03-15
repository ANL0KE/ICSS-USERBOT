import time

from . import ALIVE_NAME, StartTime, get_readable_time, mention, reply_id

DEFULTUSER = ALIVE_NAME or "IcssBot"
ICSST = " اهلا بك عزيزي في بوت اكسس "


@icssbot.on(admin_cmd(pattern="مده", outgoing=True))
@icssbot.on(sudo_cmd(pattern="مده", allow_sudo=True))
async def tim(lon):
    if lon.fwd_from:
        return
    await reply_id(icsid)
    icst = await get_readable_time((time.time() - StartTime))
    await edit_or_reply(
        lon, f"**{ICSST}**\n\n ⌔∮ المستخدم: {mention} \n⌔∮ المده: {icst}"
    )
