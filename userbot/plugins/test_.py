Pic = "https://telegra.ph/file/91fff8d40afdf0bcf626b.jpg"
F = "- نـوࢪت "

@icss.on(icss_cmd(patter="ila"))
async def tt(icss):
    ics_id = await rd(icss)
    if Pic:
        await icss.client.send_file(icss.chat_id, F, Pic, reply_to=ics_id)
        await icss.delete()
