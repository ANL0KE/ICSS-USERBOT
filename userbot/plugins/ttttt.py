Y = "hi"

@icss_cmd(pattern="Hello")
async def _(hi):
    await eor(hi, Y)
