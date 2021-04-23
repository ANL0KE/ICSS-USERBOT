"""
SOURCE ICSS
@rruuurr
"""

import io
import sys
import traceback
from ..tosh import C


@icssbot.on(
    icss_cmd(pattern="حاسبه (.*)")
)
@icssbot.on(sudo_cmd(
               pattern="حاسبه (.*)", 
               allow_sudo=True)
           )
async def _(ics):
    tosh = ics.text.split(" ", maxsplit=1)[1]
    tsh = await eor(ics, "**⌔∮ يتم الحل… **")
    osr = sys.stderr
    ost = sys.stdout
    rot = sys.stdout = io.StringIO()
    reor = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    kim = "print(%s)"% tosh
    try:
        await aexec(kim, tsh)
    except Exception:
        exc = traceback.format_exc()
    stdout = rot.getvalue()
    stderr = reor.getvalue()
    sys.stdout = ost
    sys.stderr = osr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Sorry I can't find result for the given equation"
    fot = (C.format(tosh, evaluation)
    await eor(tsh, fot)


async def aexec(code, event):
    exec(f"async def __aexec(event): " + "".join(f"\n {l}" for l in code.split("\n")))
    return await locals()["__aexec"](event)


tosh_HELP.update(
    {
        "calc": "**Plugin : **`calc`\
        \n\n• **Syntax : **`.حاسبه ` \
        \n• **Function : **للحساب مثال (2*2) "
    }
)
