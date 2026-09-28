#!/usr/bin/env python3
"""
generate_skill.py — Generate a new skill from templates.

Usage:
    python3 generate_skill.py --name my-skill --description "What it does" \\
        --persona-name "My Persona" --archetype "Builder" \\
        --voice "Action-oriented" \\
        --strengths "strength1,strength2" \\
        --blind-spots "blindspot1,blindspot2" \\
        --patterns "pattern1,pattern2"
"""

import argparse
from typing import Dict, Any
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required. Install with: pip install pyyaml")
    exit(1)

BASE_DIR = Path(__file__).parent.parent
TEMPLATE_DIR = BASE_DIR / "templates"
SKILLS_DIR = BASE_DIR / "skills"


def generate_skill(name: str, description: str, persona_name: str, 
                   archetype: str, voice: str, 
                   strengths: str, blind_spots: str, patterns: str, 
                   purpose: str) -> str:
    """Generate a .clmd skill file from templates and parameters."""
    
    # Load template
    template_path = TEMPLATE_DIR / "standard-skill.md"
    with open(template_path, 'r') as f:
        template = f.read()
    
    # Build persona metadata
    persona: Dict[str, Any] = {
        "name": persona_name,
        "archetype": archetype,
        "voice": voice,
        "strengths": [s.strip() for s in strengths.split(",")] if strengths else [],
        "blind_spots": [s.strip() for s in blind_spots.split(",")] if blind_spots else [],
        "communication_patterns": [p.strip().strip('"') for p in patterns.split(",")] if patterns else []
    }
    
    # Build frontmatter
    frontmatter: Dict[str, Any] = {
        "name": name,
        "description": description,
        "persona": persona
    }
    
    # Format the frontmatter
    frontmatter_yaml = yaml.dump(frontmatter, default_flow_style=False)
    
    # Populate template (simple replacement)
    skill_content = template
    strength_list = [s.strip() for s in strengths.split(",")] if strengths else []
    blindspot_list = [s.strip() for s in blind_spots.split(",")] if blind_spots else []
    pattern_list = [p.strip().strip('"') for p in patterns.split(",")] if patterns else []
    
    replacements = {
        "{{SKILL_NAME}}": name,
        "{{DESCRIPTION}}": description,
        "{{PERSONA_NAME}}": persona_name,
        "{{ARCHETYPE}}": archetype,
        "{{VOICE}}": voice,
        "{{STRENGTH_1}}": strength_list[0] if len(strength_list) > 0 else "",
        "{{STRENGTH_2}}": strength_list[1] if len(strength_list) > 1 else "",
        "{{STRENGTH_3}}": strength_list[2] if len(strength_list) > 2 else "",
        "{{BLIND_SPOT_1}}": blindspot_list[0] if len(blindspot_list) > 0 else "",
        "{{BLIND_SPOT_2}}": blindspot_list[1] if len(blindspot_list) > 1 else "",
        "{{PATTERN_1}}": pattern_list[0] if len(pattern_list) > 0 else "",
        "{{PATTERN_2}}": pattern_list[1] if len(pattern_list) > 1 else "",
        "{{PATTERN_3}}": pattern_list[2] if len(pattern_list) > 2 else "",
        "{{SKILL_DISPLAY_NAME}}": persona_name,
        "{{PURPOSE}}": purpose or "TODO: Describe the core purpose",
    }
    
    for placeholder, value in replacements.items():
        skill_content = skill_content.replace(placeholder, value)
    
    # Build the final file content
    full_content = f"---\n{frontmatter_yaml}---\n\n{skill_content}"
    
    # Write the skill file
    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    output_path = SKILLS_DIR / f"{name}.clmd"
    
    with open(output_path, 'w') as f:
        f.write(full_content)
    
    print(f"✅ Skill generated: {output_path}")
    print(f"   Name: {name}")
    print(f"   Persona: {persona_name} ({archetype})")
    return str(output_path)


def main():
    parser = argparse.ArgumentParser(
        description="Generate a new Codex skill from templates"
    )
    parser.add_argument("--name", required=True, help="Skill name (lowercase, hyphens)")
    parser.add_argument("--description", required=True, help="Short description")
    parser.add_argument("--persona-name", required=True, help="Persona display name")
    parser.add_argument("--archetype", required=True, 
                        choices=["Researcher", "Analyst", "Coordinator", "Builder", 
                                 "Specialist", "Gatekeeper", "Planner"],
                        help="Persona archetype")
    parser.add_argument("--voice", required=True, help="Communication style")
    parser.add_argument("--strengths", help="Comma-separated strengths")
    parser.add_argument("--blind-spots", help="Comma-separated blind spots")
    parser.add_argument("--patterns", help="Comma-separated communication patterns")
    parser.add_argument("--purpose", help="Core purpose statement")
    
    args = parser.parse_args()
    
    generate_skill(
        name=args.name,
        description=args.description,
        persona_name=args.persona_name,
        archetype=args.archetype,
        voice=args.voice,
        strengths=args.strengths or "",
        blind_spots=args.blind_spots or "",
        patterns=args.patterns or "",
        purpose=args.purpose or ""
    )


if __name__ == "__main__":
    main()