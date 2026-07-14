# Contributing / Working on this project

This is currently a solo project, but this file documents the conventions used so the workflow stays consistent (and so it's clear to anyone else who might work on it later).

## Adding a mod to the database

1. Research the mod on Nexus (or the relevant source). Check requirements, load order notes, known conflicts.
2. Add an entry to `database/mods.json`:
```json
   {
     "id": "kebab-case-id",
     "name": "Full Mod Name",
     "category": "category-slug",
     "subcategory": "subcategory-slug",
     "source": "https://www.nexusmods.com/fallout4/mods/XXXXX",
     "version": "check-on-nexus",
     "requires": ["other-mod-id"],
     "notes": "Description and compatibility notes"
   }
```
3. `requires` lists dependencies **this** mod needs, not what needs it.
4. Use `"version": "check-on-nexus"` when the exact version isn't confirmed for game 1.10.163.
5. Run `python scripts/validate_mods.py` before committing. Fix any duplicate IDs, missing fields, or broken references it reports.
6. Commit with a `feat:` prefix (see Commit conventions below).

## Marking a mod as an alternative (not both active)

If two mods serve the same purpose and only one should be active, mark the non-default one:
```json
"status": "alternative",
"alternativeTo": ["the-other-mod-id"],
```
Add a note explaining the tradeoff. The validation script and install-order script both account for this (alternatives are excluded from the default install order).

## Commit message conventions

Follow Conventional Commits:
- `feat:` - adding a mod, script, or feature
- `fix:` - correcting a mistake (wrong version, duplicate entry, broken link)
- `docs:` - documentation-only changes
- `refactor:` - restructuring without changing behavior
- `chore:` - repo maintenance (gitignore, config)

## Branch strategy

- `main` - stable milestones only
- `develop` - active work
- Merge `develop` → `main` via fast-forward after a batch of related changes, not after every single commit

## Scripts

- `python scripts/validate_mods.py` - run before every commit that touches `mods.json`
- `python scripts/generate_install_order.py` - dependency-sorted install order
- `python scripts/generate_checklist.py` - regenerates `docs/download-checklist.md`; re-run after adding mods

## Categories in use

core, bugfix, ui, graphics, quality-of-life, quest, animation, audio, gameplay, location, creature, npc-factions, companion, weapon, armor

## Research standards

- Verify version compatibility with game 1.10.163 specifically where it matters (many mods target Next-Gen by default)
- Note known conflicts/overlaps rather than silently picking one
- Prefer actively maintained mods over abandoned ones when equivalent options exist
- Cross-check LOOT warnings and errors against the database when they surface missing dependencies or patches
