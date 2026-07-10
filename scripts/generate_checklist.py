import json
from pathlib import Path

def build_install_order(mods):
    by_id = {mod["id"]: mod for mod in mods}
    active_ids = {mod["id"] for mod in mods if mod.get("status") != "alternative"}

    visited = {}
    order = []

    def visit(mod_id, stack):
        if mod_id in visited or mod_id in stack or mod_id not in by_id or mod_id not in active_ids:
            return
        stack = stack + [mod_id]
        for dep in by_id[mod_id].get("requires", []):
            if dep in active_ids:
                visit(dep, stack)
        visited[mod_id] = True
        order.append(mod_id)

    for mod in mods:
        visit(mod["id"], [])

    return order, by_id

def main():
    path = Path("database/mods.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)

    mods = data["mods"]
    order, by_id = build_install_order(mods)

    lines = []
    lines.append("# Fallout4-Remastered - Download Checklist")
    lines.append("")
    lines.append(f"Total mods to download: {len(order)}")
    lines.append("")
    lines.append("Check off each mod once downloaded. Verify the version matches game 1.10.163 where marked `check-on-nexus`.")
    lines.append("")

    current_category = None
    for mod_id in order:
        mod = by_id[mod_id]
        category = mod.get("category", "uncategorized")
        if category != current_category:
            lines.append(f"\n## {category}\n")
            current_category = category

        version_note = mod.get("version", "")
        line = f"- [ ] [{mod['name']}]({mod['source']})"
        if version_note == "check-on-nexus":
            line += " ⚠️ *verify version for 1.10.163*"
        elif version_note and version_note != "check-on-nexus":
            line += f" (`{version_note}`)"
        lines.append(line)

    output_path = Path("docs/download-checklist.md")
    output_path.parent.mkdir(exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Checklist written to {output_path} ({len(order)} mods)")

    alternatives = [mod for mod in mods if mod.get("status") == "alternative"]
    if alternatives:
        print(f"\nNote: {len(alternatives)} alternative mod(s) NOT included in checklist (your choice to add manually):")
        for mod in alternatives:
            print(f"  - {mod['name']} ({mod['id']})")

if __name__ == "__main__":
    main()
