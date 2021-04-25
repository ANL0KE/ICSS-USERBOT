Pic = "https://telegra.ph/file/91fff8d40afdf0bcf626b.jpg"
F = "- نـوࢪت "

@icss.on(icss_cmd(patter="ila"))
async def tt(icss):
    await icss.client.send_file(F, pic)
    await icss.delete()
