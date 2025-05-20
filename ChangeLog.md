## Version 1

### Version 1.0

- beacon
- fence_side
- Fix some bugs in version 0.1~0.4.
- Remove frogspawn fix, redstone cull face.
- Remove multiplied description.

### Version 1.1

- Re-added iron_bars z-fighting fix
- replace my fence_side model with MC-229645
- fence_inventory from MC-262604 (visual change)
- replace tripwire_hook MC-262172 with MC-262546
- tripwire from MC-262600.

## Version 2

### Version 2.0

- rail, sculk_vein, redstone.
- 3D cauldron, comparator, repeater, candle, torch, campfire, lantern, tripwire_hook
- hopper, cauldron now display upside down in head slot
- thin_block, slab display on the head
- spore_blossom upside down on ground
- block is bigger on ground/in item flame.

### Version 2.1

- add a 3D ladder block model (optimized)
- Shadeless for most of light blocks
- Fix lots of bugs in version 2.0, like hand held 3d items display problems.

### Version 2.2

- lever shade fix in MC-262865
- spawner fix
- Hanging mangrove propagule from MC-262689
- Replace my chorus_flower model with MC-262641
- dragon_egg from MC-262652
- Replace my fence_gate model with MC-262953
- Remove 3D ladder block model
- Fix a mangrove_roots bug
- Fix a campfire GUI bug in v2.1
- ... more fixes (I actually realized this resourcepack has so many bugs)

### Version 2.3

Fix some bugs in v2.0.

### Version 2.4

- cross/flower_pot_cross uv fix
- rail shade fix
- sculk_sensor uv fix
- gravel random rotation
- Remove mangrove_roots

### Version 2.5

- Fix some long distance z-fighting bug (I hardly ever test them far away). improve cross/flower_pot_cross uv fix

### Version 2.6

- Remove cross/flower_pot_cross uv fix (it cause to many problems)

### Version 2.7

- Separate experimental changes to MCFF-E
- Fix some item display bugs in older versions.

### Version 2.8

- glow_lichen
- sculk_vein
- calibrated_sculk_sensor shade uv fix
- Update pack format.
- ... small fixes.

### Version 2.9

- removes shadeless blocks
- hanging_lantern is shadeless now, like lantern on ground

### Version 2.10

- 3D sniffer egg
- Remove rail...

### Version 2.11

- redstone

### Version 2.12

- big_dripleaf_stem
- The back faces of spawners do not render from MC-169969

### Version 2.14

- hopper
- composter
- cauldron
- Replace stairs from MC-262461 with my model to fix MC-262461 & (a part of)MC-221723
- Fix a bug in the latest version.
- Rename project: Model Optimize & Fixes.
- Remove gravel rotation
- Remove fence inventory

## Version 3

### Version 3.0

- sculk_shrieker
- Fix z-fighting, wrong cull face in the latest version.

### Version 3.1

- little optimize to tripwire_hook, big_dripleaf, template_azalea
- tripwire_hook from [mintynoura's 3D Redstone Items](https://modrinth.com/resourcepack/3d-redstone-items-mintynoura)

### Version 3.2

Add Credits.md

- coarse_dirt, gravel random rotation.
- More files from [mintynoura's 3D Redstone Items](https://modrinth.com/resourcepack/3d-redstone-items-mintynoura), but not all.

### Version 3.3

- crimson_nylium, warped_nylium random rotation.
- Remove dragon_egg and spawner (Mojang fix it)

## Version 4

### Version 4.0

- Fix error bell bar cull
- Use Unlicense.
- fence from [MC-267281](https://bugs.mojang.com/projects/MC/issues/MC-267281)
- glass_pane from [MC-267315](https://bugs.mojang.com/browse/MC/issues/MC-267315)

### Version 4.1

- Dragon egg is not fixed so I add it back
- Remove candle no shading
- Torch fix (but lower performance), also change repeater, comparator
- Iron Bars improvements

### Version 4.2

- Improve Iron Bars again
- remove fence from [MC-267281](https://bugs.mojang.com/browse/MC/issues/MC-267281) by [Connor Steppie](https://bugs.mojang.com/secure/ViewProfile.jspa?name=Awesoman3000) because it's unsafe for new varient
- Rail is on ground now

### Version 4.3

- Disable Rail ambient occlusion
- Fix lots of problems on tripwire_hook_attached

### Version 4.4

- Fix spawner in [MC-266463](https://bugs.mojang.com/browse/MC/issues/MC-266463)
- Fix glow_lichen in [MC-249079](https://bugs.mojang.com/browse/MC/issues/MC-249079)
- Fix redstone_torch in [MC-129108](https://bugs.mojang.com/browse/MC/issues/MC-129108)
- Fix very confusing lever in [MC-141291](https://bugs.mojang.com/browse/MC/issues/MC-141291), [MC-262864](https://bugs.mojang.com/browse/MC/issues/MC-262864), [MC-262865](https://bugs.mojang.com/browse/MC/issues/MC-262865)

### Version 4.5

- Support for [Respackopts](https://modrinth.com/mod/respackopts) for config the resource pack ([#1](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/1))

### Version 4.6

- Remove some unused files, bad improvements, config that shouldn't be exist.
- Fix Chorus Plant inventory item use wrong model (I'm not sure my model is good or not).
- A "lite" version for this project.

### Version 4.7

- Fix a bug in lever_on.json
- Updated version

### Version 4.8

- Remove left hand fix because it's mirroring custom texture like text.
- Remove more Respackopts options may not used
- Fix [#3](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/3), [#4](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/4).

Fixes

- [MC-226453](https://bugs.mojang.com/browse/MC/issues/MC-226453) Potted Azalea is incorrectly shaded when smooth lighting is enabled
- [MC-262694](https://bugs.mojang.com/browse/MC/issues/MC-262694) Inner planes of azaleas are shaded
- [MC-262695](https://bugs.mojang.com/browse/MC/issues/MC-262695) Inner planes of potted azaleas are shaded
- [MC-262696](https://bugs.mojang.com/browse/MC/issues/MC-262696) Potted mangrove propagules appear darker than they should due to shading not being disabled
- [MC-267895](https://bugs.mojang.com/browse/MC/issues/MC-267895) Anvil's texture is mapped very strangely
- [MC-224392](https://bugs.mojang.com/browse/MC/issues/MC-224392) Big dripleaves are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- [MC-236374](https://bugs.mojang.com/browse/MC/issues/MC-236374) Chains are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- [MC-262598](https://bugs.mojang.com/browse/MC/issues/MC-262598) Tripwire textures in the tripwire hook "attached: true" state have a wrong black rendering when the tripwire hook is attached to a non-transparent block
- [MC-234089](https://bugs.mojang.com/browse/MC/issues/MC-234089) Lightning rods are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- [MC-234087](https://bugs.mojang.com/browse/MC/issues/MC-234087) Extinguished campfires are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- Make the item model of Nether Sprouts matches Amethyst Bud
- [MC-214625](https://bugs.mojang.com/browse/MC/issues/MC-214625) Unlit redstone torches are unaffected by block shading / are evenly lit on all sides
- [MC-172852](https://bugs.mojang.com/browse/MC/issues/MC-172852) Doors aren't affected by ambient occlusion/smooth lighting
- Bell ambient occlusion is disabled
- (Re-added) Button item model tweaks

### Version 4.9

- Remove fixes of MC-172852. (It caused doors too dark)
- Update pack format to 32.

Fixes

- [MC-175626](https://bugs.mojang.com/browse/MC/issues/MC-175626) Trapdoors are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled

### Version 4.10

- Cull vault, heavy core downside.
- Ambient occlusion is enabled again for bell floor, extinguished campfire, grindstone (they are a bit dark but maybe is intended).
- Update pack format to 34.

### Version 4.11

- Remove pack.mcmeta filter
- Synchronizing files of two versions
- Remove Candles & Cake no ambient occlusion
- Now rails has 1 pixel (y = 1/16 block) height

### Version 4.12

- Fix [#5](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/5) missing texture on redstone torch.
- 1.21.2 changed some model, so this version will be archived, the pack above 1.21.2 is version 5.
- Lite version has no changes

## Version 5

### Version 5.0

- Update pack format.
- Correction Spawner and Vault UV (now mirrored from back).
- Remove (Redstone) Torch, Dragon Egg, Small Dripleaves, Comparator, Repeater. Mojang Studios fix them in 1.21.2.
- Remove lectern because it basically affects nothing.
- Modify the button in inventory model to match vanilla style.
- Move Shadeless Lantern to Full version.
- Fix errors with RespackOpts (tested in 1.21.3).

### Version 5.1

- Update pack format.
- Rename the overlay folders.
- Move some files to overlays.
- Re-added missing Shadeless End Rod, Hopper and Cauldron display upside-down on head..
- ×`support_formats` -> √`supported_formats`
- Rename as "Resource Fixes"
- ... some small fixes.

### Version 5.2

- Add `assets` inside of overlay to make it works.

### Version 5.3

- Move more files to full version.
- Fix item display missing.

### Version 5.4

- Fix Repeater item model errors.
- Button Inventory model changes.

### Version 5.5

- Remove unused models.
- Tweaks Fence Inventory models and Button Inventory model.
- Optimize Custom Fence Gate models.

### Version 5.6

- Fix texture missing, again.

### Version 5.7

- Tweaks Fence Inventory models.
- Fix torch in inventory is smaller than before.
- Fix Brewing Stand item missing particle.
- Fix Filled Cauldron is using wrong texture.

### Version 5.8

- Update pack format.
- Clean unused files, use `gen.py` to merge files, also packing Extra variant.
- Fix hopper and cauldron display.

### Version 5.9

- Fix missing block model in `base` floder ([#6](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/6)).
- Remove unstable variants.

### Version 5.10

- Fix `gen.py` [#7](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/7)
- Fix [MC-279521](https://bugs.mojang.com/browse/MC/issues/MC-279521 "Up & down faces of resin clumps, sculk veins, vines & glow lichen are not mirrored from behind") and cull back face of them ([#8](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/8)).

### Version 5.11

- Fix [MC-236474](https://bugs.mojang.com/browse/MC/issues/MC-236474 "Melon and pumpkin stems appear much darker than they should
")
- Fix around mangrove propagule ("Previous" is previous version of Resource Fixes, "Now" is expected):

  | Mangrove propagule                                                                                                                                                             | Vanilla | Previous | Now   |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------- | ----- |
  | Shade (for cross faces) [MC-279521](https://bugs.mojang.com/browse/MC/issues/MC-262676 "Mangrove propagules appear darker than they should due to shading not being disabled") | true    | true     | false |

  | Potted mangrove propagule                                                                                                                                                             | Vanilla | Previous | Now   |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | ----- |
  | Shade (for cross faces) [MC-262696](https://bugs.mojang.com/browse/MC/issues/MC-262696 "Potted mangrove propagules appear darker than they should due to shading not being disabled") | true    | false    | false |

  | Hanging mangrove propagule (The worst model)                                                                                                                                   | Vanilla | Previous | Now      |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | -------- | -------- |
  | Ambient Occlusion                                                                                                                                                              | true    | true     | false    |
  | Rescale (for cross faces)                                                                                                                                                      | false   | false    | true     |
  | Shade (for cross faces) [MC-262676](https://bugs.mojang.com/browse/MC/issues/MC-262676 "Mangrove propagules appear darker than they should due to shading not being disabled") | true    | true     | false    |
  | Invisble faces [MC-262689](https://bugs.mojang.com/browse/MC/issues/MC-262689 "Hanging mangrove propagule models are comically unoptimized")                                   | have    | may have | not have |

- Remove Fix of [MC-262865](https://bugs.mojang.com/browse/MC/issues/MC-262865 "Lever handle is shaded").
- Fix lighting rod on using lighting rod texture.
- Coarse Dirt and Gravel random rotate is now in Lite variant.
- Fix incorrect Tripwire hook inventory display.
- Fix incorrect Big Dripleaf top cullface.
- Fix bamboo fence texture mapping.

### Version 5.12

- `tweak_shadeless_lights`(Extra): Light source blocks are shadeless. Shadeless lantern/end rod models are moved to here.
- Fix [MC-262460](https://bugs.mojang.com/browse/MC/issues/MC-262460 "Unneeded face in hanging lantern model").
- Correctly fix [MC-221851](https://bugs.mojang.com/browse/MC/issues/MC-221851 "Tilted big dripleaf texture mirrored incorrectly from underneath").
- Fix [MC-214700](https://bugs.mojang.com/browse/MC/issues/MC-214700 "Spore blossom top leaf texture is not mirrored correctly from behind").
- Fix [MC-227330](https://bugs.mojang.com/browse/MC/issues/MC-227330 "The bottom texture of bars are flipped 180° and do not match the top").

### Version 5.13

- \[Extra variant\] Fix missing texture in Glow Lichen.
- \[Full variant\] A smaller Chorus Plant item model.

### Version 5.14

Lite variant

- Remove shade of attached stem (unattached stem shade has been removed in 5.11).
- Remove fix of [MC-234089](https://bugs.mojang.com/browse/MC/issues/MC-234089 "Lightning rods are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled").

Extra variant

- Torches shade on handle.
- Add 3D Ladder and 3D Rails block model.

### Version 5.15

Lite variant

- Fix Default resource duplicate 1 flower in `flowerbed_2.json`.
- Fix Bamboo Fence mapping inconsistent with Default resource.

Extra variant

- Shadeless Lights will be disabled by Luminous No Shading if RespackOpts is installed.
- Visualize Farmland "moisture" state 0 - 7.
- 3D Redstone Dust from **Just 3D** by sniffercraft34 (modified).

### Version 5.16

Lite variant

- Fix `template_azalea.json` has wrong texture mapping.

Extra variant

- Remove Luminous No Shading disabling in 5.15 because that actually doesn't work.
- 3D Pointed Dripstone (using Dripstone Block texture).

## Version 6

### Version 6.0

Lite variant

- Small Dripleaf is now mirrored from behind, leaf can see from both side, no ambient occlusion.
- Fence Inventory model is consistent with fence block model.
- Fix [MC-276566](https://bugs.mojang.com/browse/MC/issues/MC-276566 "Inconsistency: Decorated pot items use entity/decorated_pot/decorated_pot_side for particles, but blocks do not") by set block particle = side texture
- Fix issues in Dried Ghast model

Full variant

- Split source file folders.

- `Display`:
  - Use front GUI light on Conduit, Torches, End Rod, Lanterns.
  - Thin block translation in GUI is higher, less obscured by item count.
  - Improve Lever item model display in GUI.
  - Repeater and Comparator in GUI in matching vanilla facing.
  - Tweak mob head/skull item display ([MC-91869](https://bugs.mojang.com/browse/MC/issues/MC-91869 "Mob heads/skulls (except dragon head) are barely recognizable as such when held (held awkwardly in first person view")).
  - Tweak block rotation display ([MC-114274](https://bugs.mojang.com/browse/MC/issues/MC-114274 "The rotation of some blocks in hand/GUI does not match rotation when placed")).
  - Tweak Torches, End Rod, Candle, Lanterns display again.
- `Misc`:
  - Cactus thorn can be see from both side.
  - Move Sculk Sensors tendril improvement from Lite variant to here.
  - Leaf Litter, Lily Pad is shadeless now.

Textured variant

- Reduce 1 pixel height on Tall Seagrass Top texture.

Extra variant

- `3D`: Better 3D Pointed Dripstone models perfectly match texture. At the cost, it is no longer matching the selection box.
- `Block States`: Unlit Redstone Ores has darker texture. Visualize Leaves "waterlogged" state.
- New `Better Cross`: Fern is centered.
- New `Consistent Planes`: Sore plane-like models are now not floating, shadeless, has cullface, Redstone and Glow Lichen is moved here.
- `Shadeless Lights` Use front GUI light on items.
- The medium bright pixels in sun texture is brighter, so when sun down it have light yellow (instead of yellow) edge.

<!-- endregion -->

### Version 6.1

Lite variant

- Replace pack.png
- Tweaks to custom fence and wall item display, makes it consistent to fence item

Full variant

- Display
  - Tweaks more item display. Floating item fix in Extra/Misc is now here, and use my implementation replace ItemHoldFix by [Vanilla Tweaks](https://vanillatweaks.net/), credits removed.

### Version 6.2

Lite variant

- Modify pack.png now it is 1:1 ratio.

Full variant

- Block on ground size is moved to Extra.

Extra variant

- New [New Torches](https://modrinth.com/resourcepack/new-torches) by [Waradu](https://modrinth.com/user/Waradu) under MIT License (modified).
- New `Display`: Block on ground size is larger than Default.

### Version 6.3

Extra variant

- New Torches
  - Handle of Torches is smoother.
  - Top of Torches is using a better texture.
- 3D Redstone Dust: Re-added missing 3D Redstone Dust.
- 3D Rails: Split from 3D.
- 3D Ladder: Split from 3D.
- Misc: Remove sun texture change in v6.0.
