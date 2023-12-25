from typing import Dict
from .base import BaseAction

class StartAndWaitForAnApprovalAction(BaseAction):
    """
    Represents an action to start and wait for an approval process using a specified connection host.

    Attributes:
        connection_host (dict): Static configuration detailing the API connection for approval actions.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_approvals",
        "connectionName": "shared_approvals",
        "operationId": "StartAndWaitForAnApproval",
    }

    def __init__(self, name: str, email: str):
        """
        Initializes a new instance of the StartAndWaitForAnApprovalAction.

        Args:
            name (str): The name of the action.
            email (str): The email address of the individual to whom the approval request is assigned.
        """
        super().__init__(name)
        self.type = "OpenApiConnectionWebhook"
        self.email: str = email
        self.title = "PyPowerAutomate Flow"

    def export(self) -> Dict:
        """
        Exports the current state and configuration of this action to a dictionary suitable for use in APIs.

        Returns:
            Dict: A dictionary containing metadata, type, runAfter conditions, and inputs specific to this action.
        """
        inputs = {}
        parameters = {}

        parameters["approvalType"] = "Basic"
        parameters["WebhookApprovalCreationInput/title"] = self.title
        parameters["WebhookApprovalCreationInput/assignedTo"] = self.email
        parameters["WebhookApprovalCreationInput/enableNotifications"] = True
        parameters["WebhookApprovalCreationInput/enableReassignment"] = True

        inputs["host"] = StartAndWaitForAnApprovalAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class WaitForAnApprovalAction(BaseAction):
    """
    Represents an action to wait for an approval to be completed using a specified connection host.

    Attributes:
        connection_host (dict): Static configuration detailing the API connection for approval actions.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_approvals",
        "connectionName": "shared_approvals",
        "operationId": "WaitForAnApproval",
    }

    def __init__(self, name: str, approval_name: str):
        """
        Initializes a new instance of the WaitForAnApprovalAction.

        Args:
            name (str): The name of the action.
            approval_name (str): The unique name of the approval process to wait for.
        """
        super().__init__(name)
        self.type = "OpenApiConnectionWebhook"
        self.approval_name: str = approval_name

    def export(self) -> Dict:
        """
        Exports the current state and configuration of this action to a dictionary suitable for use in APIs.

        Returns:
            Dict: A dictionary containing metadata, type, runAfter conditions, and inputs specific to this action.
        """
        inputs = {}
        parameters = {}
        parameters["approvalName"] = self.approval_name

        inputs["host"] = WaitForAnApprovalAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d
