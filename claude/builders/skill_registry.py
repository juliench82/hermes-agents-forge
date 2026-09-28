#!/usr/bin/env python3
"""
skill_registry.py — List all available skills and their metadata.

Usage:
    python3 skill_registry.py
"""

from pathlib import Path
import yaml

BASE_DIR = Path(__file__).parent.parent
SKILLS_DIR = BASE_DIR / "skills"


def load_skill_metadata(skill_path: Path) -> dict:
    """Load metadata from a skill's SKILL.md."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return {"name": skill_path.name, "valid": False}
    
    content = skill_md.read_text()
    second_delim = content.find("---", 3)
    if second_delim == -1:
        return {"name": skill_path.name, "valid": False}
    
    frontmatter = content[3:second_delim]
    try:
        metadata = yaml.safe_load(frontmatter)
        metadata["valid"] = True
        metadata["path"] = str(skill_path.relative_to(BASE_DIR))
        return metadata
    except Exception:
        return {"name": skill_path.name, "valid": False}


def main():
    skills = []
    for item in SKILLS_DIR.iterdir():
        if item.is_dir() and (item / "SKILL.md").exists():
            skills.append(item)
    
    print("=" * 70)
    print("  Claude Skill Registry")
    print("=" * 70)
    print(f"\n{len(skills)} skills available:\n")
    
    # Sort by name
    skills_sorted = sorted(skills, key=lambda p: p.name)
    
    for skill_path in skills_sorted:
        metadata = load_skill_metadata(skill_path)
        if not metadata.get("valid"):
            print(f"⚠️  {skill_path.name} — INVALID")
            continue
        
        name = metadata.get("name", "unnamed")
        desc = metadata.get("description", "No description")
        persona = metadata.get("persona", {})
        persona_name = persona.get("name", "No persona") if persona else "No persona"
        archetype = persona.get("archetype", "") if persona else ""
        
        print(f"📦 {name}")
        print(f"   Path: {skill_path.relative_to(SKILLS_DIR.parent)}")
        print(f"   Description: {desc}")
        if persona_name != "No persona":
            print(f"   Persona: {persona_name}" + (f" ({archetype})" if archetype else ""))
        
        # Show dependencies if any
        deps = metadata.get("dependencies", [])
        if deps:
            print(f"   Dependencies: {', '.join(deps)}")
        
        print()
    
    print("=" * 70)


if __name__ == "__main__":
    main()