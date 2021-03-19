from . import CMD_LIST, ALIVE_NAME
from platform import uname
import sys
from telethon import events, functions, version


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Icss - Userbot"


@borg.on(
    icss_cmd(
       pattern=r"hh ?(.*)", outgoing=True
    )
)
@borg.on(
    sudo_cmd(
       pattern=r"hh ?(.*)", outgoing=True, allow_sudo=True
    )
)
async def cmd_list(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/" , "#", "-", "_", "@"):
        tgbu = Config.TG_BOT_USERNAME
        input_str = event.pattern_match.group(1)
        if tgbu is None or input_str == "text":
            string = ""
            for i in CMD_LIST:
                string += "â¡ï¸" + i + "\n"
                for iter_list in CMD_LIST[i]:
                    string += "    " + str(iter_list) + ""
                    string += "\n"
                string += "\n"
            if len(string) > 69:
                with io.BytesIO(str.encode(string)) as out_file:
                    out_file.name = "cmd.txt"
                    await bot.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="Commends In Icss - Userbot",
                        reply_to=reply_to_id
                    )
                    await event.delete()
            else:
                await event.edit(string)
        elif input_str:
            if input_str in CMD_LIST:
                string = "الاوامر الموجوده في {}:\n".format(input_str)
                for i in CMD_LIST[input_str]:
                    string += "  " + i
                    string += "\n"
                await event.edit(string)
            else:
                await event.edit(input_str + " is not a valid plugin!")
        else:
            help_string = f"""𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑯𝑬𝑳𝑷 𝑴𝑬𝑵𝑼 𓆪\n ⌔∮ اهلا بك عزيزي DEFAULTUSER}
هنا ستجد جميع الاوامر فقط اضغط على اسم الملف وستضهر الاوامر الخاصه به"""
            results = await bot.inline_query(  # pylint:disable=E0602
                tgbu,
                help_string
            )
            await results[0].click(
                event.chat_id,
                reply_to=event.reply_to_msg_id,
                hide_via=True
            )
            await event.delete()
