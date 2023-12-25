from typing import Dict
from .base import BaseAction

class AddToTimeAction(BaseAction):
    """
    Class to define an action that adds a specified interval of time to a base time. 
    This is commonly used in workflows to calculate future or past times based on a given base time.

    Attributes:
        type (str): Type of action, set to "Expression".
        kind (str): Specific kind of action, set to "AddToTime".
        inputs (dict): Dictionary storing input parameters for the action.
    """

    def __init__(self, name: str, timeUnit: str, interval: int, baseTime: str = "@{utcNow()}"):
        """
        Initializes a new instance of AddToTimeAction.

        Args:
            name (str): The name of the action.
            timeUnit (str): The unit of time to be added (e.g., 'Minute', 'Hour').
            interval (int): The amount of time to add to the base time.
            baseTime (str): The starting time point. Default is the current UTC time.
        """
        super().__init__(name)
        self.type = "Expression"
        self.kind = "AddToTime"
        self.inputs = {}
        self.inputs["baseTime"] = baseTime
        self.inputs["interval"] = interval
        self.inputs["timeUnit"] = timeUnit

    def export(self) -> Dict:
        """
        Exports the current state and parameters of this action in a dictionary format.

        Returns:
            Dict: A dictionary containing action details and inputs for serialization.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["kind"] = self.kind
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class WaitAction(BaseAction):
    """
    Class to define a wait action in a workflow. This action pauses the workflow for a specified amount of time.

    Attributes:
        type (str): Type of action, set to "Wait".
        interval (dict): Dictionary specifying the count and unit of time for the wait duration.
        inputs (dict): Dictionary storing input parameters for the action.
    """

    def __init__(self, name: str, count: int, unit: str):
        """
        Initializes a new instance of WaitAction.

        Args:
            name (str): The name of the action.
            count (int): The duration of the wait period.
            unit (str): The unit of time for the wait period (e.g., 'Second', 'Minute').
        """
        super().__init__(name)
        self.type = "Wait"
        self.interval = {}
        self.interval["count"] = count
        self.interval["unit"] = unit
        self.inputs = {}
        self.inputs["interval"] = self.interval

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
