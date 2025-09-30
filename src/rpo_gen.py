import os
import json
from typing import Any

type StrDict = dict[str, str]
type AnyDict = dict[str, Any]
type NestedAnyDict = dict[str, NestedAnyDict | AnyDict]
op = os.path


def add_prefix(prefix: str, target: StrDict):
    new = {}
    for _k, _v in target.items():
        new[prefix + _k] = _v
    return new


os.chdir(op.dirname(__file__))

with open("rpo_config.json", encoding="utf-8") as config:
    data: list[AnyDict] = json.load(config)

translates = dict[str, StrDict]()
pack = str()
variant = str()
conf: AnyDict = {}


ENCODER = json.JSONEncoder(indent=2, ensure_ascii=False)


def write_files():
    name = f"res{pack}{variant}"
    tname = "rpo." + name
    os.makedirs(f"{pack}/{variant}/Respackopts/assets/minecraft/lang", exist_ok=True)
    with open(
        f"{pack}/{variant}/Respackopts/respackopts.json5", "w", encoding="utf-8"
    ) as c:
        c.write(
            ENCODER.encode(
                {
                    "id": name,
                    "version": 13,
                    "capabilities": ["FileFilter"],
                    "conf": conf,
                }
            )
        )

    for lang, _tr in translates.items():
        with open(
            f"{pack}/{variant}/Respackopts/assets/minecraft/lang/{lang}.json",
            "w",
            encoding="utf-8",
        ) as f:
            new_dict = {}
            if lang == "en_us":
                new_dict[f"{tname}"] = f"Resource {pack} {variant}"
            elif lang == "zh_cn":
                new_dict[f"{tname}"] = (
                    f"资源{_tr[pack_l]}【{_tr[pack_l+"."+variant_l]}】"
                )
            new_dict.update(add_prefix(tname + ".", _tr))
            f.write(ENCODER.encode(new_dict))


for item in data:
    _pack = item.get("pack", None)
    if _pack is not None:
        pack = _pack
    _variant = item.get("variant", None)
    if _variant is not None:
        variant = _variant
    pack_l = pack.lower()
    variant_l = variant.lower()
    _conf = item.get("conf", None)
    base_trans = item.get("base_trans", None)
    trans = item.get("trans", None)
    
    if _conf is not None:
        if conf.get(pack_l, None) is None:
            conf[pack_l] = {}
        conf[pack_l][variant_l] = _conf
    if base_trans is not None:
        for k, v in base_trans.items():
            if translates.get(k, None) is None:
                translates[k] = {}
            translates[k].update(v)
    if trans is not None:
        for k, v in trans.items():
            if translates.get(k, None) is None:
                translates[k] = {}
            translates[k].update(add_prefix(f"{pack_l}.{variant_l}.", v))
    write_files()
