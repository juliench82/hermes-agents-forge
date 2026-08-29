"""
Configuration generator for HERMES profiles.

Generates config.yaml with:
- Bot Mode protocol enabled by default
- Real browser profile enabled by default
- Model pinning per profile
- Role-specific toolsets
"""

from typing import Dict, List, Any


def generate_config(role: str, model: str, tools: List[str]) -> Dict[str, Any]:
    config = {
        "agent": {
            "bot_mode_protocol": True,
            "description": f"Bot profile for {role} role"
        },
        "browser": {
            "use_real_profile": True
        },
        "model": {
            "default": model
        },
        "toolsets": ["hermes-cli"] + tools
    }
    
    if role == "researcher":
        config["agent"]["skills"] = ["web_search", "web_extract"]
    elif role == "coder":
        config["agent"]["skills"] = ["terminal_execute", "file_ops"]
    elif role == "reviewer":
        config["agent"]["skills"] = ["security_audit"]
    
    return config


def write_config(profile_path: str, config: Dict[str, Any]) -> None:
    import yaml
    from pathlib import Path
    
    config_path = Path(profile_path) / "config.yaml"
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(config_path, "w") as f:
        yaml.dump(config, f, default_flow_style=False, sort_keys=False)
    
    print(f"✅ Wrote config to {config_path}")
