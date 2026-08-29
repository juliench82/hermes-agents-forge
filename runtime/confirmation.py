"""
Confirmation — Presents team proposal and waits for explicit user approval.

Follows HERMES security best practices: command approval before side-effecting actions.
"""


class ApprovalGateway:
    """
    Gateway for approval-based actions in HERMES runtime.
    
    Ensures side-effecting operations require explicit user consent before execution.
    """
    
    def __init__(self):
        self._pending_approval = None
    
    def request_approval(self, action: str, details: dict) -> bool:
        """
        Request user approval for an action.
        
        Args:
            action: Name of the action (e.g., "provision_profile")
            details: Dictionary containing action details
            
        Returns:
            True if user approved, False otherwise
        """
        print(f"\n=== Approval Required: {action} ===")
        for key, value in details.items():
            print(f"{key}: {value}")
        
        print("\nDo you approve this action? (yes/no)")
        response = input("> ").strip().lower()
        return response in ["yes", "approve", "y"]
    
    def execute_if_approved(self, action: str, details: dict, callback) -> any:
        """
        Request approval and execute callback if approved.
        
        Args:
            action: Name of the action
            details: Dictionary containing action details
            callback: Function to execute if approved
            
        Returns:
            Result of callback if approved, None otherwise
        """
        if self.request_approval(action, details):
            return callback(**details)
        return None


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
    print("Note: All bots support the host OS user and filesystem permissions.")

    print("\nDo you approve this team? (yes/no)")
    print("Type 'yes' to proceed, 'no' to cancel, or 'edit' to modify the proposal.")

    response = input("> ").strip().lower()
    return response in ["yes", "approve", "y"]
