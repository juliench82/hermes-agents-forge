"""
Confirmation — Presents team proposal and waits for explicit user approval.

Follows HERMES security best practices: command approval before side-effecting actions.
"""


def present_team_proposal(proposal: dict) -> bool:
    """
    Present the team proposal to the user and wait for confirmation.

    Returns:
        True if user approved, False otherwise
    """
    print("\n=== Proposed Team ===")
    for i, bot in enumerate(proposal["bots"], 1):
        print(f"Bot {i}: {bot['role']} — Model: {bot['model']} — Skills: {bot['skills']}")

    print("\n**Default Option: Use My Real Browser Profile**")
    print("This will configure your main profile with the team's skills.")
    print("\n**Alternative: Create Isolated Bot-Mode Profiles**")
    print("This will create separate profiles for each bot (isolated config, memory, credentials).")
    print("Note: All bots share the host OS user and filesystem permissions.")

    print("\nDo you approve this team? (yes/no)")
    print("Type 'yes' to proceed, 'no' to cancel, or 'edit' to modify the proposal.")

    response = input("> ").strip().lower()
    return response in ["yes", "approve", "y"]
