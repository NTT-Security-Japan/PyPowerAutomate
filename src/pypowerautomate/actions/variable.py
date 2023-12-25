from typing import Dict
from .base import BaseAction


class VariableTypes:
    """
    Defines constants for common variable types used in workflow actions.
    """
    string = "string"
    integer = "integer"
    boolean = "boolean"
    float = "float"
    array = "array"
    object = "object"


class InitVariableAction(BaseAction):
    """
    Class to define an action for initializing a variable. This action sets up a new variable with a specified type and an optional initial value.
    """

    def __init__(self, name: str, var_name: str, var_type: str, value=None):
        """
        Initializes a new instance of InitVariableAction.

        Args:
            name (str): The name of the action.
            var_name (str): The name of the variable to initialize.
            var_type (str): The type of the variable, defined in VariableTypes.
            value (optional): The initial value of the variable. Default is None.
        """
        super().__init__(name)
        self.type = "InitializeVariable"
        self.inputs = {}
        self.variables = []
        var = {
            "name": var_name,
            "type": var_type
        }
        if value:
            var["value"] = value
        self.variables.append(var)
        self.inputs["variables"] = self.variables

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: A dictionary containing action details and inputs for serialization.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class SetVariableAction(BaseAction):
    """
    Class to define an action for setting or updating the value of an existing variable.
    """

    def __init__(self, name: str, var_name: str, value):
        """
        Initializes a new instance of SetVariableAction.

        Args:
            name (str): The name of the action.
            var_name (str): The name of the variable to be updated.
            value: The new value to set for the variable.
        """
        super().__init__(name)
        self.type = "SetVariable"
        self.inputs = {
            "name": var_name,
            "value": value
        }

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: A dictionary containing action details and inputs for serialization.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class AppendStringToVariableAction(BaseAction):
    """
    Class to define an action that appends a string to the existing string variable.
    """

    def __init__(self, name: str, var_name: str, value):
        """
        Initializes a new instance of AppendStringToVariableAction.

        Args:
            name (str): The name of the action.
            var_name (str): The name of the string variable to be appended to.
            value (str): The string value to append.
        """
        super().__init__(name)
        self.type = "AppendToStringVariable"
        self.inputs = {
            "name": var_name,
            "value": value
        }

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: A dictionary containing action details and inputs for serialization.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class IncrementVariableAction(BaseAction):
    """
    A class that defines an action to increment the value of a variable.

    Args:
        name (str): The name of the action.
        var_name (str): The name of the variable to be incremented.
        value (Any): The value to be added to the variable.
    """

    def __init__(self, name: str, var_name: str, value):
        super().__init__(name)
        self.type = "IncrementVariable"
        self.inputs = {
            "name": var_name,
            "value": value
        }

    def export(self) -> Dict:
        """
        Exports the action as a dictionary.

        Returns:
            Dict: A dictionary representing the action.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class DecrementVariableAction(BaseAction):
    """
    A class that defines an action to decrement the value of a variable.

    Args:
        name (str): The name of the action.
        var_name (str): The name of the variable to be decremented.
        value (str): The value to be subtracted from the variable.
    """

    def __init__(self, name: str, var_name: str, value: str):
        super().__init__(name)
        self.type = "DecrementVariable"
        self.inputs = {
            "name": var_name,
            "value": value
        }

    def export(self) -> Dict:
        """
        Exports the action as a dictionary.

        Returns:
            Dict: A dictionary representing the action.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d