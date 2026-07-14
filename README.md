# Fallout 4 - Remastered

A curated, quality-first Fallout 4 modlist project, documented as a Git repository and built toward an eventual Wabbajack release.

**Philosophy:** Vanilla+ rather than total conversion. Lore-friendly, polished, stable. Quality over quantity, but a lot of quantity too.

## Project stats

- **200+ mods** across 15+ categories
- Target game version: **1.10.163** (pre-Next-Gen / Old-Gen)
- Curated and researched mod-by-mod with real Nexus data, dependency tracking, and compatibility notes

## Categories covered

Core/Stability, Bugfixes, UI, Graphics, Quality of Life, Quests & Settlement Building (Sim Settlements 2 ecosystem), Animation, Audio, Gameplay/Combat AI, Locations, Creatures, NPC Factions, Companions, Weapons, Armor, Power Armor.

## Repository structure
database/
mods.json          - The mod database: every mod, its category, dependencies, and notes
docs/
bethini-settings.md      - BethINI configuration choices
download-checklist.md   - Auto-generated download checklist (see scripts/)
known-issues.md          - Documented workarounds (DPI scaling, etc.)
lod-generation.md        - xLODGen/TexGen setup and procedure
root-builder-mods.md     - Which mods need Root Builder and why
scripts/
validate_mods.py          - Checks the database for duplicate IDs, missing fields, broken dependencies
generate_install_order.py - Topologically sorts mods by dependency for install order
generate_checklist.py     - Generates docs/download-checklist.md
profiles/          - (planned) Wabbajack-specific profile structure
ROADMAP.md          - Open TODOs and future plans
CHANGELOG.md        - Notable changes over time
CONTRIBUTING.md     - How this project's Git/data conventions work

## Setup overview

This list targets game version **1.10.163**, installed via Mod Organizer 2 (portable) with Root Builder for F4SE/ENB/game-root files. Full setup involves:

1. MO2 portable install + Root Builder plugin
2. Game downgrade to 1.10.163 (isolated from the real Steam install - see `docs/known-issues.md`)
3. Download all mods per `docs/download-checklist.md`
4. BethINI configuration (see `docs/bethini-settings.md`)
5. LOOT sort + xEdit cleaning
6. LOD generation (see `docs/lod-generation.md`)

**Important:** After character creation, wait 10-15 minutes without opening the Pip-Boy or Workshop menu, to let background scripts (Sim Settlements 2, Workshop Framework, etc.) finish initializing. See `ROADMAP.md` for details.

## Status

Actively played and maintained. See `ROADMAP.md` for open items.
