import random
import re

from userbot.utils import admin_cmd

# ===================================================== #


@icssbot.on(admin_cmd(pattern=r"scramble(\s+[\S\s]+|$)"))
async def scramble_message(i):
    reply_message = await i.get_reply_message()
    text = i.pattern_match.group(1) or reply_message.text
    words = re.split(r"\s", text)
    scrambled = map(scramble_word, words)
    text = " ".join(scrambled)
    await i.edit(text)


# ===================================================== #


def scramble_word(word):
    if len(word) < 4:
        return word

    first_letter = word[0]
    last_letter = word[-1]
    middle_letters = list(word[1:-1])
    random.shuffle(middle_letters)

    return first_letter + "".join(middle_letters) + last_letter
