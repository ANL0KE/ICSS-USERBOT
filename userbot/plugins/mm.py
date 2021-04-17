from resources._pykimo.cmd import titi
from . mention

@icssbot.on(
    icss_cmd(pattern="مدري")
)
async def hh(toti):
    await toti.edit(titi.format(mention)) 
