import os
import json

os.chdir(os.path.dirname(__file__))

ENCODER = json.JSONEncoder(indent=2, ensure_ascii=False)


def write(id: str):
    with open(f"models/block/{id}_side_double.json", "w") as double_file:
        o = {"parent": "block/fence_side_double", "textures": {"texture": f"block/{id}"}}
        double_file.write(ENCODER.encode(o))
    with open(f"blockstates/{id}_fence.json", "w") as blockstate_file:
        o = {
            "multipart": [
                {
                    "when": {
                        "OR": [
                            {"north": "false", "east": "false", "south": "false", "west": "false"},
                            {"north": "true", "east": "false", "south": "false", "west": "false"},
                            {"north": "false", "east": "true", "south": "false", "west": "false"},
                            {"north": "false", "east": "false", "south": "true", "west": "false"},
                            {"north": "false", "east": "false", "south": "false", "west": "true"},
                            {"north": "true", "east": "false", "south": "false", "west": "true"},
                            {"north": "true", "east": "true", "south": "false", "west": "false"},
                            {"north": "false", "east": "true", "south": "true", "west": "false"},
                            {"north": "false", "east": "false", "south": "true", "west": "true"},
                        ]
                    },
                    "apply": {"model": f"block/{id}_fence_post"},
                },
                {
                    "when": {"north": "true", "south": "false"},
                    "apply": {"model": f"block/{id}_fence_side", "uvlock": True},
                },
                {
                    "when": {"east": "true", "west": "false"},
                    "apply": {"model": f"block/{id}_fence_side", "y": 90, "uvlock": True},
                },
                {
                    "when": {"south": "true", "north": "false"},
                    "apply": {"model": f"block/{id}_fence_side", "y": 180, "uvlock": True},
                },
                {
                    "when": {"west": "true", "east": "false"},
                    "apply": {"model": f"block/{id}_fence_side", "y": 270, "uvlock": True},
                },
                {
                    "when": {"north": "true", "south": "true"},
                    "apply": {"model": f"block/{id}_fence_side_double", "uvlock": True},
                },
                {
                    "when": {"east": "true", "west": "true"},
                    "apply": {"model": f"block/{id}_fence_side_double", "y": 90, "uvlock": True},
                },
            ]
        }
        blockstate_file.write(ENCODER.encode(o))


for i in [
    "oak",
    "spruce",
    "birch",
    "jungle",
    "acacia",
    "dark_oak",
    "mangrove",
    "cherry",
    "pale_oak",
    "crimson",
    "warped",
]:
    write(i)


# todo: bamboo
