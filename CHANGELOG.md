# Changelog

All notable changes to this modlist project. Dates approximate, grouped by milestone rather than every individual commit (see Git history for full detail).

## Core foundation
- Repository structure, mods.json schema, .gitignore
- Core stability mods: F4SE, Buffout 4, Address Library, High FPS Physics Fix, Baka ScrapHeap, Canary Save File Monitor
- Bugfix mods: Unofficial Fallout 4 Patch, Community Fixes Merged, Previsibines Repair Pack, Extended Dialogue Interface

## UI & Graphics
- FallUI suite (Inventory, HUD, Map, Workbench, Item Sorter), MCM, LooksMenu, Better Console
- ENBSeries + NAC X preset, texture packs (Luxor's HD Overhaul, full SavrenX series)
- Vegetation and lighting mods (Boston Natural Surroundings, ELFX, Interiors Enhanced)

## Gameplay content
- Quality-of-life mods (QuickTrade, Place Everywhere, fast travel, terminals, companions)
- Major quest mods (Sim Settlements 2 + full ecosystem, Tales from the Commonwealth, America Rising 2, Fourville, Machine and Her, Valkyrie universe, Maxwell's World, Ug-Qualtoth)
- Animation, audio, and combat AI overhauls
- Location mods: Fens Sheriff's Department, South of the Sea, Beantown Interiors, Goodneighbor Expanded, Subway Runner Revival, Diamond City Expansion, Open Lexington, Stumble Upon Interiors, Isles of New England series, Point Lookout, Ashland Station, Caves of the Commonwealth, Wild Key Chase, Bradberton Interiors
- Creature retextures (HD Enhancement, LC's UHD Deathclaw, Mutant Menagerie)
- NPC Faction overhauls: complete Improved Faction series (Minutemen, Railroad, Institute, Brotherhood of Steel, Hostile Factions), NPCs Travel
- Companions: Heather Casdin, Ellen the Cartographer
- Weapons and armor: lore-friendly weapon pack, faction gear, Power Armor overhaul/retexture

## Frameworks & compatibility
- RobCo Patcher, Spell Perk Item Distributor, Baka Framework, Garden of Eden Papyrus Extender, Random Encounter Framework, SUP F4SE
- LOOT-flagged compatibility patches (Random Encounter Framework Patch Hub, SS2-XDI, Thuggyverse Immersion Patches, Machine and Her XDI, SS2 Previsibines Expansion Pack)
- Legendary Effect Overhaul, Barter economy overhaul, Perk Up, Old World Radio, LooksMenu Customization Compendium

## Quality-of-life additions (post-launch, mid-playtest)
- Configurable Hotkeys, Disable Companion Collision, Ultimate Scrap Recipes, True Grass, MCM Settings Manager, Raze My Settlement, Workshop Plus
- Expressive Expressions and Facial Expression/Eyetracking Engine Fixes (mimicry improvements)
- Daytripper 4 (fixes BA2 archive limit crash on large modlists)

## Infrastructure
- Root Builder setup for F4SE, ENBSeries, xSE PluginPreloader, and a custom 1.10.163 downgrade mod (isolated from the real Steam installation)
- BethINI configuration (Papyrus budget tuning for script-heavy setup, display settings)
- LOOT sort, xEdit dirty-plugin cleaning
- LOD generation via TexGen + xLODGen
- Validation and install-order tooling (`scripts/`)

## Known issues (see docs/known-issues.md and ROADMAP.md)
- DPI scaling fix required at the real game path (manual, per-installation step)
- Reference Handle count warning (Daytripper4) - future xEdit ESM-flagging planned
- MS Raze my Settlement F4SE detection issue - unresolved, Raze My Settlement used as active alternative
