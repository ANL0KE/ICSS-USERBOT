from . import asst_cmd, owner

H = "تيست واحد"

@asst_cmd("توتو")
async def _(e):
    await e.reply(H)
