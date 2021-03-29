#    Icss - Userbot
#    Owner - @rruuurr

from . import R, K

@icssbot.on(icss_cmd(pattern="repo$"))
@icssbot.on(sudo_cmd(pattern="repo$", allow_sudo=True))
async def icsrepo(icsp):
    await eor(icsp, R)


@icssbot.on(icss_cmd(pattern="رابط السورس$"))
@icssbot.on(sudo_cmd(pattern="رابط السورس$", allow_sudo=True))
async def icsrepo(icsp):
    await eor(icsp, K)


