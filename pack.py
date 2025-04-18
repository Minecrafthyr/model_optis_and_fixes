# Modify this file to custom output

from defines import *

tree: tree_pack_tuple = (
    "Base",
    "Resource Fixes Lite",
    (
        "Full",
        "Resource Fixes",
        (
            "Textured",
            "Resource Fixes Textured",
            (
                [
                    "Tweak/Consistent Planes",
                    "Tweak/3D",
                    "Tweak/Animation",
                    "Tweak/Better Cross",
                    "Tweak/Block States",
                    "Tweak/Fast Waterlogged Leaves",
                    "Tweak/Fire",
                    "Tweak/Shadeless Lights",
                    "Tweak/Wide Bamboo",
                    "Tweak/Misc",
                ],
                "Resource Fixes Extra",
                None,
            ),
        ),
    ),
)

pack = tree_pack_input_data(
    tree,
    "Assets/",
    "ZippedPacks/",
)
