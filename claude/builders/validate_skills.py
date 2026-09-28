#!/usr/bin/env python3
"""
validate_skills.py — Batch validate all Claude skills.

Usage:
    python3 validate_skills.py
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
SKILLS_DIR = BASE_DIR / "skills"


def validate_skill(skill_path: Path) -> dict:
    """Validate a skill directory."""
    results = {"valid": True, "errors": [], "warnings": [], "name": None, "checks": []}
    
    # Check 1: SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        results["valid"] = False
        results["errors"].append("SKILL.md not found")
        return results
    results["checks"].append("✓ SKILL.md exists")
    
    # Check 2: Valid frontmatter
    content = skill_md.read_text()
    if not content.startswith("---"):
        results["valid"] = False
        results["errors"].append("SKILL.md must start with YAML frontmatter (---)")
        return results
    
    second_delim = content.find("---", 3)
    if second_delim == -1:
        results["valid"] = False
        results["errors"].append("SKILL.md frontmatter not properly closed")
        return results
    
    results["checks"].append("✓ YAML frontmatter is valid")
    
    # Parse frontmatter
    frontmatter = content[3:second_delim]
    try:
        import yaml
        metadata = yaml.safe_load(frontmatter)
    except Exception as e:
        results["valid"] = False
        results["errors"].append(f"Invalid YAML in frontmatter: {e}")
        return results
    
    # Check 3: name field
    if "name" not in metadata:
        results["valid"] = False
        results["errors"].append("SKILL.md frontmatter missing 'name' field")
    else:
        name = metadata["name"]
        if not isinstance(name, str) or not name.strip():
            results["valid"] = False
            results["errors"].append("'name' field must be a non-empty string")
        elif not name.replace("-", "").replace("_", "").isalnum():
            results["valid"] = False
            results["errors"].append(f"'name' contains invalid characters: {name}")
        else:
            results["name"] = name
            results["checks"].append(f"✓ Name: '{name}'")
    
    # Check 4: description field
    if "description" not in metadata:
        results["valid"] = False
        results["errors"].append("SKILL.md frontmatter missing 'description' field")
    else:
        desc = metadata["description"]
        if not isinstance(desc, str) or not desc.strip():
            results["valid"] = False
            results["errors"].append("'description' field must be a non-empty string")
        elif len(desc) > 200:
            results["warnings"].append(f"Description is {len(desc)} chars (recommended < 200)")
        else:
            results["checks"].append(f"✓ Description: '{desc[:60]}...'")
    
    # Check 5: persona field (optional but recommended)
    if "persona" in metadata:
        persona = metadata["persona"]
        required_fields = ["name", "archetype", "voice"]
        missing = [f for f in required_fields if f not in persona]
        if missing:
            results["warnings"].append(f"Persona missing fields: {', '.join(missing)}")
        else:
            results["checks"].append(f"✓ Persona: {persona.get('name', 'unknown')} ({persona.get('archetype', 'unknown')})")
    
    # Check 6: Hooks validation
    if "hooks" in metadata:
        hooks = metadata["hooks"]
        if not isinstance(hooks, list):
            results["errors"].append("'hooks' must be a list")
            results["valid"] = False
        else:
            valid_events = [
                "before_user_prompt", "after_tool_result",
                "before_tool_use", "after_tool_use",
                "user_message_sent"
            ]
            for i, hook in enumerate(hooks):
                if "event" not in hook:
                    results["errors"].append(f"Hook {i} missing 'event' field")
                    results["valid"] = False
                elif hook["event"] not in valid_events:
                    results["warnings"].append(f"Hook {i} uses non-standard event: {hook['event']}")
                
                if "action" not in hook:
                    results["errors"].append(f"Hook {i} missing 'action' field")
                    results["valid"] = False
                else:
                    action_path = skill_path / hook["action"]
                    if not action_path.exists():
                        results["errors"].append(f"Hook {i} action file not found: {hook['action']}")
                        results["valid"] = False
                    else:
                        results["checks"].append(f"✓ Hook {i} action: {hook['action']}")
    
    return results


def main():
    # Find all skills
    skills = []
    for item in SKILLS_DIR.iterdir():
        if item.is_dir() and (item / "SKILL.md").exists():
            skills.append(item)
    
    if not skills:
        print("No skills found in", SKILLS_DIR)
        return
    
    print(f"\n=== Validating {len(skills)} skills ===\n")
    
    all_valid = True
    
    for skill_path in sorted(skills):
        print(f"🔍 {skill_path.name}/")
        results = validate_skill(skill_path)
        
        for check in results["checks"]:
            print(f"   {check}")
        
        for warning in results["warnings"]:
            print(f"   ⚠️  {warning}")
        
        for error in results["errors"]:
            print(f"   ✗ {error}")
        
        if results["valid"]:
            print(f"   ✅ VALID: {results['name'] or 'unnamed'}")
        else:
            all_valid = False
            print(f"   ❌ INVALID")
        print()
    
    if all_valid:
        print(f"✅ All {len(skills)} skills passed validation")
        print(f"\nReady to package: python3 package_skills.py")
    else:
        print("❌ Some skills failed validation")
        sys.exit(1)


if __name__ == "__main__":
    main()