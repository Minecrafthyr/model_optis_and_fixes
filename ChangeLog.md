## Version 0.1

**Block Optimize:**

- beacon
- bell
- brewing_stand
- dragon_egg
- glow_lichen
- lectern
- lightning_rod
- sculk_vein
- spore_blossom
- template_anvil
- template_glass_pane
- template_torch.

## Version 0.2

Change name to "More Cull Face and Fixes"

**Block Fix with Optimize:**

- iron_bar.

**Block Fix:**

- brewing_stand from MC-262410.

## Version 0.3

Divide the resource pack into two parts:  
"Vanilla" and "Mods".

**Block Fix:**

- spore_blossom from MC-224195
- flower_pot_cross from MC-129826
- tripwire_hook from MC-262172.

**Item Fix:**

- arrow, spectral_arrow, tipped_arrow from MC-201808.

**Other:**  
Remove culling of iron_bar, template_glass_pane because they can't culling correctly.

## Version 0.4

**Block Optimize:**

- beacon
- mangrove_roots (experimental)
- redstone_dust, repeater, comparator, flower_pot from MC-262433 (experimental)
- hopper from MC-262452 (experimental) cauldron from MC-262470, stairs from MC-262461, fence_side.

**Block Fix:**

- template_azalea
- spore_blossom (doesn't work in v0.3), big_dripleaf
- button_inventory
- frogspawn
- scaffolding_unstable from MC-209947.

**Item Fix:**  
Left Hand Fix from MC-160810, by Shaddatic.

## Version 0.5

**Block Optimize:**

- template_fence_gate_open
- fence_side
- template_wall_side.

**Block Fix:**

- big_dripleaf_tilt in MC-221851
- repeater, comparator from MC-214662
- sunflower_top MC-122701.

**Other:**  
Fix a bug in Left Hand Fix. Reformat code. Remove button fix.

## Version 1.0

**Block Optimize:**

- beacon
- fence_side.

**Other:**  
Fix some bugs in version 0.1~0.4. Remove frogspawn fix, redstone cull face. Remove multiple description.

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

- Mojang doesn't (and can't) fix [MC-262652](https://bugs.mojang.com/browse/MC-262652) so I add dragon_egg back  
  Really confusing, see [This comment](https://bugs.mojang.com/browse/MC-262652?focusedId=1289602&page=com.atlassian.jira.plugin.system.issuetabpanels%3Acomment-tabpanel#comment-1289602)
- Remove candle no shading
- Torch fix (but lower performance)
- Iron Bars improvements
