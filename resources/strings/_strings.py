# im noob in this but I try, from Ultroid

from yaml import salf_load
from os import listdir, path
from typing import Any, Dict, List, Union

strfile = {}
strings = path.join(path.dirname(path.realpath(__file__)), "strings")

for file in listdir(strings):
    if file.endswith(".yml"):
        code = file[:-4]
        strfile[code] = safe_load(
            open(path.join(stringsr, strfile), encoding="UTF-8"),
        )


def string(key: str) -> Any:
    return strfile[("cmd")][key]
    

def stringfile() -> Dict[str, Union[str, List[str]]]:
    return {
        code: {
            "name": strfile[code]["name"],
            "authors": strfile[code]["authors"],
        }
        for code in strfile
    }
