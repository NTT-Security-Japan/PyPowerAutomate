from typing import List, Dict
from .base import BaseAction

class TableFormat:
    """
    Enumerates the supported formats for table creation actions.
    """
    csv = "CSV"
    html = "HTML"


class SelectAction(BaseAction):
    """
    Defines a selection action similar to the `map` function, transforming an input array or list into a new structure based on specified key-value pairs.
    """
    
    def __init__(self, name: str, inputs: List | str, key: str = None, value: str = None, select: str = None):
        """
        Initializes a new instance of SelectAction.

        Args:
            name (str): The name of the action.
            inputs (List | str): The input list or a Power Automate expression that evaluates to an array.
            key (str, optional): The key used in the output dictionary, only required if select is not provided.
            value (str, optional): The value associated with each key in the output dictionary, only required if select is not provided.
            select (str, optional): A pre-formed selection string defining how inputs are mapped to outputs.
        """
        super().__init__(name)
        self.type = "Select"
        self.inputs = {"from": inputs, "select": {key: value} if key and value else select}

    def export(self) -> Dict:
        """
        Exports the configuration of the SelectAction for use in a workflow.

        Returns:
            Dict: A dictionary containing the configuration of this action.
        """
        d = {"metadata": self.metadata, "type": self.type, "runAfter": self.runafter, "inputs": self.inputs}
        return d


class CreateTableAction(BaseAction):
    """
    Defines an action to create a table from an array of dictionaries or an expression that evaluates to such an array, formatted as CSV or HTML.
    """
    
    def __init__(self, name: str, inputs: List[Dict] | str, format: str):
        """
        Initializes a new instance of CreateTableAction.

        Args:
            name (str): The name of the action.
            inputs (List[Dict] | str): The input data or a Power Automate expression that evaluates to an object array.
            format (str): The format of the output table (e.g., TableFormat.csv, TableFormat.html).
        """
        super().__init__(name)
        self.type = "Table"
        self.inputs = {"from": inputs, "format": format}

    def export(self) -> Dict:
        """
        Exports the configuration of the CreateTableAction for use in a workflow.

        Returns:
            Dict: A dictionary containing the configuration of this action.
        """
        d = {"metadata": self.metadata, "type": self.type, "runAfter": self.runafter, "inputs": self.inputs}
        return d


class ComposeAction(BaseAction):
    """
    Defines an action to compose data into a specified structure, typically used for constructing new data objects.
    """
    
    def __init__(self, name: str, inputs: List | Dict | str):
        """
        Initializes a new instance of ComposeAction.

        Args:
            name (str): The name of the action.
            inputs (List | Dict | str): The input data or expression that defines the output structure.
        """
        super().__init__(name)
        self.type = "Compose"
        self.inputs = inputs

    def export(self) -> Dict:
        """
        Exports the configuration of the ComposeAction for use in a workflow.

        Returns:
            Dict: A dictionary containing the configuration of this action.
        """
        d = {"metadata": self.metadata, "type": self.type, "runAfter": self.runafter, "inputs": self.inputs}
        return d


class FilterArrayAction(BaseAction):
    """
    Defines an action to filter elements of an array based on a specified condition, similar to the `filter` function.
    """
    
    def __init__(self, name: str, inputs: List | str, where: str):
        """
        Initializes a new instance of FilterArrayAction.

        Args:
            name (str): The name of the action.
            inputs (List | str): The input array or a Power Automate expression that evaluates to an array.
            where (str): A Power Automate expression used to evaluate each element of the array.
        """
        super().__init__(name)
        self.type = "Query"
        self.inputs = {"from": inputs, "where": where}

    def export(self) -> Dict:
        """
        Exports the configuration of the FilterArrayAction for use in a workflow.

        Returns:
            Dict: A dictionary containing the configuration of this action.
        """
        d = {"metadata": self.metadata, "type": self.type, "runAfter": self.runafter, "inputs": self.inputs}
        return d


class JoinAction(BaseAction):
    """
    Defines an action to concatenate elements of an array into a single string, separated by a specified delimiter.
    """
    
    def __init__(self, name: str, inputs: List | str, join_with: str):
        """
        Initializes a new instance of JoinAction.

        Args:
            name (str): The name of the action.
            inputs (List | str): The input array or a Power Automate expression that evaluates to an array.
            join_with (str): The delimiter used to join the array elements.
        """
        super().__init__(name)
        self.type = "Join"
        self.inputs = {"from": inputs, "joinWith": join_with}

    def export(self) -> Dict:
        """
        Exports the configuration of the JoinAction for use in a workflow.

        Returns:
            Dict: A dictionary containing the configuration of this action.
        """
        d = {"metadata": self.metadata, "type": self.type, "runAfter": self.runafter, "inputs": self.inputs}
        return d
