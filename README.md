# Resource Fixes

Optimize block models and fix bugs in vanilla resources.

- Version: 5.14
- Game versions: 1.20.2 - 1.21.5
- Project Links:
  - [Modrinth](https://modrinth.com/resourcepack/xq2isoUl)
  - [Github](https://github.com/Minecrafthyr/model_optis_and_fixes)
- Old name: Model Optimizations and Fixes
- (May contains errors. Some bugs can't be fix by resourepack.)

### Suggestions / Compatibilities

- [Model Gap Fix](https://modrinth.com/mod/modelfix) mod
- [Enhanced Block Entities](https://modrinth.com/mod/ebe) mod
- [Sodium](https://modrinth.com/mod/sodium) mod

## Variants

Download in Modrinth: [Version](https://modrinth.com/resourcepack/model-optimizations-and-fixes/version/5.14) => Files

Lite < Full(no suffix) < Textured < Extra

- "Lite" variant  
  Removes some features that may affect modified gameplay or conflict to texture-only resourcepack.
- "Full" variant  
  You can use \*[Respackopts](https://modrinth.com/mod/TiF5QWZY) mod config this and downside variant.
- "Textured" variant  
  The textured variant is using texture may conflict to other resourcepack.  
  Should be work in vanilla.
- "Extra" variant  
  Contains significant visual changes that I subjectively believe are better, not normal fixes.

### Lite

- Beacon
- Cauldron
- Fences
- Flower Pot
- Hopper
- Item Frames
- Fence Gates ([MC-262953](https://bugs.mojang.com/browse/MC/issues/MC-262953 "Fence gate models are very unoptimized, causing lag among other issues"), [MC-262936](https://bugs.mojang.com/browse/MC/issues/MC-262936 "Some pixels of open fence gates are stretched"))
- Stairs ([MC-262461](https://bugs.mojang.com/browse/MC/issues/MC-262461 "Stair models are unoptimized and can cause rendering lag"))
- Bell Floor ([MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Heavy Core ([MC-269368](https://bugs.mojang.com/browse/MC/issues/MC-269368 "Heavy Core bottom face not culled by blocks below"))
- Anvil ([MC-267895](https://bugs.mojang.com/browse/MC/issues/MC-267895 "Anvil's texture is mapped very strangely"))
- Spore Blossom ([MC-214700](https://bugs.mojang.com/browse/MC/issues/MC-214700 "Spore blossom top leaf texture is not mirrored correctly from behind"), [MC-224195](https://bugs.mojang.com/browse/MC/issues/MC-224195 "Parity issue: Differences in the spore blossom model in JE/BE"))
- Lever ([MC-141291](https://bugs.mojang.com/browse/MC/issues/MC-141291 "lever state blockstate json backwards"), [MC-262864](https://bugs.mojang.com/browse/MC/issues/MC-262864 "Lever base texture is mapped upside-down"))
- Brewing Stand ([MC-262410](https://bugs.mojang.com/browse/MC/issues/MC-262410 "Brewing stand arms appear darker than they should"), [MC-262464](https://bugs.mojang.com/browse/MC/issues/MC-262464 "Brewing stand arms appear darker than they should"))
- Dripleaves ([MC-221851](https://bugs.mojang.com/browse/MC/issues/MC-221851 "Tilted big dripleaf texture mirrored incorrectly from underneath"), [MC-224392](https://bugs.mojang.com/browse/MC/issues/MC-224392 "Big dripleaves are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Chain ([MC-236374](https://bugs.mojang.com/browse/MC/issues/MC-236374 "Chains are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Sunflower ([MC-90566](https://bugs.mojang.com/browse/MC/issues/MC-90566 "The plants of sunflowers don't connect to their stems"), [MC-122701](https://bugs.mojang.com/browse/MC/issues/MC-122701 "Sunflowers are stretched"), [MC-201760](https://bugs.mojang.com/browse/MC/issues/MC-201760 "Sunflower top half cross model is not mirrored on the back"))
- Iron Bars ([MC-192420](https://bugs.mojang.com/browse/MC/issues/MC-192420 "Iron bars Z-fight on the bottom and top"), [MC-227330](https://bugs.mojang.com/browse/MC/issues/MC-227330 "The bottom texture of bars are flipped 180° and do not match the top"))
- Tripwire (Hook) ([MC-262172](https://bugs.mojang.com/browse/MC/issues/MC-262172 "Tripwire hook model incorrect - stick does not attach to ring symmetrically"), [MC-262173](https://bugs.mojang.com/browse/MC/issues/MC-262173 "The tripwire hook model uses the oak planks texture for the stick, rather than the tripwire hook item texture"), [MC-262174](https://bugs.mojang.com/browse/MC/issues/MC-262174 "The section of tripwire that is attached to a tripwire hook is stretched"), [MC-262546](https://bugs.mojang.com/browse/MC/issues/MC-262546 "Texture mapping on tripwire hook rings appears to be wrong"), [MC-262598](https://bugs.mojang.com/browse/MC/issues/MC-262598 'Tripwire textures in the tripwire hook "attached: true" state have a wrong black rendering when the tripwire hook is attached to a non-transparent block'), [MC-262600](https://bugs.mojang.com/browse/MC/issues/MC-262600 "Tripwire texture can rotate unexpectedly when neighbouring connections change / is mapped inconsistently"))
- Spawner ([MC-266463](https://bugs.mojang.com/browse/MC/issues/MC-266463 "The interior north and south faces of trial spawners are culled incorrectly"))
- Stonecutter ([MC-164741](https://bugs.mojang.com/browse/MC/issues/MC-164741 "Stonecutter blades are much brighter when north/south than east/west"))
- Lightning Rod ([MC-277766](https://bugs.mojang.com/browse/MC/issues/MC-277766 '"On" lightning rod bottom texture is still mapped incorrectly')， [MC-277767](https://bugs.mojang.com/browse/MC/issues/MC-277767 '"On" lightning rods still use ambient occlusion'))
- Trapdoors ([MC-175626](https://bugs.mojang.com/browse/MC/issues/MC-175626 "Trapdoors are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- \*Blocks randomly rotate correction (A part of [MC-144914](https://bugs.mojang.com/browse/MC/issues/MC-144914 "Some blocks don't randomly rotate correctly"))
- Resin Clumps, Sculk Vein, Vine & Glow Lichen[MC-279521](https://bugs.mojang.com/browse/MC/issues/MC-279521 "Up & down faces of resin clumps, sculk veins, vines & glow lichen are not mirrored from behind")
- Mangrove Propagules ([MC-262676](https://bugs.mojang.com/browse/MC/issues/MC-262676 "Mangrove propagules appear darker than they should due to shading not being disabled"), [MC-262689](https://bugs.mojang.com/browse/MC/issues/MC-262689 "Hanging mangrove propagule models are comically unoptimized") , [MC-262696](https://bugs.mojang.com/browse/MC/issues/MC-262696 "Potted mangrove propagules appear darker than they should due to shading not being disabled"), [MC-279521](https://bugs.mojang.com/browse/MC/issues/MC-262676 "Mangrove propagules appear darker than they should due to shading not being disabled"))
- Melon and pumpkin stems ([MC-236474](https://bugs.mojang.com/browse/MC/issues/MC-236474 "Melon and pumpkin stems appear much darker than they should"))
- Lantern ([MC-262460](https://bugs.mojang.com/browse/MC/issues/MC-262460 "Unneeded face in hanging lantern model"))
- Sculk Sensors UV fix & shadeless tendril.
- Button item model tweaks.
- Hopper and Cauldron display upside-down on head.

### Full

- Thin block, Conduit display above the head.
- Redstone Dust optimization.
- Chorus Plant improvements.
- Block is a bit bigger in item frame.
- 3D Hopper, Cauldron, Comparator, Repeater, Candles, Torches, Lanterns, Lever, Cake, Sniffer Egg, Flower Pot, Brewing Stand.
- End Rod matches 3D Torch style.
- Handheld Arrow in [MC-201808](https://bugs.mojang.com/browse/MC/issues/MC-201808).

### Textured

- Further hopper and cauldron optimization & remove unused texture.
- Further flower pot optimization & remapping texture.
- Modern texture for spectator GUI.
- Make Particle Tweaks's ripple particle transparent.

### Extra

- Slower kelp animation.
- Animation of flowing lava is now faster then still lava.
- Sides of floor fire is lower than before (center does not change).
- Fire texture is transparent on body (it's cutout on block because of render type).
- 4 pixel wide bamboo and wider bamboo leaves ([MC-262691](https://bugs.mojang.com/browse/MC/issues/MC-262691))!
- Some items are not floating on hand now.
- Mirrored pumpkin blur.
- Square shadow.
- Better effect particle.
- Light source blocks are shadeless. ([Luminous No Shading](https://modrinth.com/mod/luminous-no-shading) does better in inventory.)
- 3D Ladder and 3D Rails block model.

### Planned (not yet implemented)

- 3D block models (It's difficult to implement).
