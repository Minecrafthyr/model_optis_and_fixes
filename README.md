# Resource Fixes

Fix bugs in vanilla resource.  
Old name: Model Optimizations and Fixes  
Notice: Some bugs can't be fix by resourepack.

- Version: 5.4
- Game versions:  
  Version 4 and before: 1.19.4 - 1.21.1  
  Version 5: 1.20.2 - 1.21.4
- Project Links:
  - [Modrinth](https://modrinth.com/resourcepack/model-optimizations-and-fixes)
  - [Github](https://github.com/Minecrafthyr/model_optis_and_fixes)

### About "lite" version

There is also a lite version of this pack, which removes some features that may affect modified gameplay or conflict to texture-only resourcepack.  
**"\*" means it will not apply in the lite version**  
Download:
- On Modrinth:  
  Version page -> Files -> Resource Fixes Lite
- On Github:  
  Open model_optis_and_fixes/ZippedPack2 -> [Resource Fixes Lite.zip](https://github.com/Minecrafthyr/model_optis_and_fixes/blob/main/ZippedPack2/Resource%20Fixes%20Lite.zip)


## Mods Info

### Supports

- \*[Respackopts](https://modrinth.com/mod/respackopts) mod for config this resource pack (full version only)

### Suggestions / Compatibilities

- [Model Gap Fix](https://modrinth.com/mod/modelfix)
- [Enhanced Block Entities](https://modrinth.com/mod/ebe)
- [Sodium](https://modrinth.com/mod/sodium)

## Feature list

### Fixes

#### Blocks

- Beacon
- Cauldron
- Fences
- Fence Gates
- Flower Pot
- Hopper
- Item Frames
- Lighting Rod
- Stairs ([MC-262461](https://bugs.mojang.com/browse/MC-262461 "Stair models are unoptimized and can cause rendering lag"))
- Bell Floor ([MC-109087](https://bugs.mojang.com/browse/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Heavy Core ([MC-269368](https://bugs.mojang.com/browse/MC-269368 "Heavy Core bottom face not culled by blocks below"))
- Anvil ([MC-267895](https://bugs.mojang.com/browse/MC-267895 "Anvil's texture is mapped very strangely"))
- Spore Blossom ([MC-224195](https://bugs.mojang.com/browse/MC-224195 "Parity issue: Differences in the spore blossom model in JE/BE"))
- Lever ([MC-141291](https://bugs.mojang.com/browse/MC-141291 "lever state blockstate json backwards"), [MC-262864](https://bugs.mojang.com/browse/MC-262864 "Lever base texture is mapped upside-down"), [MC-262865](https://bugs.mojang.com/browse/MC-262865 "Lever handle is shaded"))
- Brewing Stand ([MC-262410](https://bugs.mojang.com/browse/MC-262410 "Brewing stand arms appear darker than they should"), [MC-262464](https://bugs.mojang.com/browse/MC-262464 "Brewing stand arms appear darker than they should"))
- Dripleaves ([MC-221851](https://bugs.mojang.com/browse/MC-221851 "Tilted big dripleaf texture mirrored incorrectly from underneath"), [MC-224392](https://bugs.mojang.com/browse/MC-224392 "Big dripleaves are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Chain ([MC-236374](https://bugs.mojang.com/browse/MC-236374 "Chains are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Sunflower ([MC-90566](https://bugs.mojang.com/browse/MC-90566 "The plants of sunflowers don't connect to their stems"), [MC-122701](https://bugs.mojang.com/browse/MC-122701 "Sunflowers are stretched"), [MC-201760](https://bugs.mojang.com/browse/MC-201760 "Sunflower top half cross model is not mirrored on the back"))
- Iron Bars ([MC-192420](https://bugs.mojang.com/browse/MC-192420 "Iron bars Z-fight on the bottom and top"))
- Tripwire (Hook) ([MC-262172](https://bugs.mojang.com/browse/MC-262172 "Tripwire hook model incorrect - stick does not attach to ring symmetrically"), [MC-262173](https://bugs.mojang.com/browse/MC-262173 "The tripwire hook model uses the oak planks texture for the stick, rather than the tripwire hook item texture"), [MC-262174](https://bugs.mojang.com/browse/MC-262174 "The section of tripwire that is attached to a tripwire hook is stretched"), [MC-262546](https://bugs.mojang.com/browse/MC-262546 "Texture mapping on tripwire hook rings appears to be wrong"), [MC-262598](https://bugs.mojang.com/browse/MC-262598 'Tripwire textures in the tripwire hook "attached: true" state have a wrong black rendering when the tripwire hook is attached to a non-transparent block'), [MC-262600](https://bugs.mojang.com/browse/MC-262600 "Tripwire texture can rotate unexpectedly when neighbouring connections change / is mapped inconsistently"))
- Spawner ([MC-266463](https://bugs.mojang.com/browse/MC-266463 "The interior north and south faces of trial spawners are culled incorrectly"))
- Stonecutter ([MC-164741](https://bugs.mojang.com/browse/MC-164741 "Stonecutter blades are much brighter when north/south than east/west"))
- Lightning Rod ([MC-234089](https://bugs.mojang.com/browse/MC-234089 "Lightning rods are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Trapdoors ([MC-175626](https://bugs.mojang.com/browse/MC-175626 "Trapdoors are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- \*Blocks randomly rotate correction (A part of [MC-144914](https://bugs.mojang.com/browse/MC-144914 "Some blocks don't randomly rotate correctly"))
- Sculk Sensors UV fix
- \*Redstone Dust


#### Items

- Handheld Arrow in [MC-201808](https://bugs.mojang.com/browse/MC-201808)

### Improvements

#### Blocks

- \*Shadeless Lantern.
- \*Shadeless End Rod.

#### Items

- Button item model tweaks
- Hopper and Cauldron display upside-down on head.
- Thin block, Conduit display on the head.
- \*Chorus Plant improvements.
- \*Block is a bit bigger in item frame.
- \*3D Hopper, Cauldron, Comparator, Repeater, Candles, Torches, Lanterns, Lever, Cake, Sniffer Egg, Flower Pot, Brewing Stand.
- \*End Rod matches 3D Torch style.
