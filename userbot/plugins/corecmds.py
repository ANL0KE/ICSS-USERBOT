import asyncio
import os
from datetime import datetime
from pathlib import Path

from ..utils import load_module, remove_plugin
from . import ALIVE_NAME, CMD_LIST, SUDO_LIST, M

DELETE_TIMEOUT = 5
thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


@icssbot.on(admin_cmd(pattern="اضافه$"))
@icssbot.on(sudo_cmd(pattern="اضافه$", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "userbot/plugins/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await edit_or_reply(
                    event,
                    f"**⌔∮ تم اضافه الملف** `{os.path.basename(downloaded_file_name)}` **في سورس اكسس.** ",
                )
            else:
                os.remove(downloaded_file_name)
                await edit_or_reply(
                    event, "**⌔∮ هذا الملف مضاف بالـفعل**/pre-installed."
                )
        except Exception as e:
            await edit_or_reply(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@icssbot.on(admin_cmd(pattern=r"حمل (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern=r"حمل (.*)", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await edit_or_reply(event, f"**⌔∮ تم تحميـل الملف** {shortname} **في اكسس.**")
    except Exception as e:
        await edit_or_reply(
            event,
            f"**⌔∮ لايمكن تحميل** {shortname} **بسبب الخطا التالي**.\n⌔∮ - {str(e)} .",
        )


@icssbot.on(admin_cmd(pattern=r"ارسل (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern=r"ارسل (.*)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    reply_to_id = await reply_id(event)
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = f"./userbot/plugins/{input_str}.py"
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        ics = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            thumb=thumb,
        )
        end = datetime.now()
        ms = (end - start).seconds
        await event.delete()
        await ics.edit(
            f"**⌔∮ اسم الاضافه : {input_str}**\n**⌔∮ الوقت المستغرق : {ms}ثانيه**\n**⌔∮ للمستخدم :** {M}"
        )
    else:
        await eor(event, "**⌔∮ لاتوجد اضافه بهذا الاسم**")


@icssbot.on(admin_cmd(pattern=r"unload (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern=r"unload (.*)", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    try:
        remove_plugin(shortname)
        await edit_or_reply(event, f"Unloaded {shortname} successfully")
    except Exception as e:
        await edit_or_reply(event, f"Successfully unload {shortname}\n{str(e)}")


@icssbot.on(admin_cmd(pattern=r"الغاء الاضافه (.*)", outgoing=True))
@icssbot.on(sudo_cmd(pattern=r"الغاء الاضافه (.*)", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match.group(1)
    path = Path(f"userbot/plugins/{shortname}.py")
    if not os.path.exists(path):
        return await edit_delete(
            event, f"There is no plugin with path {path} to uninstall it"
        )
    os.remove(path)
    if shortname in CMD_LIST:
        CMD_LIST.pop(shortname)
    if shortname in SUDO_LIST:
        SUDO_LIST.pop(shortname)
    if shortname in CMD_HELP:
        CMD_HELP.pop(shortname)
    try:
        remove_plugin(shortname)
        await eor(event, "**⌔∮ اهلا عزيزي : {}**\n**⌔∮ تم الغاء تنزيل الاضافه {} بنجاح **".format(M, shortname))
    except Exception as e:
        await eor(event, f"**⌔∮ تم الغاء تنزيل الاضافه {shortname} بنجاح ** {shortname}\n{str(e)}")


CMD_HELP.update(
    {
        "corecmds": """**Plugin : **`corecmds`

  •  **Syntax : **`.install`
  •  **Function : **__Reply to any external plugin to install in bot__ 
  
  •  **Syntax : **`.load <plugin name>`
  •  **Function : **__To load that plugin again__
  
  •  **Syntax : **`.send <plugin name>`  
  •  **Function : **__to send any plugin__
  
  •  **Syntax : **`.unload <plugin name>`
  •  **Function : **__To stop functioning of that plugin__ 
  
  •  **Syntax : **`.uninstall <plugin name>`
  •  **Function : **__To stop functioning of that plugin and remove that plugin from bot__ 
  
**Note : **__To unload a plugin permenantly from bot set __`NO_LOAD`__ var in heroku with that plugin name with space between plugin names__"""
    }
)
