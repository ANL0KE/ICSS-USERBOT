from asyncio import sleep


@icssbot.on(admin_cmd(pattern="schd (\d*) (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern="schd (\d*) (.*)", allow_sudo=True))
async def _(kimo):
    if kimo.fwd_from:
        return
    ics = ("".join(event.text.split(maxsplit=1)[1:])).split(" ", 1)
    message = ics[1]
    ttl = int(ics[0])
    try:
        await kimo.delete()
    except Exception as e:
        LOGS.info(str(e))
    await sleep(ttl)
    await kimo.respond(message)


CMD_HELP.update(
    {
        "schedule": "**Plugin : **`schedule`\
    \n\n**Syntax : **`.schd <time_in_seconds>  <message to send>`\
    \n**Function : **Send you the given message after that particular time\
    "
    }
)
