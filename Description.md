- Version: 9.11
- Game versions: 1.14.4-1.21.9
- Project Links:
  - [Modrinth](https://modrinth.com/project/xq2isoUl) (updated most quickly)
  - [Github](https://github.com/Minecrafthyr/model_optis_and_fixes)
  - [CurseForge](https://www.curseforge.com/minecraft/texture-packs/resource-fixes-and-tweaks)
- Optional Dependencies: **[Respackopts](https://modrinth.com/project/TiF5QWZY) for config**.
- May contains errors. Some bugs can't be fix by resourepack.

### FAQ

> FPS Boost?

- Fixes.(Lite|Normal|Textured|Simplified): ✔️ (in some cases; depends on block type and count).
- Tweaks.(Lite|Normal|External): ❌️ (some models slow downs).

## Variants

Resource Fixes.zip is primary file. Download variants in **additional files** or on [Github](https://github.com/Minecrafthyr/model_optis_and_fixes/tree/main/out/Variants).

Resource Fixes (optimize and fixes)

- Lite variant  
  Optimization & Fixes only, compatible with texture only resourcepacks.
- Normal variant  
  Visually improve item models (3D block item) or display.
- Textured variant  
  Using texture may conflict to other resourcepack.  
  Designed with Default resource style.
- Simplified variant  
  Simplified some block models for fun.  
  Resource Tweaks are **not affected**.

Resource Tweaks (tweaks and improvements)

- Lite variant  
  Contains significant visual tweaks that I thought better, not fixes.
- Normal variant  
  May causing lag or breaking visual tweaks, options may help you.
- External variant  
  Try compat with external pack.  
  Embedded GeForceLegend's [3D Default](https://modrinth.com/resourcepack/3d-default).

## License

Please also check license in ./Credits folder (in source or pack) for specific files.

- Resource Tweaks External: [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only).
- Others: [Unlicense](https://spdx.org/licenses/Unlicense), means you can modify, distribute, split, use it anywhere.

---

## Resource Fixes

Optimize block models and fix bugs in Default resources.

### Lite

- Anvil (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"), [MC-267895](https://bugs.mojang.com/browse/MC/issues/MC-267895 "Anvil's texture is mapped very strangely"))
- Beacon (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Bell Floor (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Big Dripleaf ([MC-221851](https://bugs.mojang.com/browse/MC/issues/MC-221851 "Tilted big dripleaf texture mirrored incorrectly from underneath"), [MC-224392](https://bugs.mojang.com/browse/MC/issues/MC-224392 "Big dripleaves are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Brewing Stand (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"), [MC-262410](https://bugs.mojang.com/browse/MC/issues/MC-262410 "Brewing stand arms appear darker than they should"), [MC-262464](https://bugs.mojang.com/browse/MC/issues/MC-262464 "The bottom texture of the rod in brewing stands is incorrect"))
- Button item is now using block model.
- Cauldron ([MC-262470](https://bugs.mojang.com/browse/MC/issues/MC-262470 "Cauldron models are very unoptimized, causing render lag"))
- Chain ([MC-236374](https://bugs.mojang.com/browse/MC/issues/MC-236374 "Chains are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Chorus Flowers (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"), [MC-262641](https://bugs.mojang.com/browse/MC/issues/MC-262641 "Chorus flower models are incredibly unoptimized and cause serious rendering lag"))
- Fence Gates ([MC-262936](https://bugs.mojang.com/browse/MC/issues/MC-262936 "Some pixels of open fence gates are stretched"), [MC-262953](https://bugs.mojang.com/browse/MC/issues/MC-262953 "Fence gate models are very unoptimized, causing lag among other issues"))
- Fences (partial fix [MC-279617](https://bugs.mojang.com/browse/MC/issues/MC-279617 "Bamboo fence multipart rendering optimization - requires texture mapping modification"), partial fix [MC-267281](https://bugs.mojang.com/browse/MC/issues/MC-267281 "Fence multipart model system performance optimization"))
- Flower Pot (partial fix [MC-262427](https://bugs.mojang.com/browse/MC/issues/MC-262427 "Flower pots and potted objects have very poorly optimized models and strange texture mapping"))
- Four Turtle Egg (one of [MC-109087](https://bugs.mojang.com/browse/MC/issues/MC-109087 "Faces of some blocks are not at all culled when said face is hidden by a solid, opaque block"))
- Heavy Core ([MC-269368](https://bugs.mojang.com/browse/MC/issues/MC-269368 "Heavy Core bottom face not culled by blocks below"))
- Hopper ([MC-262452](https://bugs.mojang.com/browse/MC/issues/MC-262452 "Hopper models are unoptimized and cause rendering lag"))
- Iron Bars ([MC-192420](https://bugs.mojang.com/browse/MC/issues/MC-192420 "Iron bars Z-fight on the bottom and top"), [MC-227330](https://bugs.mojang.com/browse/MC/issues/MC-227330 "The bottom texture of bars are flipped 180° and do not match the top"))
- Item Frames ([MC-262527](https://bugs.mojang.com/browse/MC/issues/MC-262527 "Item frame models are quite unoptimized"))
- Lantern ([MC-262460](https://bugs.mojang.com/browse/MC/issues/MC-262460 "Unneeded face in hanging lantern model"))
- Lever ([MC-141291](https://bugs.mojang.com/browse/MC/issues/MC-141291 "lever state blockstate json backwards"), [MC-262864](https://bugs.mojang.com/browse/MC/issues/MC-262864 "Lever base texture is mapped upside-down"))
- Lightning Rod ([MC-277766](https://bugs.mojang.com/browse/MC/issues/MC-277766 '"On" lightning rod bottom texture is still mapped incorrectly'), [MC-277767](https://bugs.mojang.com/browse/MC/issues/MC-277767 '"On" lightning rods still use ambient occlusion'))
- Mangrove Propagules ([MC-262676](https://bugs.mojang.com/browse/MC/issues/MC-262676 "Mangrove propagules appear darker than they should due to shading not being disabled"), [MC-262689](https://bugs.mojang.com/browse/MC/issues/MC-262689 "Hanging mangrove propagule models are comically unoptimized"), [MC-262696](https://bugs.mojang.com/browse/MC/issues/MC-262696 "Potted mangrove propagules appear darker than they should due to shading not being disabled"))
- Melon and pumpkin stems ([MC-236474](https://bugs.mojang.com/browse/MC/issues/MC-236474 "Melon and pumpkin stems appear much darker than they should"))
- Resin Clumps, Sculk Vein, Vine & Glow Lichen ([MC-279521](https://bugs.mojang.com/browse/MC/issues/MC-279521 "Up & down faces of resin clumps, sculk veins, vines & glow lichen are not mirrored from behind"))
- Small Dripleaf
- Spawner ([MC-266463](https://bugs.mojang.com/browse/MC/issues/MC-266463 "The interior north and south faces of trial spawners are culled incorrectly"))
- Spore Blossom ([MC-214700](https://bugs.mojang.com/browse/MC/issues/MC-214700 "Spore blossom top leaf texture is not mirrored correctly from behind"), [MC-224195](https://bugs.mojang.com/browse/MC/issues/MC-224195 "Parity issue: Differences in the spore blossom model in JE/BE"))
- Stairs ([MC-262461](https://bugs.mojang.com/browse/MC/issues/MC-262461 "Stair models are unoptimized and can cause rendering lag"))
- Stonecutter ([MC-164741](https://bugs.mojang.com/browse/MC/issues/MC-164741 "Stonecutter blades are much brighter when north/south than east/west"))
- Sunflower ([MC-90566](https://bugs.mojang.com/browse/MC/issues/MC-90566 "The plants of sunflowers don't connect to their stems"), [MC-122701](https://bugs.mojang.com/browse/MC/issues/MC-122701 "Sunflowers are stretched"), [MC-201760](https://bugs.mojang.com/browse/MC/issues/MC-201760 "Sunflower top half cross model is not mirrored on the back"))
- Trapdoors ([MC-175626](https://bugs.mojang.com/browse/MC/issues/MC-175626 "Trapdoors are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled"))
- Tripwire (Hook) ([MC-262172](https://bugs.mojang.com/browse/MC/issues/MC-262172 "Tripwire hook model incorrect - stick does not attach to ring symmetrically"), [MC-262174](https://bugs.mojang.com/browse/MC/issues/MC-262174 "The section of tripwire that is attached to a tripwire hook is stretched"), [MC-262546](https://bugs.mojang.com/browse/MC/issues/MC-262546 "Texture mapping on tripwire hook rings appears to be wrong"), [MC-262598](https://bugs.mojang.com/browse/MC/issues/MC-262598 'Tripwire textures in the tripwire hook "attached: true" state have a wrong black rendering when the tripwire hook is attached to a non-transparent block'), [MC-262600](https://bugs.mojang.com/browse/MC/issues/MC-262600 "Tripwire texture can rotate unexpectedly when neighbouring connections change / is mapped inconsistently"))
- Remove 1 duplicate face in Wildflowers and Pink Petals (`flowerbed_2`) model.
- Hopper and Cauldron display upside-down on head.
- `Handheld_Arrow` ([MC-201808](https://bugs.mojang.com/browse/MC/issues/MC-201808 "Arrows are held awkwardly in entities' hands"))
- `Random_Rotate`: Clay, Coarse Dirt, Crimson Nylium, Gravel, Warped Nylium block randomly rotate (partial fix [MC-144914](https://bugs.mojang.com/browse/MC/issues/MC-144914 "Some blocks don't randomly rotate correctly"))
- `Language_Fix`: Enchantment|Potion Level Fix.
- Minor optimize Enhanced Block Entities and Farmer's Delight. If you meet issue, use Respackopts to disable it.

### Normal

- `Block_Variants`: variants of blocks, now only Terracotta.
- `Display`
  - 3D Cauldron, Comparator, Repeater, Cake, Hopper item.
  - Improve Button, Conduit item.
  - Chorus Plant has a smaller model now.
  - Thin block translation in GUI is higher, less obscured by item count.
  - Thin block (and more blocks) display above the head instead of inside.
  - Lightning Rod, All Shelf (not bookshelves), Copper Golem is a bit bigger in GUI.
  - Tweak mob head/skull item display ([MC-91869](https://bugs.mojang.com/browse/MC/issues/MC-91869 "Mob heads/skulls (except dragon head) are barely recognizable as such when held (held awkwardly in first person view")).
  - Tweak block rotation display ([MC-114274](https://bugs.mojang.com/browse/MC/issues/MC-114274 "The rotation of some blocks in hand/GUI does not match rotation when placed")).
  - Tweak some items display, they are not floating on hand or head now.
- `Small_Back_Faces`: Cactus and small dripleaf has some pixels of back faces.

### Textured

- `Better_Fast_Leaves`: Same as Sodium's fast leaves.
- `End_Portal_Frame_Fix`: Now you can see where it facing.
- `Item_Frame_Tweaks`: Optimize Item Frame with Texture change.
- `Misc`
  - Make Particle Tweaks mod's ripple particle transparent.
  - Rabbit Stew Height is consistent with other bowled items.
- `Modern_Recipe_Button_Texture`
- `Modern_Redstone_Torch_Texture`
- `Modern_Spectator_GUI_Texture`
- `Rail_Fix` @[Rail Fix](https://modrinth.com/project/481jOCry)
  - Raised rail is stretched better.
- `Tall_Seagrass_Fix`: -1 pixel height on Tall Seagrass Top texture to avoid it visually goes out of water.

#### Credits

- `Better_Fast_Leaves`: Copied 11 files from "[Vanilla Tweaks](https://vanillatweaks.net/)/NicerFastLeaves" under [Vanilla Tweaks - Terms and Conditions](https://vanillatweaks.net/terms/).
- `Rail_Fix`: Modified 23 files from [Rail Fix](https://modrinth.com/project/481jOCry) by [Lad_Flaver](https://modrinth.com/user/Lad_Flaver) under [ARR with explicitly stated](https://modrinth.com/project/481jOCry).
- `Smooth_Stone_Slab_Fix`: Copied 1 file from [Smooth Stone Slab Fix](https://modrinth.com/project/QoUSM3q9) by [creep](https://modrinth.com/user/creep) under [MIT License](https://spdx.org/licenses/MIT).

### Simplified

This variant just for fun and does not affect Resource Tweaks. If you just need simplified flower, see [Performant Petals](https://modrinth.com/resourcepack/performant-petals).

Simplified model: Hanging Mangrove Propagule, Leaf Litter, Pink Petals, Wildflowers, Dragon Egg, Chorus Plant, Chorus Flower, Fence Gate.

## Resource Tweaks

### Lite

- `3D_Ladder`
- `Axolotl_Bucket_Variants` @[Axolotl Bucket Variants](https://modrinth.com/resourcepack/axolotl-bucket-variants)
- `Better_Animation`
  - Animation of flowing lava is now faster then still lava.
  - Smooth Lava animation.
  - Kelp animation is slower.
- `Better_Fire`
  - Fire texture is a bit transparent on body.
  - Sides of floor fire is 1 block height (center does not change), and tilted (in supported MC version).
- `Better_Particles`
  - Better Effect particles.
  - Light blue Splash particle.
  - Heart, Damage, Golden Heart texture is hollowed.
- `Better_Sculk_Sensor_Swing`
- `Better_Weather`
  - White and light blue and more transparent rain.
  - Less filled texture.
- `Clean_Water`: It's now 75% solid compared to default.
- `Display`: 3D Brewing Stand, Campfires, Candles, Lever, Sniffer Egg, Turtle Egg, Flower Pot, Tripwire Hook.
- `Fast_Better_Grass`
  - Makes the following blocks use the top texture on their sides as well: (Snow-covered) Grass block, Dirt path, Podzol, Mycelium, (Warped|Crimson) Nylium, additionally Farmland.
  - Also make compatibly with [Full Paths](https://modrinth.com/mod/full-paths).
- `Language_Tweaks`
  - Renamed Nether Quartz to Quartz.
- `Lantern`: 3D item and smooth animation.
- `Mirrored_Pumpkin_Blur`
- `Moist_Farmland`: Visualize Farmland "moisture" state 0 - 7 (when it dries up).
- `Natural_Firefly_Bushes` @[Natural Firefly Bushes](https://modrinth.com/project/1u7lYbpD)
- `New_Torches`: All Torch has glowing outline model. 20% more smooth torch handle.
- `Particle_Tweaks`: Slime jump use it's block texture.
- `Sandstone_Tweaks`
  - Top using mixed (50% bottom/50% top) texture.
  - Side using mixed (75% bottom/25% top) texture.
  - Smooth/Cut/Chiseled using original top texture.
- `Shadeless_Lights`
  - Light source blocks are shadeless.
  - Light source items are using front GUI light.
- `Square_Shadow`: Square entity shadow.
- `Unlit_Redstone_Ore`: Redstone Ore is darker on unlit state.

#### Credits

- `Axolotl_Bucket_Variants`: Copied 11 files from [Axolotl Bucket Variants](https://modrinth.com/resourcepack/axolotl-bucket-variants) by [manyrandomthings](https://modrinth.com/user/manyrandomthings) under [LGPL-3.0-only](https://spdx.org/licenses/LGPL-3.0-only).
- `Better_Particles`: Modified 9 files from "[Vanilla Tweaks](https://vanillatweaks.net/)/Unobtrusive Particles" under [Vanilla Tweaks - Terms and Conditions](https://vanillatweaks.net/terms/).
- `Fast_Better_Grass`: Modified 8 files from [Fast Better Grass](https://modrinth.com/project/dspVZXKP) by [Fabulously Optimized](https://modrinth.com/organization/fabulously-optimized)/[robotkoer](https://modrinth.com/user/robotkoer) under [MIT License](https://spdx.org/licenses/MIT).
- `Natural_Firefly_Bushes`: Copied zip file from [Natural Firefly Bushes](https://modrinth.com/project/1u7lYbpD) by [TheGreatOwlMaster](https://modrinth.com/user/TheGreatOwlMaster) under [MIT License](https://spdx.org/licenses/MIT).

### Normal

- `3D_Bars`
- `3D_Pointed_Dripstone`
- `3D_Redstone_Dust`
- `Better_Copper_Grate`: Inner faces of Copper Grate.
- `Better_Leaves`: Inner faces of Leaves, better with [Cull Leaves](https://modrinth.com/mod/cull-leaves).
- `Consistent_Planes`: Some plane-like models are now not floating, shadeless, has cullface.
- `Cross_Correction`
  - Center of Flowers and fern is corrected.
  - Cross models are now has mirrored back face.
  - Add random rotation for 1 block tall (standard and potted) cross model.
- `Tasty_Items` @[Tasty Items](https://modrinth.com/project/yVNZK7l2)
  - Move Rabbit Stew up 1 pixel (feature in Fixes/Textured/Misc)
- `Wide_Bamboo`
  - 4 pixel wide Bamboo.
  - Wider bamboo leaves ([MC-262691](https://bugs.mojang.com/browse/MC/issues/MC-262691 "The leaves planes in bamboo aren't as wide as they should be")). With mirrored back face.
  - Rotate bamboo leaves 5° (in supported MC version) to avoid z-fighting.

#### Credits

- `3D_Bars`: Modified 6 files from [Simple 3D Iron Bars](https://modrinth.com/project/p5Kdm58p) by [poqbox](https://modrinth.com/user/poqbox) under [BSD-3-Clause](https://spdx.org/licenses/BSD-3-Clause).
- `3D_Redstone_Dust`: Modified 4 files from [Just 3D](https://modrinth.com/project/EnOq8vEP) by [sniffercraft34](https://modrinth.com/user/sniffercraft34) under [MIT License](https://spdx.org/licenses/MIT).
- `Tasty_Items`: Copied zip file from [Tasty Items](https://modrinth.com/project/yVNZK7l2) by [enchanted-games](https://modrinth.com/user/enchanted-games) under [CC-BY-NC-4.0](https://spdx.org/licenses/CC-BY-NC-4.0).

### External

- `3D_Default` @[3D Default](https://modrinth.com/resourcepack/3d-default)
  - Used Resource Fixes feature:
    - `Normal.Display`: Anvil, Thin block | Flower Pot | Candle | Lightning Rod | Comparator | Repeater | Tripwire Hook
  - Used Resource Tweaks feature:
    - `Normal.(New_Torches, 3D Iron Bars, Unlit Redstone Ore, Wide Bamboo, 3D Redstone Dust)`.
  - Modified Shovel item model: Middle thin.
  - Modified Brewing Stand model.
  - Emissive blocks are shadeless.
  - Enable ambient occlusion for (Carved) Pumpkin, Hay Block.
  - Removed 3D potions.
  - Add Respackopts options to disable Bed, Chain, Cobweb, Gilded Blackstone, Lily Pad, Mushrooms & Fungus, Ores.
- `UltiCraft-Models3D` @[3D Models (UltiCraft Sandalone)](https://modrinth.com/resourcepack/ulticraft-models-3d)
  - Only use Bookshelf and Barrel.

#### Credits

- `3D_Default`: Copied zip file from [3D Default](https://modrinth.com/resourcepack/3d-default) by [GeForceLegend](https://modrinth.com/user/GeForceLegend) under [GPL-3.0-only](https://spdx.org/licenses/GPL-3.0-only).
- `UltiCraft-Models3D`: Copied 17 files from [3D Models (UltiCraft Sandalone)](https://modrinth.com/resourcepack/ulticraft-models-3d) by [meenimc](https://modrinth.com/user/meenimc) under [Apache-2.0](https://spdx.org/licenses/Apache-2.0).

## More Information

### Planned

- You can try resourcepack here, but may not compatible.
- Work in progress:
  - `Fixes.Simplified`: More simplified models.
  - `Fixes.Normal.Block_Variants`: More block variants.
  - `Tweaks.Normal.Cross_Correction`: More random rotate & correction models.
  - `Tweaks.Normal.Particle_Tweaks`: More filled block particle texture.
- Slowly embedding or implementing outside packs.
  - [Vanilla Tweaks](https://vanillatweaks.net/picker/resource-packs/)
  - [Vary Me](https://modrinth.com/resourcepack/vary-me)
  - [Smaller Side Shield](https://modrinth.com/resourcepack/smaller-side-shield)
  - [Smooth Bow Animations](https://modrinth.com/resourcepack/smooth-bow-animations)
  - [Blockstates +](https://modrinth.com/resourcepack/blockstates)

### Suggestions

- [3D Particles](https://modrinth.com/resourcepack/3d-particles)
- [Boosted Brightness](https://modrinth.com/resourcepack/boosted-brightness-rp)
- [Smoother Glowing](https://modrinth.com/shader/smoother-glowing)
- [Visual: Armor Trims](https://modrinth.com/resourcepack/visual-armor-trims)

## Custom Build

1. Clone Github Repository
2. Config `config.json` following `config.md`
3. Enter path `cd <the path>`
4. `pip install jsonpatch`
5. `python build.py`
   - `--release` arg build config root with tag `only_in_release` is true and do more compressions.
   - `--dir <path>` arg change the current directory path.
   - `--cfg <path>` arg change the config path.
   - `--log <path>` arg change the log path.
