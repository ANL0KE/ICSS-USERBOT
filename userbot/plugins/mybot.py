# Hey There 

from . import Mb
from ..tosh import TBOT

@icssbot.on(
    icss_cmd(
       pattern="بوتي", outgoing=True
    )
)
async def mybot(k):
    await eor(k, Mb.format(TBOT))
