import json
from ..actions import BaseAction, Actions
from ..triggers import BaseTrigger, Triggers

DEFAULT_PARAMETER = {
    "$connections": {
        "defaultValue": {},
        "type": "Object"
    },
    "$authentication": {
        "defaultValue": {},
        "type": "SecureObject"
    }
}

DEFAULT_SCHEMA = "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#"
DEFAULT_VERSION = "1.0.0.0"


class Flow:
    """
    Manages a PowerAutomate Flow, including its components like triggers and actions.
    This class allows for configuring and manipulating the structure of a workflow.
    
    Attributes:
        schema (str): The default schema for the flow.
        contentVersion (str): The version of the content used in the flow.
        parameters (dict): Default parameters for the flow.
    """
    schema: str = DEFAULT_SCHEMA
    contentVersion: str = DEFAULT_VERSION
    parameters: dict = DEFAULT_PARAMETER

    def __init__(self):
        """
        Initializes the Flow with default triggers and actions.
        """
        self.triggers: BaseTrigger = Triggers()
        self.root_actions: Actions = Actions(True)

    def set_trigger(self, trigger: BaseTrigger):
        """
        Sets the main trigger for the flow.
        
        Args:
            trigger (BaseTrigger): An instance of BaseTrigger to be set as the flow's main trigger.
        """
        self.triggers.append(trigger)

    def append_action(self, action: BaseAction, prev_action: BaseAction = None, force_exec: bool = False, exec_if_failed: bool = False):
        """
        Appends an action to the flow, optionally specifying a previous action to link it after.
        
        Args:
            action (BaseAction): The action to append.
            prev_action (BaseAction, optional): The action after which the new action should be placed.
            force_exec (bool, optional): If True, the action will execute even if the previous action fails.
            exec_if_failed (bool, optional): If True, the action will execute only if the previous action fails.
        """
        if prev_action:
            self.root_actions.add_after(action, prev_action, force_exec, exec_if_failed)
        else:
            self.root_actions.append(action, force_exec, exec_if_failed)

    def add_top_action(self, action: BaseAction):
        """
        Adds an action at the top of the actions list.
        
        Args:
            action (BaseAction): The action to be added at the top of the action sequence.
        """
        self.root_actions.add_top(action)

    def export(self):
        """
        Exports the flow configuration as a dictionary.
        
        Returns:
            dict: A dictionary representing the complete flow configuration.
        """
        d = {}
        d["$schema"] = Flow.schema
        d["contentVersion"] = Flow.contentVersion
        d["parameters"] = Flow.parameters
        d["triggers"] = self.triggers.export()
        d["actions"] = self.root_actions.export()
        return d

    def export_json(self, xor_key=None):
        """
        Exports the flow configuration as a JSON string, optionally encoding it with an XOR key.
        
        Args:
            xor_key (str, optional): A comma-separated string of integers used as the key for XOR encryption.
        
        Returns:
            str: A JSON string representation of the flow, potentially XOR encrypted.
        """
        json_str = json.dumps(self.export())
        if xor_key:
            xor_key = [int(x) for x in xor_key.split(",")]
            json_str = ",".join(
                [str(ord(json_str[i]) ^ xor_key[i % len(xor_key)]) for i in range(len(json_str))])

        return json_str
