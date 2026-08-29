"""Profile provisioner using official HERMES CLI commands.

This module provisions isolated bot-mode profiles using the official
HERMES CLI (`hermes profile create`) instead of direct filesystem manipulation.
"""

import subprocess
from pathlib import Path


def provision_profile(name: str, role: str, model: str = None, soul_md: str = None, clone: bool = False):
    """Provision a new HERMES profile using official CLI.
    
    Args:
        name: Profile name (becomes ~/.hermes/profiles/<name>/)
        role: Agent role description
        model: Optional model pin (e.g., "anthropic/claude-sonnet-4-20250514")
        soul_md: Optional SOUL.md content for agent persona
        clone: If True, clone config from main profile (shares config, fresh memory)
    
    Returns:
        dict with profile info and status
    """
    # Step 1: Create profile with description
    cmd = ["hermes", "profile", "create", name, "--description", role]
    if clone:
        cmd.append("--clone")
    
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    
    # Step 2: Set model pin (if requested)
    if model:
        subprocess.run(
            ["hermes", "-p", name, "config", "set", "model.default", model],
            capture_output=True, text=True, check=True
        )
    
    # Step 3: Write SOUL.md (if provided)
    if soul_md:
        soul_path = Path.home() / ".hermes" / "profiles" / name / "SOUL.md"
        soul_path.parent.mkdir(parents=True, exist_ok=True)
        with open(soul_path, "w") as f:
            f.write(soul_md)
    
    return {
        "name": name,
        "role": role,
        "model": model,
        "profile_path": str(Path.home() / ".hermes" / "profiles" / name),
        "status": "provisioned"
    }


def list_profiles():
    """List all HERMES profiles using official CLI."""
    result = subprocess.run(
        ["hermes", "profile", "list"],
        capture_output=True, text=True, check=True
    )
    return result.stdout.strip().split("\n")


def verify_profile(name: str) -> bool:
    """Verify a profile exists and is accessible."""
    try:
        result = subprocess.run(
            ["hermes", "-p", name, "chat", "--dry-run"],
            capture_output=True, text=True, timeout=10
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
        return False
