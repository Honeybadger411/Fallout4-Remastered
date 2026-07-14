# LOD Generation (xLODGen / TexGen)

**Important correction:** DynDOLOD 3 as a full application is currently Skyrim SE-only. For Fallout 4, there is no equivalent "DynDOLOD" tool - instead use TexGen (bundled in the DynDOLOD 3 Alpha download, which explicitly supports FO4) together with xLODGen (renamed "FO4LODGen").

## Downloads

1. **DynDOLOD 3 Alpha** (contains TexGen): https://www.nexusmods.com/skyrimspecialedition/mods/68518
2. **xLODGen** (currently beta 132): https://stepmodifications.org/forum/topic/13451-xlodgen-terrain-lod-beta-132-for-fnv-fo3-fo4-fo4vr-tes5-sse-tes5vr-enderal-enderalse/
3. **FO4LODGen Resources** (required Nexus mod, tracked in mods.json as `fo4lodgen-resources`): https://www.nexusmods.com/fallout4/mods/80276

## Setup

- Install both tools outside of MO2/game/Documents/Downloads folders, e.g. `D:\Modding\Tools\DynDOLOD3\` and `D:\Modding\Tools\xLODGen\`
- Add both as MO2 executables:
  - TexGen: `TexGenx64.exe`, argument `-FO4`
  - xLODGen: `xLODGenx64.exe`, argument `-FO4 -o:"D:\Output\"` (output folder must be OUTSIDE MO2/game folders, or files will be overwritten by mod managers)

## Procedure

1. Install `fo4lodgen-resources` mod first (required base data for terrain LOD)
2. Run TexGen via MO2. Set Base Size to 256 (higher unsupported due to engine mipmap bugs). Click Start. When done, click "Zip and Exit" and install the resulting zip as a mod (overwrites LOD textures from other mods - should load with high priority)
3. Run xLODGen via MO2. Select all relevant worldspaces (skip DLC03VRWorldspace - not visible in-game). Enable Terrain LOD, Object LOD, and Tree LOD generation. Click generate and wait (terrain LOD is CPU-intensive, can take a long time)
4. When done, create a new empty MO2 mod (e.g. "FO4LODGen Output"), cut the generated `meshes` and `textures` folders from the output directory into it
5. Enable the new mod and place it **at the very bottom of the mod list (highest priority)** - if any other mod overwrites it, in-game LOD will be broken
6. Do NOT disable the LOD resource mods used during generation - the game needs them for LOD to work correctly at runtime

## Adding to an existing save (mid-playthrough)

Per official DynDOLOD documentation: no full "clean save" procedure needed for a first-time addition. Recommended: save while in an interior (house/settlement building), then install the LOD output, then reload and go outside. The full clean-save procedure (deactivate, wait 24 game hours, disable/remove old output) is only needed when regenerating LOD from scratch after removing a mod that was a master in existing LOD plugins, or when switching internal LOD scripting methods.

## Notes

- Only generate Terrain LOD if using mods that alter landscape/landscape textures (we have several, e.g. Boston Natural Surroundings, savrenx-landscape) - worth the generation time for us
- Re-run generation whenever new worldspace-affecting mods are added later
