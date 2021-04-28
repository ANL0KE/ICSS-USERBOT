from . import asst_cmd, owner

H = "تيست واحد"

@asst_cmd("توتو")
@owner
async def _(e):
    await eor(e, H)
