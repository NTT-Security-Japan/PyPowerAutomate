import uuid
from typing import List, Dict
from .base import BaseAction
from ..connections import Connections


class CreateFlowAction(BaseAction):
    """
    Class to define the action of creating a flow. It translates defined string variables into JSON and aims to create a flow based on this JSON.

    Attributes:
        connection_host (dict): Predefined connection details for Microsoft PowerApps flow management API.
    """
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_flowmanagement",
        "connectionName": "shared_flowmanagement",
        "operationId": "CreateFlow"
    }

    def __init__(self, name: str):
        """
        Initializes a new instance of the CreateFlowAction.

        Args:
            name (str): The name of the action.
        """
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = CreateFlowAction.connection_host
        self.inputs["parameters"] = {}

    def set_parameters(self, display_name: str, var_name: str, connection_ref: Connections):
        """
        Sets the parameters required for the flow creation.

        Args:
            display_name (str): The display name of the flow.
            var_name (str): The variable name in the workflow that holds the flow definition.
            connection_ref (Connections): The connection references needed for the flow.
        """
        self.parameters["environmentName"] = "@workflow()?['tags/environmentName']"
        self.parameters["Flow/properties/displayName"] = display_name
        self.parameters["Flow/properties/definition"] = f"@json(variables('{var_name}'))"
        self.parameters["Flow/properties/state"] = "Started"
        self.parameters["Flow/properties/connectionReferences"] = connection_ref.export()
        self.inputs["parameters"] = self.parameters

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: The dictionary containing action details and parameters.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class DeleteFlowAction(BaseAction):
    """
    Class to define the action of deleting a flow.

    Attributes:
        connection_host (dict): Predefined connection details for Microsoft PowerApps flow management API.
    """
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_flowmanagement",
        "connectionName": "shared_flowmanagement",
        "operationId": "DeleteFlow"
    }

    def __init__(self, name: str):
        """
        Initializes a new instance of the DeleteFlowAction.

        Args:
            name (str): The name of the action.
        """
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = DeleteFlowAction.connection_host
        self.inputs["parameters"] = {
            "environmentName": "@workflow()?['tags/environmentName']",
            "flowName": "@workflow()?['tags']?['logicAppName']"
        }

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: The dictionary containing action details and parameters.
        """
        d = {}
        d["metadata"] = self.metadata
        d["runAfter"] = self.runafter
        d["type"] = self.type
        d["inputs"] = self.inputs
        return d


class ListConnectionsAction(BaseAction):
    """
    Class to define the action to retrieve a list of active connections in an account.

    Attributes:
        connection_host (dict): Predefined connection details for Microsoft PowerApps flow management API.
    """
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_flowmanagement",
        "connectionName": "shared_flowmanagement",
        "operationId": "ListConnections"
    }

    def __init__(self, name: str):
        """
        Initializes a new instance of the ListConnectionsAction.

        Args:
            name (str): The name of the action.
        """
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = ListConnectionsAction.connection_host
        self.inputs["parameters"] = {
            "environmentName": "@workflow()?['tags/environmentName']",
        }

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: The dictionary containing action details and parameters.
        """
        d = {}
        d["metadata"] = self.metadata
        d["runAfter"] = self.runafter
        d["type"] = self.type
        d["inputs"] = self.inputs
        return d


class ListUserEnvironmentsAction(BaseAction):
    """
    Class to define the action to list all user environments in an account.

    Attributes:
        connection_host (dict): Predefined connection details for Microsoft PowerApps flow management API.
    """
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_flowmanagement",
        "connectionName": "shared_flowmanagement",
        "operationId": "ListUserEnvironments"
    }

    def __init__(self, name: str):
        """
        Initializes a new instance of the ListUserEnvironmentsAction.

        Args:
            name (str): The name of the action.
        """
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: The dictionary containing action details and parameters.
        """
        d = {}
        d["metadata"] = self.metadata
        d["runAfter"] = self.runafter
        d["type"] = self.type
        d["inputs"] = self.inputs
        return d
