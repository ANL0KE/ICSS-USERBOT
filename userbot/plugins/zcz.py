from .whois import first_name

@icssbot.on(
    icss_cmd(pattern="تصحيح")
)
async def hii(tosh):
    await eor(tosh, f"هها هلو - {first_name}")
