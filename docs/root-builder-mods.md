# Mods Requiring Root Builder

These are the only mods in this list that install files directly into the Fallout 4 root folder (where `Fallout4.exe` lives) rather than the `Data` folder. All other mods install normally through MO2 without special treatment.

## 1. F4SE (Fallout 4 Script Extender)

Files in `Root/`: `f4se_loader.exe`, `f4se_1_10_163.dll`, `f4se_steam_loader.dll`
Files outside `Root/` (normal Data folder): `F4SE/Scripts`, `F4SE/Plugins` (initially empty, populated by other mods)

Set up as an MO2 executable pointing to `Root/f4se_loader.exe`.

## 2. ENBSeries (binary)

Source: enbdev.com, not Nexus. Use version 0.496 (better preset compatibility than 0.501).

Files in `Root/`: `d3d11.dll`, `d3dcompiler_46e.dll`, `enblocal.ini`

## 3. xSE PluginPreloader F4

Files in `Root/`: `WinHTTP.dll`, `xSE PluginPreloader.xml`

Required because Buffout 4 needs it on old-gen F4SE (0.6.23), which lacks Next-Gen F4SE's built-in plugin preload method.

## Custom: Fallout4-Downgrade-1.10.163

Not a Nexus mod - files generated locally using the Simple Fallout 4 Downgrader tool (Nexus ID 81933), run once against the real Steam installation, then copied out and the real installation reverted to Next-Gen using the tool's automatic backups.

Files in `Root/`: `Fallout4.exe`, `Fallout4Launcher.exe`, `steam_api64.dll` (all patched to 1.10.163)

## Load order note

Root Builder mods should be checked for conflicts if their Root files ever overlap, but as of this list none of the four above share any file names, so load order between them is not critical. Standard MO2 conflict resolution rules apply if that changes later.

## Troubleshooting: Root Builder file sync issues

If Root Builder Build/Clear/Sync seem to have no effect, or files don't update after editing them in the mod folder, check these in order:

### 1. Custom deployment rules for file types
Root Builder's "USVFS + Link" mode only physically links `.exe` and `.dll` files by default; everything else (`.ini`, `.fx`, `.xml`, etc.) is mapped virtually only and won't be reliably picked up by tools that read config files at a low level (F4SE, ENB, xSE PluginPreloader all need this).

Fix: In Root Builder's Custom tab, add these patterns to the "Link" column:
***.ini
***.fx
***.xml

### 2. Stale cache after game/mod changes
If files still don't update after fixing deployment rules:
1. Run Clear
2. Delete the RootBuilder cache folder entirely: `[MO2 install]\plugins\data\RootBuilder\`
3. Manually delete any stale files this affected from the real game folder
4. In Root Builder Settings, click Create for both Backup and Cache
5. Run Build again

### 3. MO2's Overwrite folder takes priority over everything
`[MO2 install]\overwrite\Root\` has the highest priority in MO2 and will silently override any Root Builder mod file with the same name, regardless of mod list order. If a file won't update no matter what, search for it inside the `overwrite` folder and delete it there.

### Diagnostic tip
When something won't start and no crash log is generated, check the tool's own log file (e.g. `xSE PluginPreloader.log`, `enbseries.log`) in the real game folder immediately after a crash - Root Builder's automatic Clear runs fast, so you may need to disable Autobuild temporarily to inspect the real folder without it being cleared.
