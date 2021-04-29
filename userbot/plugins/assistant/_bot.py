from . import *

@asst_cmd("alive")
async def _(e):
    await asst.send_file(e.chat_id, asst_p, caption=asst_c)
