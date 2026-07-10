import json
import sys
from pathlib import Path

def main():
    path = Path("database/mods.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    mods = data["mods"]
    print(f"Total mods: {len(mods)}\n")

    ids = {}
    duplicate_ids = []
    missing_fields = []
    required_fields = ["id", "name", "category", "subcategory", "source", "version", "requires", "notes"]

    for i, mod in enumerate(mods):
        mod_id = mod.get("id", f"<MISSING ID at index {i}>")

        # Check duplicate IDs
        if mod_id in ids:
            duplicate_ids.append(mod_id)
        else:
            ids[mod_id] = mod

        # Check missing required fields
        missing = [field for field in required_fields if field not in mod]
        if missing:
            missing_fields.append((mod_id, missing))

    # Check broken 'requires' references
    broken_requires = []
    for mod in mods:
        mod_id = mod.get("id", "UNKNOWN")
        for req in mod.get("requires", []):
            if req not in ids:
                broken_requires.append((mod_id, req))

    # Check broken 'alternativeTo' references
    broken_alt = []
    for mod in mods:
        mod_id = mod.get("id", "UNKNOWN")
        for alt in mod.get("alternativeTo", []):
            if alt not in ids:
                broken_alt.append((mod_id, alt))

    print("=== Duplicate IDs ===")
    print(duplicate_ids if duplicate_ids else "None found ✅")

    print("\n=== Missing required fields ===")
    if missing_fields:
        for mod_id, fields in missing_fields:
            print(f"  {mod_id}: missing {fields}")
    else:
        print("None found ✅")

    print("\n=== Broken 'requires' references ===")
    if broken_requires:
        for mod_id, req in broken_requires:
            print(f"  {mod_id} requires '{req}', which does not exist")
    else:
        print("None found ✅")

    print("\n=== Broken 'alternativeTo' references ===")
    if broken_alt:
        for mod_id, alt in broken_alt:
            print(f"  {mod_id} alternativeTo '{alt}', which does not exist")
    else:
        print("None found ✅")

if __name__ == "__main__":
    main()
