# BethINI Settings - Fallout4-Remastered

Documented configuration choices for this modlist. Priority order: **Stability > Graphics > Performance** (minimum target: 60 FPS 1% low).

## Setup

- Run BethINI Pie standalone (MO2 closed), pointed at the MO2 profile's Ini Path:
  `D:\Modding\MO2\profiles\Fallout4-Remastered\`
- Base preset: Ultra (adjusted based on high-end hardware)
- Applied "Recommended Tweaks"
- Text Language: English
- Display Mode: Borderless Windowed / Fullscreen (per personal preference)

## Papyrus (Advanced/Custom tab, section "Papyrus")

Increased script budget to accommodate a heavily scripted modlist (Sim Settlements 2, Improved Faction series, NPCs Travel, Legendary Effect Overhaul, Combat AI Empowered, Barter, Perk Up).

| Setting | Default | Set to |
|---|---|---|
| `fUpdateBudgetMS` | 1.2 | 2.4 |
| `fExtraTaskletBudgetMS` | 1.2 | 2.4 |
| `fPostLoadUpdateTimeMS` | 500 | 500 (unchanged) |
| `iMinMemoryPageSize` | 128 | 256 (or higher, kept existing higher value if already set) |
| `iMaxMemoryPageSize` | 512 | 1024 (or higher, kept existing higher value if already set) |
| `iMaxAllocatedMemoryBytes` | 153600 | 524288 (kept existing higher preset value instead of lowering to 307200) |

**Rationale:** Doubling script time/memory budget is a well-established community recommendation (Sim Settlements official wiki, BiRaitBec modlist guide) for script-heavy setups. Where an existing preset had already set a *higher* value than our target, we kept the higher value rather than lowering it — more budget is a stability benefit given ample RAM on high-end hardware, not a risk.

## Explicitly NOT changed

- **`iNumHWThreads`**: Left untouched. Community opinion is split; some current BethINI-based presets have removed it entirely, citing instability on some systems. Given our stability-first priority, the risk isn't worth an unclear performance gain.
- **`uGridsToLoad`**: Left at default (5). Higher values (7+) are a well-known crash risk.

## Display / Graphics

- **VSync: Off** — Bethesda's implementation is unreliable; frame limiting is instead handled via High FPS Physics Fix / driver-level cap.
- **FOV: Vanilla-ish (default ~70-75)** — Higher FOV values are known to cause visual clipping issues with armor/scope mods (relevant since our list has several weapon/armor mods).
- **Godrays / Motion Blur / Depth of Field: Low or Off** — Disproportionately expensive for their visual payoff, used as a performance buffer to protect the 60 FPS 1% low target.

## To revisit later

- Confirm whether these settings need re-application after major mod additions (e.g. NAC X weather presets may have their own godray/shadow settings).
