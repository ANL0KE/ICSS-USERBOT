# Hey There

_tts = (
""" Google Text to Speech
Available Commands:
.tts LanguageCode as reply to a message
.tts LangaugeCode | text to speak
"""
)

import asyncio
import os
import subprocess
from datetime import datetime

from gtts import gTTS

from . import deEmojify


@icssbot.on(
    icss_cmd(pattern="صوت كوكل (.*)")
)
@icssbot.on(sudo_cmd(pattern="صوت كوكل (.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await eor(event, "**⌔∮ قم برد على الرساله**")
        return
    text = deEmojify(text.strip())
    lan = lan.strip()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    required_file_name = "./temp/" + "voice.ogg"
    try:
        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
            required_file_name,
            "-map",
            "0:a",
            "-codec:a",
            "libopus",
            "-b:a",
            "100k",
            "-vbr",
            "on",
            required_file_name + ".opus",
        ]
        try:
            t_response = subprocess.check_output(
                command_to_execute, stderr=subprocess.STDOUT
            )
        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:
            await event.edit(str(exc))
        else:
            os.remove(required_file_name)
            required_file_name = required_file_name + ".opus"
        end = datetime.now()
        ms = (end - start).seconds
        await event.client.send_file(
            event.chat_id,
            required_file_name,
            reply_to=event.message.reply_to_msg_id,
            allow_cache=False,
            voice_note=True,
        )
        os.remove(required_file_name)
        event = await eor(
            event, "**⌔∮ تم معالجة {} ({}) في وقت {} ثانيه !**".format(text[0:97], lan, ms)
        )
        await asyncio.sleep(5)
        await event.delete()
    except Exception as e:
        await eor(event, str(e))


CMD_HELP.update({"tts": "**Plugin : tts**\n " + "{_tts}"})
