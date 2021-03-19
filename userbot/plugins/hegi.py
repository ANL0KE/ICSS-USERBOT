import asyncio
import random

Ulodya = [
   "𓄂"
   "⇲"
   "𖦼"
   "❒"
   "༕"
   "༗"
   ""
   "༗"
   "⌭"
]

@icss.on(
    icss_cmd(
       pattern="هاا", outgoing=True
    )
)
async def icss(ics):
   Ulo = random.choice(Ulodya)
   await ics.edit("وجع انتظر")
   await asyncio.sleep(3)
   await edit_or_reply(ics, Ulo)
