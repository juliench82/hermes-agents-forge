"""
Onboarding Wizard for HERMES-Forge.

Conducts user interview to collect:
- Domain/project context
- Goals and outcomes
- Desired bot roles
- Tool permissions
- Model preferences per bot
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field


@dataclass
class BotSpec:
    name: str
    role: str
    description: str
    model: str = "anthropic/claude-sonnet-4"
    tools: List[str] = field(default_factory=list)


@dataclass
class TeamSpec:
    domain: str = ""
    goals: str = ""
    bots: List[BotSpec] = field(default_factory=list)
    use_real_browser: bool = True


class OnboardingWizard:
    def __init__(self):
        self.domain = ""
        self.goals = ""
        self.roles: List[str] = []
        self.tools: List[str] = []
        self.model_preferences: Dict[str, str] = {}
        self.team_spec: Optional[TeamSpec] = None
    
    def run_interview(self) -> TeamSpec:
        print("\n=== HERMES-Forge Team Setup ===\n")
        
        self.domain = input("1. What domain or project are you working in?\n   (e.g., 'SaaS startup', 'XRPL blockchain', 'research paper'): ").strip()
        
        self.goals = input("\n2. What outcomes do you want from this agent team?\n   (e.g., 'daily market digest', 'PR reviews', 'code deployment'): ").strip()
        
        print("\n3. Which specialist roles do you need? (comma-separated)\n   Suggested: researcher, coder, reviewer, coordinator")
        roles_input = input("   Your choices: ").strip()
        self.roles = [r.strip() for r in roles_input.split(",") if r.strip()]
        
        print("\n4. Which capabilities should bots have? (comma-separated)\n   Options: browser, terminal, github_mcp, graphiti_mcp")
        tools_input = input("   Your choices: ").strip()
        self.tools = [t.strip() for t in tools_input.split(",") if t.strip()]
        
        print("\n5. Model preferences per bot:")
        for role in self.roles:
            model = input(f"   Which model for @{role}?\n   (e.g., claude-opus-4, gpt-5, claude-sonnet-4): ").strip()
            if model:
                self.model_preferences[role] = model
        
        self.team_spec = TeamSpec(
            domain=self.domain,
            goals=self.goals,
            bots=[
                BotSpec(
                    name=role,
                    role=role,
                    description=self._get_role_description(role),
                    model=self.model_preferences.get(role, "anthropic/claude-sonnet-4"),
                    tools=self.tools
                )
                for role in self.roles
            ],
            use_real_browser="browser" in self.tools
        )
        
        return self.team_spec
    
    def _get_role_description(self, role: str) -> str:
        descriptions = {
            "researcher": "Gathers evidence from web, docs, GitHub",
            "coder": "Implements features, runs tests, deploys",
            "reviewer": "Security audits, challenges assumptions",
            "coordinator": "Synthesizes outputs, manages handoffs"
        }
        return descriptions.get(role, f"Specialist for {role} tasks")
    
    def present_team_proposal(self) -> str:
        if not self.team_spec:
            raise ValueError("Must run interview first")
        
        proposal = "\n### Proposed Team ###\n\n"
        for bot in self.team_spec.bots:
            proposal += f"- @{bot.name}: {bot.model}, tools={bot.tools}\n"
        
        proposal += "\nEach bot gets:\n"
        proposal += "- Isolated profile (~/.hermes/profiles/<name>/)\n"
        proposal += "- Real browser profile (your logins)\n"
        proposal += "- Bot Mode protocol (can message each other)\n"
        proposal += "\nProceed with provisioning? [y/N]: "
        
        return proposal
