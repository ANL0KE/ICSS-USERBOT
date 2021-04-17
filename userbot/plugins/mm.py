from resources.pybsk import pytosh
from . import mention

@icssbot.on(
    icss_cmd(pattern="مدري")
)
async def mdry(tf):
    await tf.edit(pytosh("titi").format(mention)) 
