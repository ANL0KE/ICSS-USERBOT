import platform
import sys
from datetime import datetime

import psutil
from telethon import __version__

from . import ALIVE_NAME

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "icss"
# ============================================


@icssbot.on(admin_cmd(outgoing=True, pattern=r"spc$"))
@icssbot.on(sudo_cmd(allow_sudo=True, pattern=r"spc$"))
async def psu(event):
    uname = platform.uname()
    softw = "𓆩 𝑺𝑶𝑼𝑹𝑪𝑬 𝑰𝑪𝑺𝑺 𝑺𝒀𝑺𝑻𝑬𝑴 𝑰𝑵𝑭𝑶 𓆪\n"
    softw += f"⌔∮ System : `{uname.system}`\n"
    softw += f"⌔∮ Release  : `{uname.release}`\n"
    softw += f"⌔∮ Version  : `{uname.version}`\n"
    softw += f"⌔∮ Machine  : `{uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"⌔∮ Boot Time: `{bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**- CPU Info**\n"
    cpuu += "⌔∮ Physical cores   : `" + str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "⌔∮ Total cores      : `" + str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"⌔∮ Max Frequency    : `{cpufreq.max:.2f}Mhz`\n"
    cpuu += f"⌔∮ Min Frequency    : `{cpufreq.min:.2f}Mhz`\n"
    cpuu += f"⌔∮ Current Frequency: `{cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**- CPU Usage Per Core**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"⌔∮ Core {i}  : `{percentage}%`\n"
    cpuu += "**- Total CPU Usage**\n"
    cpuu += f"⌔∮ All Core: `{psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**- Memory Usage**\n"
    memm += f"⌔∮ Total     : `{get_size(svmem.total)}`\n"
    memm += f"⌔∮ Available : `{get_size(svmem.available)}`\n"
    memm += f"⌔∮ Used      : `{get_size(svmem.used)}`\n"
    memm += f"⌔∮ Percentage: `{svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**- Bandwith Usage**\n"
    bw += f"⌔∮ Upload  : `{get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"⌔∮ Download : `{get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{str(softw)}\n"
    help_string += f"{str(cpuu)}\n"
    help_string += f"{str(memm)}\n"
    help_string += f"{str(bw)}\n"
    help_string += "**Engine Info**\n"
    help_string += f"⌔∮ Python `{sys.version}`\n"
    help_string += f"⌔∮ Telethon `{__version__}`"
    await event.edit(help_string)


def get_size(inputbytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if inputbytes < factor:
            return f"{inputbytes:.2f}{unit}{suffix}"
        inputbytes /= factor


@icssbot.on(admin_cmd(pattern="cpu$"))
@icssbot.on(sudo_cmd(pattern="cpu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    cmd = "ics /proc/cpuinfo | grep 'model name'"
    o = (await _icssutils.runcmd(cmd))[0]
    await edit_or_reply(
        event, f"**[- icss’s](tg://need_update_for_some_feature/) CPU Model:**\n{o}"
    )


@icssbot.on(admin_cmd(pattern=f"sysd$", outgoing=True))
@icssbot.on(sudo_cmd(pattern=f"sysd$", allow_sudo=True))
async def sysdetails(sysd):
    cmd = "git clone https://github.com/dylanaraps/neofetch.git"
    await _catutils.runcmd(cmd)
    neo = "neofetch/neofetch --off --color_blocks off --bold off --cpu_temp C \
                    --cpu_speed on --cpu_cores physical --kernel_shorthand off --stdout"
    a, b, c, d = await _catutils.runcmd(neo)
    result = str(a) + str(b)
    await edit_or_reply(sysd, "Neofetch Result: `" + result + "`")


CMD_HELP.update(
    {
        "sysdetails": "**Plugin : **`sysdetails`\
        \n\n**Syntax : **`.spc`\
        \n**Function : **__Show system specification.__\
        \n\n**Syntax : **`.sysd`\
        \n**Function : **__Shows system information using neofetch.__\
        \n\n**Syntax : **`.cpu`\
        \n**Function : **__shows the cpu information__\
    "
    }
)
