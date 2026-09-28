#!/usr/bin/env python3
"""
install_skills.py — Install all pre-built skills to ~/.codex/skills/

Usage:
    python3 install_skills.py
    python3 install_skills.py --dry-run  # Show what would be installed
"""

import os
import shutil
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SKILLS_DIR = BASE_DIR / "skills"
DEFAULT_TARGET = Path.home() / ".codex" / "skills"


def validate_clmd(skill_file: Path) -> dict:
    """Validate a .clmd file's frontmatter."""
    content = skill_file.read_text()
    
    if not content.startswith("---"):
        return {"valid": False, "error": "Must start with YAML frontmatter"}
    
    second_delim = content.find("---", 3)
    if second_delim == -1:
        return {"valid": False, "error": "Frontmatter not closed"}
    
    frontmatter = content[3:second_delim]
    try:
        metadata = yaml.safe_load(frontmatter)
    except Exception as e:
        return {"valid": False, "error": f"Invalid YAML: {e}"}
    
    required = ["name", "description", "persona"]
    for field in required:
        if field not in metadata:
            return {"valid": False, "error": f"Missing required field: {field}"}
    
    if "name" not in metadata.get("persona", {}):
        return {"valid": False, "error": "Persona missing 'name'"}
    
    if "archetype" not in metadata.get("persona", {}):
        return {"valid": False, "error": "Persona missing 'archetype'"}
    
    return {"valid": True, "name": metadata["name"]}


def install_skills(target_dir: Path, dry_run: bool = False):
    """Install all skills to target directory."""
    if not SKILLS_DIR.exists():
        print(f"❌ Skills directory not found: {SKILLS_DIR}")
        return
    
    skills = list(SKILLS_DIR.glob("*.clmd"))
    if not skills:
        print(f"No .clmd skills found in {SKILLS_DIR}")
        return
    
    print(f"Found {len(skills)} skills to install:\n")
    
    success = 0
    failed = 0
    
    for skill_file in sorted(skills):
        validation = validate_clmd(skill_file)
        
        if not validation["valid"]:
            print(f"  ❌ {skill_file.name}: Invalid — {validation['error']}")
            failed += 1
            continue
        
        target_path = target_dir / skill_file.name
        
        if dry_run:
            print(f"  📄 {validation['name']} → {target_path} (dry-run)")
            success += 1
        else:
            if target_dir == DEFAULT_TARGET:
                target_dir.mkdir(parents=True, exist_ok=True)
            
            shutil.copy2(skill_file, target_path)
            print(f"  ✅ {validation['name']} → {target_path}")
            success += 1
    
    print(f"\n📊 Results: {success} installed, {failed} failed")
    
    if dry_run:
        print(f"\n(Dry run — no files were actually installed)")
        print(f"To install for real: python3 install_skills.py")
    elif success > 0:
        print(f"\n✅ Skills installed to {target_dir}")
        print(f"Restart Codex to activate the skills.")


def main():
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Install pre-built Codex skills to the skills directory"
    )
    parser.add_argument(
        "--target", "-t",
        help=f"Target directory (default: {DEFAULT_TARGET})",
        default=str(DEFAULT_TARGET)
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be installed without copying"
    )
    
    args = parser.parse_args()
    
    target = Path(args.target)
    install_skills(target, args.dry_run)


if __name__ == "__main__":
    main()