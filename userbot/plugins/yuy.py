from . import 2K, mention

@icssbot.on(
icss_cmd(pattern="ختبار")
)
async def _(tosh):
    await eor(tosh, 2K.format(mention))
