Repo = "https://github.com/ANL0KE/kimo-kimo/blob/master/kimo.py"

from repo import *

@icss.on(
    icss_cmd(pattern="تيت")
)
async def tt(tosh):
   await eor(tosh,Masg.format(mention, TBOT))
