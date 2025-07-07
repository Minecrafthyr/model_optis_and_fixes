from defines import *
from pack import *

data = tree_pack_input_data(
    tree,
    "Assets/",
    [
        "Zipped/",
        "C:/PCL2/.minecraft/resourcepacks/",
        "C:/PCL2/.minecraft/versions/Shadow Fabric/resourcepacks/",
        "C:/PCL2/.minecraft/versions/Shadow NeoForge/resourcepacks/",
    ],
)

packs_data = tree_pack_input_data(
    packs_tree,
    "Assets/",
    "ZippedPacks/",
)