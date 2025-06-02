# Resource Fixes

Optimize block models and fix bugs in Default vanilla resources.

- Version: 6.3
- Game versions: 1.20.2 - 1.21.5
- Project Links:
  - [Modrinth](https://modrinth.com/resourcepack/xq2isoUl)
  - [CurseForge](https://legacy.curseforge.com/minecraft/texture-packs/resource-fixes)
  - [Github](https://github.com/Minecrafthyr/model_optis_and_fixes)
- Old name: Model Optimizations and Fixes
- (May contains errors. Some bugs can't be fix by resourepack.)

## Variants

Lite < Full(no suffix) < Textured < Extra < Extra with 3D Default

- "Lite" variant  
  Consistent with Default resource look, fixes only.
- "Full" variant (Default download)  
  Visually improve item models or display.  
  You can use [Respackopts](https://modrinth.com/mod/TiF5QWZY) mod config this and downside variant.
- "Textured" variant  
  Using texture may conflict to other resourcepack.  
  Designed works with Default resources.
- "Extra" variant  
  Contains significant visual changes that I subjectively believe are better, not normal fixes.
- "Extra with 3D Default" variant  
  Embedded GeForceLegend's [3D Default](https://modrinth.com/resourcepack/3d-default) with compatibility tweaks. 


### Lite

- Anvil (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"), [MC-267895](https://bugs.mojang.com/browse/MC/issues/MC-267895 "Anvil's texture is mapped very strangely"))
- Beacon (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Bell Floor (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Big Dripleaf ([MC-221851](https://bugs.mojang.com/browse/MC/issues/MC-221851 "Tilted big dripleaf texture mirrored incorrectly from underneath"), [MC-224392](https://bugs.mojang.com/browse/MC/issues/MC-224392 "Big dripleaves are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Blocks randomly rotate correction (a part of [MC-144914](https://bugs.mojang.com/browse/MC/issues/MC-144914 "Some blocks don't randomly rotate correctly"))
- Brewing Stand (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"), [MC-262410](https://bugs.mojang.com/browse/MC/issues/MC-262410 "Brewing stand arms appear darker than they should"), [MC-262464](https://bugs.mojang.com/browse/MC/issues/MC-262464 "The bottom texture of the rod in brewing stands is incorrect"))
- Button item is now using block model.
- Cauldron ([MC-262470](https://bugs.mojang.com/browse/MC/issues/MC-262470 "Cauldron models are very unoptimized, causing render lag"))
- Chain ([MC-236374](https://bugs.mojang.com/browse/MC/issues/MC-236374 "Chains are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Chorus Flowers (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"), [MC-262641](https://bugs.mojang.com/browse/MC/issues/MC-262641 "Chorus flower models are incredibly unoptimized and cause serious rendering lag"))
- Fence Gates ([MC-262936](https://bugs.mojang.com/browse/MC/issues/MC-262936 "Some pixels of open fence gates are stretched"), [MC-262953](https://bugs.mojang.com/browse/MC/issues/MC-262953 "Fence gate models are very unoptimized, causing lag among other issues"))
- Fences (a part of [MC-279617](https://bugs.mojang.com/browse/MC/issues/MC-279617 "Bamboo fence multipart rendering optimization - requires texture mapping modification"), a part of [MC-267281](https://bugs.mojang.com/browse/MC/issues/MC-267281 "Fence multipart model system performance optimization"))
- Flower Pot (A part of [MC-262427](https://bugs.mojang.com/browse/MC/issues/MC-262427 "Flower pots and potted objects have very poorly optimized models and strange texture mapping"))
- Four Turtle Egg (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Heavy Core ([MC-269368](https://bugs.mojang.com/browse/MC/issues/MC-269368 "Heavy Core bottom face not culled by blocks below"))
- Hopper ([MC-262452](https://bugs.mojang.com/browse/MC/issues/MC-262452 "Hopper models are unoptimized and cause rendering lag"))
- Hopper and Cauldron display upside-down on head.
- Iron Bars ([MC-192420](https://bugs.mojang.com/browse/MC/issues/MC-192420 "Iron bars Z-fight on the bottom and top"), [MC-227330](https://bugs.mojang.com/browse/MC/issues/MC-227330 "The bottom texture of bars are flipped 180° and do not match the top"))
- Item Frames ([MC-262527](https://bugs.mojang.com/browse/MC/issues/MC-262527 "Item frame models are quite unoptimized"))
- Lantern ([MC-262460](https://bugs.mojang.com/browse/MC/issues/MC-262460 "Unneeded face in hanging lantern model"))
- Lever ([MC-141291](https://bugs.mojang.com/browse/MC/issues/MC-141291 "lever state blockstate json backwards"), [MC-262864](https://bugs.mojang.com/browse/MC/issues/MC-262864 "Lever base texture is mapped upside-down"))
- Lightning Rod ([MC-277766](https://bugs.mojang.com/browse/MC/issues/MC-277766 '"On" lightning rod bottom texture is still mapped incorrectly'), [MC-277767](https://bugs.mojang.com/browse/MC/issues/MC-277767 '"On" lightning rods still use ambient occlusion'))
- Mangrove Propagules ([MC-262676](https://bugs.mojang.com/browse/MC/issues/MC-262676 "Mangrove propagules appear darker than they should due to shading not being disabled"), [MC-262689](https://bugs.mojang.com/browse/MC/issues/MC-262689 "Hanging mangrove propagule models are comically unoptimized"), [MC-262696](https://bugs.mojang.com/browse/MC/issues/MC-262696 "Potted mangrove propagules appear darker than they should due to shading not being disabled"))
- Melon and pumpkin stems ([MC-236474](https://bugs.mojang.com/browse/MC/issues/MC-236474 "Melon and pumpkin stems appear much darker than they should"))
- Remove 1 duplicate face in Wildflowers and Pink Petals model.
- Resin Clumps, Sculk Vein, Vine & Glow Lichen ([MC-279521](https://bugs.mojang.com/browse/MC/issues/MC-279521 "Up & down faces of resin clumps, sculk veins, vines & glow lichen are not mirrored from behind"))
- Small Dripleaf
- Spawner ([MC-266463](https://bugs.mojang.com/browse/MC/issues/MC-266463 "The interior north and south faces of trial spawners are culled incorrectly"))
- Spore Blossom ([MC-214700](https://bugs.mojang.com/browse/MC/issues/MC-214700 "Spore blossom top leaf texture is not mirrored correctly from behind"), [MC-224195](https://bugs.mojang.com/browse/MC/issues/MC-224195 "Parity issue: Differences in the spore blossom model in JE/BE"))
- Stairs ([MC-262461](https://bugs.mojang.com/browse/MC/issues/MC-262461 "Stair models are unoptimized and can cause rendering lag"))
- Stonecutter ([MC-164741](https://bugs.mojang.com/browse/MC/issues/MC-164741 "Stonecutter blades are much brighter when north/south than east/west"))
- Sunflower ([MC-90566](https://bugs.mojang.com/browse/MC/issues/MC-90566 "The plants of sunflowers don't connect to their stems"), [MC-122701](https://bugs.mojang.com/browse/MC/issues/MC-122701 "Sunflowers are stretched"), [MC-201760](https://bugs.mojang.com/browse/MC/issues/MC-201760 "Sunflower top half cross model is not mirrored on the back"))
- Trapdoors ([MC-175626](https://bugs.mojang.com/browse/MC/issues/MC-175626 "Trapdoors are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Tripwire (Hook) ([MC-262172](https://bugs.mojang.com/browse/MC/issues/MC-262172 "Tripwire hook model incorrect - stick does not attach to ring symmetrically"), [MC-262174](https://bugs.mojang.com/browse/MC/issues/MC-262174 "The section of tripwire that is attached to a tripwire hook is stretched"), [MC-262546](https://bugs.mojang.com/browse/MC/issues/MC-262546 "Texture mapping on tripwire hook rings appears to be wrong"), [MC-262598](https://bugs.mojang.com/browse/MC/issues/MC-262598 'Tripwire textures in the tripwire hook "attached: true" state have a wrong black rendering when the tripwire hook is attached to a non-transparent block'), [MC-262600](https://bugs.mojang.com/browse/MC/issues/MC-262600 "Tripwire texture can rotate unexpectedly when neighbouring connections change / is mapped inconsistently"))

### Full

- 3D Hopper, Cauldron, Comparator, Repeater, Candles, Torches, Lanterns, Lever, Cake, Sniffer Egg, Flower Pot, Brewing Stand.
- Block is a bit bigger in item frame.
- Smaller Chorus Plant item.
- End Rod matches 3D Torch style.
- Handheld Arrow in [MC-201808](https://bugs.mojang.com/browse/MC/issues/MC-201808 "Arrows are held awkwardly in entities' hands").
- Use front gui light on Conduit, Torches, End Rod, Lanterns.
- Thin block, Conduit display above the head.
- Thin block translation in gui is higher, less obscured by item count.
- Sculk Sensors tendril improvement.
- Leaf Litter, Lily Pad is shadeless now.
- Tweak mob head/skull item display ([MC-91869](https://bugs.mojang.com/browse/MC/issues/MC-91869 "Mob heads/skulls (except dragon head) are barely recognizable as such when held (held awkwardly in first person view")).
- Tweak block rotation display ([MC-114274](https://bugs.mojang.com/browse/MC/issues/MC-114274 "The rotation of some blocks in hand/GUI does not match rotation when placed")).
- Tweak some items display, they are not floating on hand or head now.

### Textured

- Make Particle Tweaks mod's ripple particle transparent.
- Modern texture for spectator GUI.
- Reduce 1 pixel height on Tall Seagrass Top texture.

### Extra

3D Ladder

3D Rails

3D Pointed Dripstone (for matching texture, model is bigger than collision box)

3D Redstone Dust

Animation

- Animation of flowing lava is now faster then still lava.
- Kelp animation is slower.

Better Cross

- Centered Fern, Oxeye Daisy.

Better Effect Particles

Block States

- Visualize Farmland "moisture" state 0 - 7.
- Redstone Ore is darker on unlit state.

Consistent Planes

- Sore plane-like models are now not floating, shadeless, has cullface.

Clean Water

Fire

- Fire texture is a bit transparent on body (it's cutout on block because of render type).
- Sides of floor fire is lower than before (center does not change).

Mirrored Pumpkin Blur

New Torches

- Torch texture is also left top bright.
- Handle of Torches is smoother.
- Top of Torches is using a better texture.

Shadeless Lights

- Light source blocks are shadeless. ([MC-296027](https://bugs.mojang.com/browse/MC/issues/MC-296027 "Certain Light-Emitting Blocks Lack Internal Glow in Java Edition"))
- Light source items are using front GUI light.

Square Shadow

Textured Lighting Rod

- Lightning Rod Lit is using very bright Lightning Rod texture instead of full white.

Wide Bamboo

- 4 pixel wide Bamboo.
- Wider bamboo leaves ([MC-262691](https://bugs.mojang.com/browse/MC/issues/MC-262691 "The leaves planes in bamboo aren't as wide as they should be")).

## License and Credits

License:

- 3D Default variant: [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html)
- Others variant: Unlicense, means you can modify or distribute, use it anywhere.

Credits:

Extra/3D Redstone Dust: Modified 4 files from [Just 3D](https://modrinth.com/resourcepack/EnOq8vEP) by [sniffercraft34](https://modrinth.com/user/sniffercraft34), under [MIT License](https://spdx.org/licenses/MIT.html).

Extra/New Torches: Modified 4 files from [New Torches](https://modrinth.com/resourcepack/new-torches) by [Waradu](https://modrinth.com/user/Waradu) under [MIT License](https://spdx.org/licenses/MIT.html).

3D Default: Modified files from [3D Default](https://modrinth.com/resourcepack/3d-default) by [GeForceLegend](https://modrinth.com/user/GeForceLegend) under [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html).