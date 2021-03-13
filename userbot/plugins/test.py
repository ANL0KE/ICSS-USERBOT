import asyncio

@icssbot.on(admin_cmd(pattern="هيج", outgoing=True))
async def icss(ics):
   await ics.edit(" هها هلو")
   await asyncio.sleep(1)
   await ics.edit(" هها هلو")
