# Codex Skill Development Guide

## Overview

This guide explains how to develop, test, and install custom skills for Codex using the bootstrap system.

## Skill Format

Codex skills use `.clmd` files (Codex Markdown) — markdown files with YAML frontmatter:

```yaml
---
name: <skill-name>
description: <short description>
persona:
  name: <persona-name>
  archetype: <role-type>
  voice: <communication style>
  strengths: [<key strengths>]
  blind_spots: [<limitations>]
  communication_patterns: [<interaction patterns>]
---
```

## Creating a New Skill

### Method 1: Interactive Generation

```bash
cd codex/builders
python3 generate_skill.py \
    --name my-skill \
    --description "What it does" \
    --persona-name "My Persona" \
    --archetype "Builder" \
    --voice "Action-oriented" \
    --strengths "strength1,strength2,strength3" \
    --blind-spots "blindspot1,blindspot2" \
    --patterns "pattern1,pattern2,pattern3" \
    --purpose "Core purpose statement"
```

### Method 2: Manual Creation

1. Copy a template:
   ```bash
   cp templates/standard-skill.md skills/my-skill.clmd
   ```

2. Edit the frontmatter and body
3. Validate:
   ```bash
   python3 builders/validate_skill.py skills/my-skill.clmd
   ```

## Installing Skills

### Install to Personal Skills Directory

```bash
python3 codex/builders/install_skills.py
```

This copies all `.clmd` files to `~/.codex/skills/`.

### Per-Project Skills

```bash
mkdir -p .codex/skills/
cp /path/to/skills/*.clmd .codex/skills/
```

## Validation

Validate a single skill:
```bash
python3 codex/builders/validate_skill.py codex/skills/market-scout.clmd
```

Validate all skills:
```bash
python3 codex/builders/validate_skills.py
```

## Using Skills in Codex

When you have skills installed, you can invoke them by mentioning the persona:

```
Use the Market Scout persona to research AI tools for fitness coaching
```

Or chain multiple skills:

```
Act as the Product Manager and create a PRD for a task management app. 
Then act as the Product Architect and design the architecture.
Then act as MVP Builder and build the core API.
```

## Development Workflow

1. **Design**: Use the interview script to plan your skill team
2. **Create**: Generate or manually create skill files
3. **Validate**: Run validation to ensure format compliance
4. **Test**: Invoke the skill in Codex to verify behavior
5. **Iterate**: Refine based on testing
6. **Install**: Copy to `~/.codex/skills/` for regular use
7. **Commit**: Push to the repo for team sharing

## Persona Schema

See `templates/role-schema.md` for the complete schema and archetype definitions.

## Best Practices

1. **One skill, one persona** — Keep personas focused and consistent
2. **Clear boundaries** — Each skill should have non-overlapping responsibilities
3. **Cite sources** — Build trust with verified information
4. **Handle uncertainty** — Always flag what you don't know
5. **Provide examples** — Show exact usage patterns
6. **Include error handling** — Tell Codex how to respond to problems
7. **Define quality checklists** — Make expectations explicit

## Comparison with Other Platforms

| Feature | Claude Skills | Codex Skills | Hermes Forge |
|---------|---------------|--------------|--------------|
| Format | ZIP archive | `.clmd` markdown | SOUL.md + skills |
| Installation | UI upload | Filesystem copy | CLI command |
| Invocation | `/command` | Persona mention | Profile activation |
| State | Per conversation | Per conversation | Persistent |
| Autonomy | Single skill | Single agent | Multi-agent team |