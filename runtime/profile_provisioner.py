"""
Profile Provisioner — Creates isolated bot-mode profiles for HERMES agents.

Follows HERMES Bot Mode (beta) isolation model:
- Each profile gets its own: config, memory, credentials, chat history
- All bots share the host OS user and filesystem permissions
- Bots communicate through a shared inbox
"""

import os
import shutil
from pathlib import Path


def provision_profile(role: str, model: str, skills: list, use_main_profile: bool = False):
    """
    Provision a profile for a bot role.

    Args:
        role: Bot role name (e.g., "Researcher", "Coder")
        model: Model to use (e.g., "claude-opus-4.6")
        skills: List of skills to install
        use_main_profile: If True, use the main profile instead of creating isolated bot
    """
    if use_main_profile:
        # Configure the main profile with the team's skills
        print(f"Configuring main profile with role: {role}")
        # Add skills to main profile's skill directory
        return

    # Create isolated bot-mode profile
    hermes_home = Path.home() / ".hermes"
    profile_dir = hermes_home / "profiles" / f"forge-{role}"

    # Ensure isolation: each profile gets its own directories
    profile_dir.mkdir(parents=True, exist_ok=True)
    (profile_dir / "config").mkdir(exist_ok=True)
    (profile_dir / "memory").mkdir(exist_ok=True)
    (profile_dir / "credentials").mkdir(exist_ok=True)
    (profile_dir / "sessions").mkdir(exist_ok=True)

    # Write profile configuration
    config_file = profile_dir / "config.yaml"
    config_file.write_text(f"""
model: {model}
skills: {skills}
role: {role}
bot_mode: true
shared_inbox: true
""")

    print(f"Provisioned profile: {profile_dir}")
    return profile_dir
