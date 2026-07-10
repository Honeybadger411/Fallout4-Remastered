# Known Issues & Manual Fixes

Issues that Wabbajack cannot automate and require manual steps after installation.

## Fallout 4 main menu UI too large / doesn't fit screen (high DPI displays)

**Symptom:** After launching through F4SE/MO2, the main menu UI is oversized and doesn't fit the screen.

**Cause:** Windows DPI compatibility settings are stored per-file-path in the Windows Registry, not inside the game/mod files themselves. Since Root Builder links `Fallout4.exe` and `Fallout4Launcher.exe` to their real path in the actual game installation folder, Windows only recognizes a compatibility override set on that real path — not on the copy inside the MO2 mods folder.

**Fix (manual, per-user):**
1. Navigate to your real Fallout 4 installation folder (e.g. `[SteamLibrary]\steamapps\common\Fallout 4`)
2. Right-click `Fallout4.exe` → Properties → Compatibility tab
3. Click "Change high DPI settings"
4. Check "Override high DPI scaling behavior" and set scaling to be performed by "Application"
5. Repeat the same for `Fallout4Launcher.exe`

**Note:** This must be done on the real game folder path, not inside the MO2 mods folder, because Root Builder links files to the real path at launch. This is a per-installation, per-user step that cannot be automated by Wabbajack.

**Possible better fix (to verify):** Check whether BethINI Pie can resolve this via `Fallout4Prefs.ini` scaling settings instead, which would travel with the modlist and not require this manual step.
