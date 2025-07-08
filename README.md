# Resource Fixes

Optimize block models and fix bugs in Default resources.

- Version: 7.5
- Game versions: 1.20.2 - 1.21.7
- Project Links:
  - [Modrinth](https://modrinth.com/resourcepack/xq2isoUl)
  - [CurseForge](https://legacy.curseforge.com/minecraft/texture-packs/resource-fixes)
  - [Github](https://github.com/Minecrafthyr/model_optis_and_fixes)
- Old name: Model Optimizations and Fixes
- (May contains errors. Some bugs can't be fix by resourepack.)

Menu

- [Resource Fixes](#resource-fixes)
  - [Variants](#variants)
    - [Lite](#lite)
    - [Full](#full)
    - [Textured](#textured)
    - [Extra](#extra)
    - [External](#external)
  - [Suggestions](#suggestions)
  - [Included Features](#included-features)
  - [License](#license)
  - [Credits](#credits)

## Variants

Lite < Full(no suffix) < Textured < Extra < External

Full is Primary file. Download variants in additional files or [Github Source](https://github.com/Minecrafthyr/model_optis_and_fixes/tree/main/Zipped).

- Lite variant  
  Consistent with Default resource look, fixes only.
- Full variant  
  Visually improve item models or display.  
  Config use [Respackopts](https://modrinth.com/mod/TiF5QWZY) mod (not suggested, it just disable files).
- Textured variant  
  Using texture may conflict to other resourcepack.  
  Designed works with Default resources.
- Extra variant  
  Contains significant visual changes that I subjectively believe are better, not normal fixes, see [Modrinth Gallery](https://modrinth.com/resourcepack/model-optimizations-and-fixes/gallery).
- External variant  
  Include and tweaks with external pack.  
  Embedded GeForceLegend's [3D Default](https://modrinth.com/resourcepack/3d-default).

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

- 3D Hopper, Cauldron, Comparator, Repeater, Candles, Torches, Lanterns, Lever, Cake, Sniffer Egg Turtle Egg, Flower Pot, Brewing Stand.
- Block is a bit bigger in item frame.
- Cull Glass Pane.
- End Rod matches 3D Torch style.
- Handheld Arrow in [MC-201808](https://bugs.mojang.com/browse/MC/issues/MC-201808 "Arrows are held awkwardly in entities' hands").
- Leaf Litter, Lily Pad is shadeless now.
- Sculk Sensors tendril improvement.
- Smaller Chorus Plant item.
- Thin block translation in GUI is higher, less obscured by item count.
- Thin block, Conduit display above the head.
- Tweak block rotation display ([MC-114274](https://bugs.mojang.com/browse/MC/issues/MC-114274 "The rotation of some blocks in hand/GUI does not match rotation when placed")).
- Tweak mob head/skull item display ([MC-91869](https://bugs.mojang.com/browse/MC/issues/MC-91869 "Mob heads/skulls (except dragon head) are barely recognizable as such when held (held awkwardly in first person view")).
- Tweak some items display, they are not floating on hand or head now.
- Use front GUI light on Conduit, Torches, End Rod, Lanterns.

### Textured

- Item Frame
  - Optimize Item Frame with Texture change.
- Misc
  - Make Particle Tweaks mod's ripple particle transparent.
  - Rabbit Stew Height is consistent with other bowled items.
- Modern Spectator GUI
- Tall Seagrass Fix
  - \-1 pixel height on Tall Seagrass Top texture to avoid it visually goes out of water.

### Extra

- 3D Ladder
- 3D Pointed Dripstone (for matching texture, model is bigger than collision box)
- 3D Redstone Dust
- Animation
  - Animation of flowing lava is now faster then still lava.
  - Kelp animation is slower.
- Bedrock Slot Highlight
- Better Cross
  - Centered Fern, Oxeye Daisy.
- Better Leaves
  - Add inner back face.
  - Fast leaves waterlogged texture.
  - Better with [More Culling](https://modrinth.com/mod/moreculling)
- Better Weather
  - White and light blue and more transparent rain.
  - Less snow.
- Better Particles
  - Better Effect particles.
  - Light blue Splash particle.
  - Heart, Damage, Golden Heart texture is hollowed.
- Consistent Planes
  - Sore plane-like models are now not floating, shadeless, has cullface.
- Clean Water
- Fire
  - Fire texture is a bit transparent on body.
  - Sides of floor fire is lower than before (center does not change).
- Mirrored Pumpkin Blur
- Moist Farmland
  - Visualize Farmland "moisture" state 0 - 7.
- New Torches
  - All Torch has glowing outline model.
  - Better texture.
  - Handle of Torches is smoother.
- Shadeless Lights
  - Light source blocks are shadeless. ([MC-296027](https://bugs.mojang.com/browse/MC/issues/MC-296027 "Certain Light-Emitting Blocks Lack Internal Glow in Java Edition"))
  - Light source items are using front GUI light.
- Square Shadow
- Textured Lighting Rod
  - Lightning Rod Lit is using very bright Lightning Rod texture instead of full white.
- Unlit Redstone Ore
  - Redstone Ore is darker on unlit state.
- Wide Bamboo
  - 4 pixel wide Bamboo.
  - Wider bamboo leaves ([MC-262691](https://bugs.mojang.com/browse/MC/issues/MC-262691 "The leaves planes in bamboo aren't as wide as they should be")).

### External

- [3D Default](https://modrinth.com/resourcepack/3d-default)
  - Use Res Fixes "Extra/New Torches",  
    "Full/Display" Thin block | Flower Pot | Candle | Lightning Rod | Comparator | Repeater,  
    "Lite" & "Full/Display" Anvil | Tripwire Hook,  
    "Extra/3D Iron Bars",  
    "Extra/Unlit Redstone Ore" feature.
  - Modified Shovel item model: Middle thin.
  - Emissive blocks are shadeless.
  - Edited Brewing Stand model.
  - Fix compass_16 is missing.
  - Enable ambient occlusion for (Carved) Pumpkin, Hay Block.
  - Fix Fishing Rod display.

## Suggestions

Resourcepacks

- [3D Particles](https://modrinth.com/resourcepack/3d-particles)
- [AL's 3D Potions](https://modrinth.com/resourcepack/als-3d-potions)
- [Better Ores 3D](https://modrinth.com/resourcepack/better-ores-3d)
- [Boosted Brightness](https://modrinth.com/resourcepack/boosted-brightness-rp)
- [Smaller Side Shield](https://modrinth.com/resourcepack/smaller-side-shield)
- [Smooth Bow Animations](https://modrinth.com/resourcepack/smooth-bow-animations)
- [Smoother Glowing](https://modrinth.com/shader/smoother-glowing)
- [Tasty Items](https://modrinth.com/resourcepack/tasty-items)
- [Visual: Armor Trims](https://modrinth.com/resourcepack/visual-armor-trims)

## Included Features

May not 100% consistent to them.

Textured variant

- [End Portal Frame Fix](https://modrinth.com/resourcepack/end-portal-frame-fix)
- [Fix FireFly Bush](https://modrinth.com/resourcepack/firefly-bush-fix)
- [Tall Seagrass Fix](https://modrinth.com/resourcepack/tall-seagrass-fix)

Extra variant

- [3D Ladders](https://modrinth.com/resourcepack/3d-ladders)
- [CLEAN WATER](https://modrinth.com/resourcepack/clean-water)|[Clear Water!](https://modrinth.com/resourcepack/clear-water!)|[Clearer Water](https://modrinth.com/resourcepack/clearer-water)
- [Glowing Blocks Fix](https://modrinth.com/resourcepack/glowing-blocks-fix)

External variant

- [3D Default](https://modrinth.com/resourcepack/3d-default)

## License

- External variant: [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html)
- Other variants: [Unlicense](https://spdx.org/licenses/Unlicense.html), means you can modify, distribute, split, use it anywhere.

## Credits

Textured variant

- Firefly Bush Fix: Unmodified 2 files from [Fix Firefly Bush](https://modrinth.com/resourcepack/firefly-bush-fix) under [MIT License](https://spdx.org/licenses/MIT.html).

Extra variant

- 3D Redstone Dust: Modified 4 files from [Just 3D](https://modrinth.com/resourcepack/EnOq8vEP) by [sniffercraft34](https://modrinth.com/user/sniffercraft34), under [MIT License](https://spdx.org/licenses/MIT.html).
- Bedrock Slot Highlight: Unmodified 2 files from "[Vanilla Tweaks](https://vanillatweaks.net/)/BedrockSlotHighlight" under [Custom License](https://vanillatweaks.net/terms/)
- Better Leaves: Unmodified 41 files from "[Vanilla Tweaks](https://vanillatweaks.net/)/NicerFastLeaves" under [Custom License](https://vanillatweaks.net/terms/).
- Better Particles: Modified 9 files from "[Vanilla Tweaks](https://vanillatweaks.net/)/Unobtrusive Particles" under [Custom License](https://vanillatweaks.net/terms/).
- New Torches: Modified 4 files from [New Torches](https://modrinth.com/resourcepack/new-torches) by [Waradu](https://modrinth.com/user/Waradu) under [MIT License](https://spdx.org/licenses/MIT.html).

External variant

- 3D Default: Modified files from [3D Default](https://modrinth.com/resourcepack/3d-default) by [GeForceLegend](https://modrinth.com/user/GeForceLegend) under [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only.html).
