import json
from pathlib import Path

def main():
    path = Path("database/mods.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    mods = data["mods"]
    by_id = {mod["id"]: mod for mod in mods}

    # Separate active mods from alternatives (alternatives aren't part of the default install)
    active_ids = {mod["id"] for mod in mods if mod.get("status") != "alternative"}

    visited = {}
    order = []
    cycle_warnings = []

    def visit(mod_id, stack):
        if mod_id in visited:
            return
        if mod_id in stack:
            cycle_warnings.append(f"Circular dependency detected: {' -> '.join(stack)} -> {mod_id}")
            return
        if mod_id not in by_id:
            return  # already reported by validate_mods.py if broken
        if mod_id not in active_ids:
            return  # skip alternatives, they're not installed by default

        stack = stack + [mod_id]
        for dep in by_id[mod_id].get("requires", []):
            if dep in active_ids:
                visit(dep, stack)

        visited[mod_id] = True
        order.append(mod_id)

    for mod in mods:
        visit(mod["id"], [])

    print(f"Install order for {len(order)} active mods (dependencies first):\n")
    for i, mod_id in enumerate(order, start=1):
        name = by_id[mod_id]["name"]
        category = by_id[mod_id]["category"]
        print(f"{i:3}. [{category}] {name}  ({mod_id})")

    if cycle_warnings:
        print("\n=== WARNING: Circular dependencies found ===")
        for w in cycle_warnings:
            print(f"  {w}")

    alternatives = [mod for mod in mods if mod.get("status") == "alternative"]
    if alternatives:
        print(f"\n=== {len(alternatives)} alternative mods excluded from install order (choose manually) ===")
        for mod in alternatives:
            alt_to = ", ".join(mod.get("alternativeTo", []))
            print(f"  {mod['name']} ({mod['id']}) - alternative to: {alt_to}")

if __name__ == "__main__":
    main()
