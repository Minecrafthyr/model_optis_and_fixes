# Resource Fixes

Optimize block models and fix bugs in Default vanilla resources.

- Version: 6.0
- Game versions: 1.20.2 - 1.21.5
- Project Links:
  - [Modrinth](https://modrinth.com/resourcepack/xq2isoUl)
  - [Github](https://github.com/Minecrafthyr/model_optis_and_fixes)
- Old name: Model Optimizations and Fixes
- (May contains errors. Some bugs can't be fix by resourepack.)

### Suggestions / Compatibilities

- [Enhanced Block Entities](https://modrinth.com/mod/ebe) mod
- [Model Gap Fix](https://modrinth.com/mod/modelfix) (or [Stfu](https://modrinth.com/mod/shuttfup)) mod
- [Sodium](https://modrinth.com/mod/sodium) mod

## Variants

Download in Modrinth: [Version](https://modrinth.com/resourcepack/xq2isoUl/version/6.0) => Files

Lite < Full(no suffix) < Textured < Extra

- "Lite" variant  
  Consistent with Default resource look, fixes only.
- "Full" variant (Default download)  
  Visually improve item models or display.  
  You can use [Respackopts](https://modrinth.com/mod/TiF5QWZY) mod config this and downside variant.
- "Textured" variant  
  Using texture may conflict to other resourcepack.  
  Should be work in vanilla.
- "Extra" variant  
  Contains significant visual changes that I subjectively believe are better, not normal fixes.

### Lite

<details><summary> All the 43 bugs fixed in Lite variant</summary>

1. [MC-90566](https://bugs.mojang.com/browse/MC/issues/MC-90566 "The plants of sunflowers don't connect to their stems")
2. A part of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block")
3. [MC-122701](https://bugs.mojang.com/browse/MC/issues/MC-122701 "Sunflowers are stretched")
4. [MC-141291](https://bugs.mojang.com/browse/MC/issues/MC-141291 "lever state blockstate json backwards")
5. A part of [MC-144914](https://bugs.mojang.com/browse/MC/issues/MC-144914 "Some blocks don't randomly rotate correctly")
6. [MC-164741](https://bugs.mojang.com/browse/MC/issues/MC-164741 "Stonecutter blades are much brighter when north/south than east/west")
7. [MC-175626](https://bugs.mojang.com/browse/MC/issues/MC-175626 "Trapdoors are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled")
8. [MC-192420](https://bugs.mojang.com/browse/MC/issues/MC-192420 "Iron bars Z-fight on the bottom and top")
9. [MC-201760](https://bugs.mojang.com/browse/MC/issues/MC-201760 "Sunflower top half cross model is not mirrored on the back")
10. [MC-214700](https://bugs.mojang.com/browse/MC/issues/MC-214700 "Spore blossom top leaf texture is not mirrored correctly from behind")
11. [MC-221851](https://bugs.mojang.com/browse/MC/issues/MC-221851 "Tilted big dripleaf texture mirrored incorrectly from underneath")
12. [MC-224195](https://bugs.mojang.com/browse/MC/issues/MC-224195 "Parity issue: Differences in the spore blossom model in JE/BE")
13. [MC-224392](https://bugs.mojang.com/browse/MC/issues/MC-224392 "Big dripleaves are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled")
14. [MC-227330](https://bugs.mojang.com/browse/MC/issues/MC-227330 "The bottom texture of bars are flipped 180° and do not match the top")
15. [MC-236374](https://bugs.mojang.com/browse/MC/issues/MC-236374 "Chains are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled")
16. [MC-236474](https://bugs.mojang.com/browse/MC/issues/MC-236474 "Melon and pumpkin stems appear much darker than they should")
17. [MC-262172](https://bugs.mojang.com/browse/MC/issues/MC-262172 "Tripwire hook model incorrect - stick does not attach to ring symmetrically")
18. [MC-262174](https://bugs.mojang.com/browse/MC/issues/MC-262174 "The section of tripwire that is attached to a tripwire hook is stretched")
19. [MC-262410](https://bugs.mojang.com/browse/MC/issues/MC-262410 "Brewing stand arms appear darker than they should")
20. [MC-262452](https://bugs.mojang.com/browse/MC/issues/MC-262452 "Hopper models are unoptimized and cause rendering lag")
21. [MC-262460](https://bugs.mojang.com/browse/MC/issues/MC-262460 "Unneeded face in hanging lantern model")
22. [MC-262461](https://bugs.mojang.com/browse/MC/issues/MC-262461 "Stair models are unoptimized and can cause rendering lag")
23. [MC-262464](https://bugs.mojang.com/browse/MC/issues/MC-262464 "The bottom texture of the rod in brewing stands is incorrect")
24. [MC-262470](https://bugs.mojang.com/browse/MC/issues/MC-262470 "Cauldron models are very unoptimized, causing render lag")
25. [MC-262527](https://bugs.mojang.com/browse/MC/issues/MC-262527 "Item frame models are quite unoptimized")
26. [MC-262546](https://bugs.mojang.com/browse/MC/issues/MC-262546 "Texture mapping on tripwire hook rings appears to be wrong")
27. [MC-262598](https://bugs.mojang.com/browse/MC/issues/MC-262598 'Tripwire textures in the tripwire hook "attached: true" state have a wrong black rendering when the tripwire hook is attached to a non-transparent block')
28. [MC-262600](https://bugs.mojang.com/browse/MC/issues/MC-262600 "Tripwire texture can rotate unexpectedly when neighbouring connections change / is mapped inconsistently")
29. [MC-262641](https://bugs.mojang.com/browse/MC/issues/MC-262641 "Chorus flower models are incredibly unoptimized and cause serious rendering lag")
30. A part of [MC-262427](https://bugs.mojang.com/browse/MC/issues/MC-262427 "Flower pots and potted objects have very poorly optimized models and strange texture mapping")
31. [MC-262676](https://bugs.mojang.com/browse/MC/issues/MC-262676 "Mangrove propagules appear darker than they should due to shading not being disabled")
32. [MC-262689](https://bugs.mojang.com/browse/MC/issues/MC-262689 "Hanging mangrove propagule models are comically unoptimized")
33. [MC-262696](https://bugs.mojang.com/browse/MC/issues/MC-262696 "Potted mangrove propagules appear darker than they should due to shading not being disabled")
34. [MC-262864](https://bugs.mojang.com/browse/MC/issues/MC-262864 "Lever base texture is mapped upside-down")
35. [MC-262936](https://bugs.mojang.com/browse/MC/issues/MC-262936 "Some pixels of open fence gates are stretched")
36. [MC-262953](https://bugs.mojang.com/browse/MC/issues/MC-262953 "Fence gate models are very unoptimized, causing lag among other issues")
37. [MC-266463](https://bugs.mojang.com/browse/MC/issues/MC-266463 "The interior north and south faces of trial spawners are culled incorrectly")
38. A part of [MC-267281](https://bugs.mojang.com/browse/MC/issues/MC-267281 "Fence multipart model system performance optimization")
39. [MC-267895](https://bugs.mojang.com/browse/MC/issues/MC-267895 "Anvil's texture is mapped very strangely")
40. [MC-269368](https://bugs.mojang.com/browse/MC/issues/MC-269368 "Heavy Core bottom face not culled by blocks below")
41. [MC-277766](https://bugs.mojang.com/browse/MC/issues/MC-277766 '"On" lightning rod bottom texture is still mapped incorrectly')
42. [MC-277767](https://bugs.mojang.com/browse/MC/issues/MC-277767 '"On" lightning rods still use ambient occlusion')
43. [MC-279521](https://bugs.mojang.com/browse/MC/issues/MC-279521 "Up & down faces of resin clumps, sculk veins, vines & glow lichen are not mirrored from behind")

</details>

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
- Handheld Arrow in [MC-201808](https://bugs.mojang.com/browse/MC/issues/MC-201808).
- Use front gui light on Conduit, Torches, End Rod, Lanterns.
- Thin block, Conduit display above the head.
- Thin block translation in gui is higher, less obscured by item count.
- Sculk Sensors tendril improvement.
- Leaf Litter, Lily Pad is shadeless now.
- Tweak mob head/skull item display ([MC-91869](https://bugs.mojang.com/browse/MC/issues/MC-91869 "Mob heads/skulls (except dragon head) are barely recognizable as such when held (held awkwardly in first person view")).
- Tweak block rotation display ([MC-114274](https://bugs.mojang.com/browse/MC/issues/MC-114274 "The rotation of some blocks in hand/GUI does not match rotation when placed")).  
  Work in process, completed:
  - `block.json`
  - `thin_block.json`
  - `template_anvil.json`
  - `repeater_1tick.json`
  - `comparator.json`

### Textured

- Further Flower Pot optimization & remapping texture ([MC-262427](https://bugs.mojang.com/browse/MC/issues/MC-262427 "Flower pots and potted objects have very poorly optimized models and strange texture mapping")).
- Further hopper and cauldron optimization & remove unused texture ([MC-262454](https://bugs.mojang.com/browse/MC/issues/MC-262454 "Unused pixels in hopper top texture and hopper side texture")).
- Make Particle Tweaks mod's ripple particle transparent.
- Modern texture for spectator GUI.
- Reduce 1 pixel height on Tall Seagrass Top texture.

### Extra

3D (Blocks)

- Ladder
- Rails
- Pointed Dripstone (for matching texture, model is bigger than collision box)

Animation

- Animation of flowing lava is now faster then still lava.
- Kelp animation is slower.

Better Cross

- Centered Fern.

Block States

- Visualize Farmland "moisture" state 0 - 7.
- Visualize Leaves "waterlogged" state.
- Redstone Ore is darker on unlit state.

Consistent Planes

- Sore plane-like models are now not floating, shadeless, has cullface.

Fire

- Fire texture is a bit transparent on body (it's cutout on block because of render type).
- Sides of floor fire is lower than before (center has not changes).

Shadeless Lights

- Light source blocks are shadeless and use front GUI light. ([MC-296027](https://bugs.mojang.com/browse/MC/issues/MC-296027 "Certain Light-Emitting Blocks Lack Internal Glow in Java Edition"))

Wide Bamboo

- 4 pixel wide Bamboo.
- Wider bamboo leaves ([MC-262691](https://bugs.mojang.com/browse/MC/issues/MC-262691)).

Misc

- Better effect particle.
- Mirrored pumpkin blur.
- Some items are not floating on hand now.
- Square shadow.
