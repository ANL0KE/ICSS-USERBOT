from .Tosh import *

@icssbot.on(icss_cmd(pattern="م1"))
async def icss(tosh):
    await eor(tosh, R)

@icssbot.on(icss_cmd(pattern="م11"))
async def icss(tosh):
    await eor(tosh, L)
