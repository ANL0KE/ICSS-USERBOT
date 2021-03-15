"""
©icss : @rruuurr
  - Icss TimeZone
  - TimeZone Commend 
  - `.الوقت`
"""

import os
from datetime import datetime as dt

from PIL import Image, ImageDraw, ImageFont
from pytz import country_names as i_n
from pytz import country_timezones as i_tz
from pytz import timezone as tz

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

LOCATION = Config.TZ
COUNTRY = Config.COUNTRY
TZ_NUMBER = Config.TZ_NUMBER


async def get_tz(con):
    if "(IQ)" in con: 
        con = con.replace("Iq", "IQ")
    if "(Uk)" in con:
        con = con.replace("Uk", "UK")
    if "(Us)" in con:
        con = con.replace("Us", "US")
    if " Of " in con:
        con = con.replace(" Of ", " of ")
    if "(Western)" in con:
        con = con.replace("(Western)", "(western)")
    if "Minor Outlying Islands" in con:
        con = con.replace("Minor Outlying Islands", "minor outlying islands")
    if "Nl" in con:
        con = con.replace("Nl", "NL")
    for icode in i_n:
        if con == i_n[icode]:
            return i_tz[icode]
    try:
        if i_n[con]:
            return i_tz[con]
    except KeyError:
        return


@icssbot.on(admin_cmd(outgoing=True, pattern="الوقت(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?"))
@icssbot.on(
    sudo_cmd(
        outgoing=True,
        pattern="الوقت(?: |$)(.*)(?<![0-9])(?: |$)([0-9]+)?",
        allow_sudo=True,
    )
)
async def time_func(tdata):
    con = tdata.pattern_match.group(1).title()
    tz_num = tdata.pattern_match.group(2)
    t_form = "%H:%M"
    d_form = "%d/%m/%y - %A"
    c_name = ""
    if len(con) > 4:
        try:
            c_name = i_n[con]
        except KeyError:
            c_name = con
        timezones = await get_tz(con)
    elif COUNTRY:
        c_name = COUNTRY
        tz_num = TZ_NUMBER
        timezones = await get_tz(COUNTRY)
    else:
        await edit_or_reply(
            tdata,
            f"𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 - 𝑻𝑰𝑴𝑬𝒁𝑶𝑵𝑬 𓆪 \n 𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻 \n⪼ الوقت  **{dt.now().strftime(t_form)}** في **{dt.now().strftime(d_form)}**",
        )
        return
    if not timezones:
        await edit_or_reply(tdata, "`Invaild country.`")
        return
    if len(timezones) == 1:
        time_zone = timezones[0]
    elif len(timezones) > 1:
        if tz_num:
            tz_num = int(tz_num)
            time_zone = timezones[tz_num - 1]
        else:
            return_str = f"⌔∮ {c_name} لها مناطق زمنيه متعدده :n\n"

            for i, item in enumerate(timezones):
                return_str += f"`{i+1}. {item}`\n"

            return_str += "\n`Choose one by typing the number "
            return_str += "in the command.`\n"
            return_str += f"`Example: .ctime {c_name} 2`"

            await edit_or_reply(tdata, return_str)
            return

    dtnow1 = dt.now(tz(time_zone)).strftime(t_form)
    dtnow2 = dt.now(tz(time_zone)).strftime(d_form)
    if c_name != COUNTRY:
        await edit_or_reply(
            tdata,
            f"`It's`  **{dtnow1}**` on `**{dtnow2}**  `in {c_name} ({time_zone} timezone).`",
        )
        return
    if COUNTRY:
        await edit_or_reply(
            tdata,
            f"`It's`  **{dtnow1}**` on `**{dtnow2}**  `here, in {COUNTRY}"
            f"({time_zone} timezone).`",
        )
        return


CMD_HELP.update(
    {
        "time": "**Plugin : **`time`\
        \n\n**Syntax : **`.الوقت <country name/code> <timezone number>` \
    \n**Function : **__Get the time of a country. If a country has multiple timezones, it will list all of them and let you select one. here are [country names](https://telegra.ph/country-names-10-24)__\
    }
)
