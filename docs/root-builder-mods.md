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
