from resources.strings import *

@icssbot.on(
    icss_cmd(
    outgoing=True, 
    pattern="السورس$"
    )
)
@icssbot.on(
    sudo_cmd(pattern="السورس$", allow_sudo=True)
)
async def ica(icss):
    ics_id = await rd(icss)
    await icss.client.send_file(
        icss.chat_id, ICSS_IMG, caption=ics_c, reply_to=ics_id
    )
    await icss.delete()

CMD_HELP.update({"alive": "{}".format(alv)})
