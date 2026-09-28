#!/usr/bin/env python3
"""
package_skills.py — Batch package all Claude skills as ZIP files for upload.

Usage:
    python3 package_skills.py
    
Creates ZIP files in the packages/ directory for each skill in skills/
"""

import os
import zipfile
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).parent.parent
SKILLS_DIR = BASE_DIR / "skills"
PACKAGES_DIR = BASE_DIR / "packages"


def validate_skill_md(skill_path: Path) -> dict:
    """Basic validation of a skill's SKILL.md file."""
    skill_md = skill_path / "SKILL.md"
    results = {"valid": True, "errors": [], "warnings": [], "name": None}
    
    if not skill_md.exists():
        results["valid"] = False
        results["errors"].append("SKILL.md not found")
        return results
    
    content = skill_md.read_text()
    
    if not content.startswith("---"):
        results["valid"] = False
        results["errors"].append("Must start with YAML frontmatter (---)")
        return results
    
    # Find closing ---
    second_delim = content.find("---", 3)
    if second_delim == -1:
        results["valid"] = False
        results["errors"].append("Frontmatter not closed")
        return results
    
    # Parse frontmatter
    frontmatter = content[3:second_delim]
    try:
        import yaml
        metadata = yaml.safe_load(frontmatter)
    except Exception as e:
        results["valid"] = False
        results["errors"].append(f"Invalid YAML: {e}")
        return results
    
    # Check required fields
    if "name" not in metadata:
        results["valid"] = False
        results["errors"].append("Missing 'name' field")
    else:
        results["name"] = metadata["name"]
    
    if "description" not in metadata:
        results["valid"] = False
        results["errors"].append("Missing 'description' field")
    
    # Check name validity
    if results["name"]:
        if not results["name"].replace("-", "").replace("_", "").isalnum():
            results["errors"].append(f"Invalid name: {results['name']}")
            results["valid"] = False
    
    return results


def package_skill(skill_path: Path, output_dir: Path) -> Path:
    """Package a skill directory into a ZIP file."""
    skill_md = skill_path / "SKILL.md"
    
    # Parse frontmatter for skill name
    content = skill_md.read_text()
    second_delim = content.find("---", 3)
    frontmatter = content[3:second_delim]
    import yaml
    metadata = yaml.safe_load(frontmatter)
    
    skill_name = metadata["name"]
    zip_path = output_dir / f"{skill_name}.zip"
    
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for item in skill_path.rglob("*"):
            if item.is_file():
                arcname = item.relative_to(skill_path)
                zf.write(item, arcname)
    
    return zip_path


def main():
    # Ensure packages directory exists
    PACKAGES_DIR.mkdir(parents=True, exist_ok=True)
    
    # Find all skills
    skills = []
    for item in SKILLS_DIR.iterdir():
        if item.is_dir() and (item / "SKILL.md").exists():
            skills.append(item)
    
    if not skills:
        print("No skills found in", SKILLS_DIR)
        return
    
    print(f"Found {len(skills)} skills:\n")
    
    success_count = 0
    failed_count = 0
    
    for skill_path in sorted(skills):
        print(f"📦 {skill_path.name}/")
        
        # Validate
        validation = validate_skill_md(skill_path)
        
        if not validation["valid"]:
            print(f"   ❌ Invalid: {', '.join(validation['errors'])}")
            failed_count += 1
            continue
        
        # Package
        try:
            zip_path = package_skill(skill_path, PACKAGES_DIR)
            size_kb = zip_path.stat().st_size / 1024
            print(f"   ✅ Validated and packaged: {validation['name']} ({size_kb:.1f} KB)")
            success_count += 1
        except Exception as e:
            print(f"   ❌ Package failed: {e}")
            failed_count += 1
    
    print(f"\n📊 Results: {success_count} packaged, {failed_count} failed")
    
    if failed_count > 0:
        print("\n⚠️  Some skills failed validation. Fix errors before uploading.")
    else:
        print("\n✅ All skills ready for upload to Claude Desktop!")
        print(f"   Found in: {PACKAGES_DIR}")


if __name__ == "__main__":
    main()