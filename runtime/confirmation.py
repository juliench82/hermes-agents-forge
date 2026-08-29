"""
Confirmation — Presents team proposal and waits for explicit user approval.

Follows HERMES security best practices: command approval before side-effecting actions.
"""


class Request:
    """Represents an approval request."""
    
    def __init__(self, transaction_id: str, user: str, action: str, resource: str, target: str):
        self.id = transaction_id
        self.transaction_id = transaction_id
        self.user = user
        self.action = action
        self.resource = resource
        self.target = target
        self.status = "pending"
        self.approved = False
        self.denied = False


class ApprovalGateway:
    """
    Gateway for approval-based actions in HERMES runtime.
    
    Ensures side-effecting operations require explicit user consent before execution.
    """
    
    def __init__(self):
        self._pending_approval = None
        self._requests = {}
    
    def request(self, transaction_id: str, user: str, action: str, resource: str, target: str) -> Request:
        req = Request(transaction_id, user, action, resource, target)
        self._requests[transaction_id] = req
        return req
    
    def approve(self, transaction_id: str) -> bool:
        if transaction_id in self._requests:
            self._requests[transaction_id].status = "approved"
            self._requests[transaction_id].approved = True
            return True
        return False
    
    def deny(self, transaction_id: str) -> bool:
        if transaction_id in self._requests:
            self._requests[transaction_id].status = "denied"
            self._requests[transaction_id].denied = True
            return True
        return False
    
    def is_approved(self, transaction_id: str) -> bool:
        req = self._requests.get(transaction_id)
        return req.approved if req else False
    
    def is_denied(self, transaction_id: str) -> bool:
        req = self._requests.get(transaction_id)
        return req.denied if req else False


def present_team_proposal(proposal: dict) -> bool:
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
