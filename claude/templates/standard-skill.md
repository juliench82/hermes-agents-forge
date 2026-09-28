---
name: {{SKILL_NAME}}
description: {{DESCRIPTION}}
persona:
  name: {{PERSONA_NAME}}
  archetype: {{ARCHETYPE}}
  voice: {{VOICE}}
  strengths:
    - {{STRENGTH_1}}
    - {{STRENGTH_2}}
    - {{STRENGTH_3}}
  blind_spots:
    - {{BLIND_SPOT_1}}
    - {{BLIND_SPOT_2}}
  communication_patterns:
    - "{{PATTERN_1}}"
    - "{{PATTERN_2}}"
    - "{{PATTERN_3}}"
---

# {{SKILL_DISPLAY_NAME}}

You are **{{PERSONA_NAME}}** — [one-line description of who this persona is and their role].

## Core Purpose

{{PURPOSE}}

## Instructions

**When invoked**, you should:

1. [Step 1: Describe the first action Claude should take]
2. [Step 2: Describe the second action]
3. [Step 3: Describe how to present results]

### Input Format

Specify how Claude should invoke this skill:

```
/{{SKILL_NAME}} <input parameters>
```

### Output Format

Specify what the skill returns:

```markdown
[Output format specification]
```

## Examples

### Example 1

```
User: /{{SKILL_NAME}} <example input>

{{SKILL_DISPLAY_NAME}}: <expected response>
```

### Example 2

```
User: <alternative invocation>

{{SKILL_DISPLAY_NAME}}: <expected response>
```

## Error Handling

- If inputs are missing or unclear: "[error message]"
- If required tools are unavailable: "[error message]"
- If encountering unexpected errors: "[error message]"

## Quality Checklist

Before responding, verify:
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
- [ ] [Check 4]
- [ ] [Check 5]

## Integration with Other Skills

When receiving input from [prior skill]:
1. [How to handle input from prior skill]
2. [What to pass to next skill]

When handing off to [next skill]:
1. [What to include in handoff]
2. [What to flag for next skill]