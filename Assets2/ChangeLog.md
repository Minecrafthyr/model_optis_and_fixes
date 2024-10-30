## Version 1.0

**Block Optimize:**

- beacon
- fence_side

**Others:**  
Fix some bugs in version 0.1~0.4. Remove frogspawn fix, redstone cull face. Remove multiplied description.

## Version 1.1

**Block Fix:**

- Re-added iron_bars z-fighting fix
- replace my fence_side model with MC-229645
- fence_inventory from MC-262604 (visual change)
- replace tripwire_hook MC-262172 with MC-262546
- tripwire from MC-262600.

## Version 2.0

What a large update! (Starting making 3D items.)

**Block Fix with Optimize:**

- rail, sculk_vein, redstone.  
  (I make them close to block and be culling. experimental, visual change!)

**Item Fix:**

- 3D cauldron, comparator, repeater, candle, torch, campfire, lantern, tripwire_hook
- hopper, cauldron now display upside down in head slot
- thin_block, slab display on the head
- spore_blossom upside down on ground
- block is bigger on ground/in item flame.

## Version 2.1

**Block Fix:**

- add a 3D ladder block model (optimized)
- add "shade": false to most of light blocks, they looks like "glowing"  
  (I don't want to list the blocks **: )**

**Other:**  
Fix lots of bugs in version 2.0, like hand held 3d items rotation/translation/scale problems.

## Version 2.2

**Block Fix:**

- lever shade fix in MC-262865
- spawner fix

**Block Optimize:**

- Hanging mangrove propagule from MC-262689
- Replace my chorus_flower model with MC-262641

**Block Fix with Optimize:**

- dragon_egg from MC-262652
- Replace my fence_gate model with MC-262953

**Other:**  
Remove 3D ladder block model  
Fix a mangrove_roots bug  
Fix a campfire gui bug in v2.1  
Fix some bugs (I actually realized this resourcepack has so many bugs)

### Version 2.3

**Other:**  
Fix some bugs in v2.0.

### Version 2.4

**Block Fix:**

- cross/flower_pot_cross uv fix
- rail shade fix
- sculk_sensor uv fix
- gravel random rotation

**Other:**  
Remove mangrove_roots

### Version 2.5

**Other:**

- Fix some long distance z-fighting bug (I hardly ever test them far away). improve cross/flower_pot_cross uv fix

### Version 2.6

**Other:**

- Remove cross/flower_pot_cross uv fix (it cause to many problems)

### Version 2.7

- Separate experimental changes to MCFF-E

**Other:**

- Fix some item display bugs in older versions.

### Version 2.8

**Block Optimize:**

- glow_lichen
- sculk_vein
- calibrated_sculk_sensor shade uv fix

**Other:**

- Update version.
- Some small fixes.

### Version 2.9

**Other:**

- removes shadeless blocks
- hanging_lantern is shadeless now, like lantern on ground

### Version 2.10

**Block Fix:**

- 3D sniffer egg

**Other:**

- Unfix rail...

### Version 2.11

**Block Optimize:**

- redstone

### Version 2.12

**Block Fix:**

- big_dripleaf_stem
- The back faces of spawners do not render from MC-169969

### Version 2.14

**Block Optimize:**

- hopper
- composter
- cauldron

**Block Fix with Optimize:**

- Replace stairs from MC-262461 with my model to fix MC-262461 & (a part of)MC-221723

**Other:**

- Fix a bug in the latest version.
- Rename project: Model Optimize & Fixes.
- Remove gravel rotation
- Remove fence inventory

### Version 3.0

**Block Optimize:**

- sculk_shrieker

**Other:**

- Fix z-fighting, wrong cull face in the latest version.

### Version 3.1

**Block Optimize:**

- little optimize to tripwire_hook, big_dripleaf, template_azalea

**Item Fix**

- tripwire_hook from [mintynoura's 3D Redstone Items](https://modrinth.com/resourcepack/3d-redstone-items-mintynoura)

### Version 3.2

Add Credits.md

**Block Fix:**

- coarse_dirt, gravel random rotation.
- More files from [mintynoura's 3D Redstone Items](https://modrinth.com/resourcepack/3d-redstone-items-mintynoura), but not all.

### Version 3.3

**Block Fix:**

- crimson_nylium, warped_nylium random rotation.

**Other:**

- Remove dragon_egg and spawner (Mojang fix it)

### Version 4.0

- Fix error bell bar cull
- Use Unlicense.
- fence from [MC-267281](https://bugs.mojang.com/projects/MC/issues/MC-267281)
- glass_pane from [MC-267315](https://bugs.mojang.com/browse/MC-267315)

### Version 4.1

- Mojang doesn't fix [MC-262652](https://bugs.mojang.com/browse/MC-262652) so I add dragon_egg back 
- Remove candle no shading
- Torch fix (but lower performance), also change repeater, comparator
- Iron Bars improvements

### Version 4.2

- Improve Iron Bars again
- remove fence from [MC-267281](https://bugs.mojang.com/browse/MC-267281) by [Connor Steppie](https://bugs.mojang.com/secure/ViewProfile.jspa?name=Awesoman3000) because it's unsafe for new varient
- Rail is on ground now

### Version 4.3

- Disable rail ambient occlusion
- Fix lots of problems on tripwire_hook_attached

### Version 4.4

- Fix spawner in [MC-266463](https://bugs.mojang.com/browse/MC-266463)
- Fix glow_lichen in [MC-249079](https://bugs.mojang.com/browse/MC-249079)
- Fix redstone_torch in [MC-129108](https://bugs.mojang.com/browse/MC-129108)
- Fix very confusing lever in [MC-141291](https://bugs.mojang.com/browse/MC-141291), [MC-262864](https://bugs.mojang.com/browse/MC-262864), [MC-262865](https://bugs.mojang.com/browse/MC-262865)

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

- [MC-226453](https://bugs.mojang.com/browse/MC-226453) Potted Azalea is incorrectly shaded when smooth lighting is enabled
- [MC-262694](https://bugs.mojang.com/browse/MC-262694) Inner planes of azaleas are shaded
- [MC-262695](https://bugs.mojang.com/browse/MC-262695) Inner planes of potted azaleas are shaded
- [MC-262696](https://bugs.mojang.com/browse/MC-262696) Potted mangrove propagules appear darker than they should due to shading not being disabled
- [MC-267895](https://bugs.mojang.com/browse/MC-267895) Anvil's texture is mapped very strangely
- [MC-224392](https://bugs.mojang.com/browse/MC-224392) Big dripleaves are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- [MC-236374](https://bugs.mojang.com/browse/MC-236374) Chains are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- [MC-262598](https://bugs.mojang.com/browse/MC-262598) Tripwire textures in the tripwire hook "attached: true" state have a wrong black rendering when the tripwire hook is attached to a non-transparent block
- [MC-234089](https://bugs.mojang.com/browse/MC-234089) Lightning rods are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- [MC-234087](https://bugs.mojang.com/browse/MC-234087) Extinguished campfires are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled
- Make the item model of Nether Sprouts matches Amethyst Bud
- [MC-214625](https://bugs.mojang.com/browse/MC-214625) Unlit redstone torches are unaffected by block shading / are evenly lit on all sides
- [MC-172852](https://bugs.mojang.com/browse/MC-172852) Doors aren't affected by ambient occlusion/smooth lighting
- Bell ambient occlusion is disabled
- (Readded) Button item model tweaks

### Version 4.9

- Remove fixes of MC-172852. (It caused doors too dark)
- Update pack format to 32.

Fixes

- [MC-175626](https://bugs.mojang.com/browse/MC-175626) Trapdoors are rendered too dark when blocks are placed adjacent to them while smooth lighting is enabled

### Version 4.10

- Ambient occlusion is enabled again for bell floor, extinguished campfire, grindstone (they are a bit dark but maybe is intented).
- Update pack format to 34.

Fixes

- Cull vault, heavy core downside.

### Version 4.11

- Remove pack.mcmeta filter
- Synchronizing files of two versions
- Remove Candles & Cake no ambient occlusion
- Now rail 1 pixel (y = 1/16 block) height


### Version 4.12

- Fix [#5](https://github.com/Minecrafthyr/model_optis_and_fixes/issues/5) missing texture on redstone torch.
- 1.21.2 changed some model, so this version will be archived, the pack above 1.21.2 is version 5.
- Lite version has no changes

### Version 5.0

- Correction Spawner and Vault UV (now mirrored from back).
- Remove (Redstone) Torch, Dragon Egg, Small Dripleaves, Comparator, Repeater. Mojang Studios fix them in 1.21.2.
- Remove lectern because it basically affects nothing.
- Modify the button in inventory model to match vanilla style.
- Move Shadeless Lantern to Full version.
- Fix errors with RespackOpts (tested in 1.21.3).
- Format some files with Blockbench.