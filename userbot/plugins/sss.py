from . import mention

@icssbot.on(icss_cmd(pattern="تفوو"))
async def icss(tosh):
    return await eor(
        tosh,
        f"هها {mention} هيع"
    )
