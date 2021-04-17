from os import listdir, path
from typing import Any, Dict, List, Union

from yaml import safe_load

pyics = {}
pykim = path.join(path.dirname(path.realpath(__file__)), "tosh")

for file in listdir(pykim):
    if file.endswith(".yml"):
        code = file[:-4]
        pyics[code] = safe_load(
            open(path.join(pykim, file), encoding="UTF-8"),
        )


def pytosh(key: str) -> Any:
    return pyics[(bot.get("pyics" or "cmd"))][key]


def pyhiba() -> Dict[str, Union[str, List[str]]]:
    return {
        code: {
            "name": pyics[code]["name"],
            "author": pyics[code]["author"],
        }
        for code in pyics
    }
