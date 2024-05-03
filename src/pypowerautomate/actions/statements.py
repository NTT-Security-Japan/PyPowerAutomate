from typing import Dict
from .base import BaseAction
from .actions import Actions, RawActions
from .condition import Condition


class IfStatement(BaseAction):
    """
    A class that defines an If statement.

    Args:
        name (str): The name of the If statement.
        condition (Condition): The condition to be evaluated.
    """

    def __init__(self, name: str, condition: Condition):
        super().__init__(name)
        self.type: str = "If"
        self.condition: Condition = condition
        self.true_actions: Actions = None
        self.false_actions: Actions = None

    def set_true_actions(self, actions: Actions):
        """
        Sets the actions to be executed if the condition is true.

        Args:
            actions (Actions): The actions to be executed if the condition is true.
        """
        self.true_actions = actions

    def set_false_actions(self, actions: Actions):
        """
        Sets the actions to be executed if the condition is false.

        Args:
            actions (Actions): The actions to be executed if the condition is false.
        """
        self.false_actions = actions

    def export(self) -> Dict:
        """
        Exports the If statement as a dictionary.

        Returns:
            Dict: A dictionary representing the If statement.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["expression"] = self.condition.export()

        if self.true_actions:
            d["actions"] = self.true_actions.export()
        else:
            d["actions"] = {}

        if self.false_actions:
            d["else"] = {"actions": self.false_actions.export()}

        return d


class ForeachStatement(BaseAction):
    """
    A class that defines a Foreach statement.

    Args:
        name (str): The name of the Foreach statement.
        foreach (str): The variable to iterate over.
    """

    def __init__(self, name: str, foreach: str):
        super().__init__(name)
        self.type: str = "Foreach"
        self.foreach: str = foreach
        self.actions: Actions = None

    def set_actions(self, actions: Actions):
        """
        Sets the actions to be executed for each iteration.

        Args:
            actions (Actions): The actions to be executed for each iteration.
        """
        self.actions = actions

    def export(self) -> Dict:
        """
        Exports the Foreach statement as a dictionary.

        Returns:
            Dict: A dictionary representing the Foreach statement.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["foreach"] = self.foreach
        d["actions"] = self.actions.export()
        return d


class ScopeStatement(BaseAction):
    """
    A class that defines a Scope statement.

    Args:
        name (str): The name of the Scope statement.
        actions (Actions | RawActions): The actions to be executed within the scope.
    """

    def __init__(self, name: str, actions: Actions | RawActions):
        super().__init__(name)
        self.type: str = "Scope"
        self.actions: Actions | RawActions = actions

    def export(self) -> Dict:
        """
        Exports the Scope statement as a dictionary.

        Returns:
            Dict: A dictionary representing the Scope statement.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["actions"] = self.actions.export()
        return d


class DoUntilStatement(BaseAction):
    """
    A class that defines a Do Until statement.

    Args:
        name (str): The name of the Do Until statement.
        actions (Actions): The actions to be executed within the Do Until loop.
        expression (str): The expression to be evaluated to determine when to stop the loop.
        limit_count (int, optional): The maximum number of iterations to perform. Defaults to 60.
    """

    def __init__(self, name: str, actions: Actions, expression: str, limit_count: int = 60):
        super().__init__(name)
        self.type: str = "Until"
        self.actions: Actions = actions
        self.limit = {
            "count": limit_count,
            "timeout": "PT1H"
        }
        self.expression = expression

    def export(self) -> Dict:
        """
        Exports the Do Until statement as a dictionary.

        Returns:
            Dict: A dictionary representing the Do Until statement.
        """
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["actions"] = self.actions.export()
        d["expression"] = self.expression
        d["limit"] = self.limit
        return d