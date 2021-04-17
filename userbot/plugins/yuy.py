from . import ToK, mention

@icssbot.on(
icss_cmd(pattern="ختبار")
)
async def _(tosh):
    await eor(tosh, ToK.format(mention))
