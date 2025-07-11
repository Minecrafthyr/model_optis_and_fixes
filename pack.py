# Modify this file to custom output

from defines import *

tree: tree_pack_tuple = (
    "Base",
    "Resource Fixes Lite",
    (
        [
            "Full/Display",
            "Full/Glass",
            "Full/Misc",
            "Full/Random Rotate",
            "Full/Respackopts",
        ],
        "Resource Fixes",
        (
            [
                "Textured/End Portal Frame Fix",
                "Textured/Firefly Bush Fix",
                "Textured/Item Frame",
                "Textured/Misc",
                "Textured/Modern Spectator GUI",
                "Textured/Tall Seagrass Fix",
            ],
            "Resource Fixes Textured",
            (
                [
                    "Extra/3D Iron Bars",
                    "Extra/Consistent Planes",
                    "Extra/3D Ladder",  # After Consistent Planes
                    # "Extra/3D Rails", # After Consistent Planes
                    "Extra/3D Pointed Dripstone",  # After Consistent Planes
                    "Extra/3D Redstone Dust",  # After Consistent Planes
                    "Extra/Animation",
                    "Extra/Better Cross",
                    "Extra/Better Leaves",
                    "Extra/Better Particles",
                    "Extra/Better Weather",
                    "Extra/Clean Water",
                    "Extra/Display",
                    "Extra/Fire",
                    "Extra/Mirrored Pumpkin Blur",
                    "Extra/Moist Farmland",
                    "Extra/New Torches",
                    "Extra/Shadeless Lights",
                    "Extra/Square Shadow",
                    "Extra/Textured Lighting Rod",
                    "Extra/Unlit Redstone Ore",
                    "Extra/Wide Bamboo",
                ],
                "Resource Fixes Extra",
                (
                    "External/3D Default",
                    "Resource Fixes External",
                    None,
                ),
            ),
        ),
    ),
)

packs_tree: tree_pack_tuple = (
    "Packs/pack.mcmeta",
    None,
    [
        ("Textured/End Portal Frame Fix", "End Portal Frame Fix", None),
        ("Textured/Firefly Bush Fix", "Firefly Bush Fix", None),
        ("Textured/Modern Spectator GUI", "Modern Spectator GUI", None),
        ("Textured/Tall Seagrass Fix", "Tall Seagrass Fix", None),
        ("Extra/3D Iron Bars", "3D Iron Bars", None),
        ("Extra/3D Ladder", "3D Ladder", None),
        ("Extra/3D Pointed Dripstone", "3D Pointed Dripstone", None),
        ("Extra/3D Redstone Dust", "3D Redstone Dust", None),
        ("Extra/Better Leaves", "Better Leaves", None),
        ("Extra/Better Weather", "Better Weather", None),
        ("Extra/Better Particles", "Better Particles", None),
        ("Extra/Better Cross", "Better Cross", None),
        ("Extra/Clean Water", "Clean Water", None),
        ("Extra/Mirrored Pumpkin Blur", "Mirrored Pumpkin Blur", None),
        ("Extra/Moist Farmland", "Moist Farmland", None),
        ("Extra/Textured Lighting Rod", "Textured Lighting Rod", None),
        ("Extra/New Torches", "New Torches", None),
        ("Extra/Square Shadow", "Square Shadow", None),
        ("Extra/Unlit Redstone Ore", "Unlit Redstone Ore", None),
        ("Extra/Wide Bamboo", "Wide Bamboo", None),
    ],
)
