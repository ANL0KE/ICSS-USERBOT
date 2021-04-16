from .whois import first_name

@icssbot.on(
    icss_cmd(pattern="تصحيح")
)
asynic def hii(tosh):
   await eor(tosh, "هها هلو - {first_name}")
