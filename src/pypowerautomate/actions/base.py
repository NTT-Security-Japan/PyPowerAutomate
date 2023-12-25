from typing import List, Dict, Set, Union
import uuid
from copy import deepcopy


class State:
    """
    Enumerates possible states for the execution status of actions within a workflow.
    """
    Aborted = "Aborted"
    Cancelled = "Cancelled"
    Failed = "Failed"
    Faulted = "Faulted"
    Ignored = "Ignored"
    Paused = "Paused"
    Running = "Running"
    Skipped = "Skipped"
    Succeeded = "Succeeded"
    Suspended = "Suspended"
    TimedOut = "TimedOut"
    Waiting = "Waiting"


class BaseAction:
    """
    Defines a base class for creating action nodes in a workflow.

    Attributes:
        action_name (str): The name of the action.
        type (str): The type of the action, defined in derived classes.
        runafter (Dict): A dictionary defining conditions under which this action should run after another action.
        metadata (Dict): Metadata associated with the action.
        next_nodes (Set[BaseAction]): A set of actions that follow this action.
        have_parent_node (bool): Flag indicating whether this action is a child of another action.
    """

    def __init__(self, name: str):
        """
        Initializes the BaseAction with a specific name.

        Args:
            name (str): The name of the action.
        """
        self.action_name: str = name
        self.type: str = ""
        self.runafter: Dict = {}
        self.metadata: Dict = {}
        self.next_nodes: Set[BaseAction] = set()
        self.have_parent_node: bool = False
        self.metadata["operationMetadataId"] = uuid.uuid4().__str__()

    def __deepcopy__(self, memo) -> 'BaseAction':
        """
        Creates a deep copy of the current action, with a new UUID and reset link information.

        Args:
            memo (Dict): Memory map to manage deep copies and avoid circular references.

        Returns:
            BaseAction: A new instance of BaseAction.
        """
        cls = self.__class__
        new_instance = cls.__new__(cls)
        memo[id(self)] = new_instance
        for k, v in self.__dict__.items():
            setattr(new_instance, k, deepcopy(v, memo))
        new_instance.metadata["operationMetadataId"] = str(uuid.uuid4())
        new_instance.runafter = {}
        new_instance.next_nodes = set()
        new_instance.have_parent_node = False
        return new_instance

    def clone(self) -> 'BaseAction':
        """
        Clones the current action using deep copy.

        Returns:
            BaseAction: A clone of the current action.
        """
        return deepcopy(self)

    def add_next_action(self, node: 'BaseAction'):
        """
        Adds an action to the set of next actions.

        Args:
            node (BaseAction): The action to add as a next action.
        """
        self.next_nodes.add(node)

    def update_runafter(self, parent_node: 'BaseAction', force_exec: bool = False, exec_if_failed: bool = False):
        """
        Updates the run-after condition based on parent node and execution flags.

        Args:
            parent_node (BaseAction): The parent action node.
            force_exec (bool): If True, the action will execute regardless of the parent's state, except where prohibited.
            exec_if_failed (bool): If True, the action will execute if the parent action fails.
        """
        state_list = [State.Succeeded]
        if force_exec:
            state_list = [State.Succeeded, State.Failed, State.Skipped, State.TimedOut]
        elif exec_if_failed:
            state_list = [State.Failed]
        if isinstance(parent_node, SkeltonNode):
            self.runafter = {}
        else:
            self.runafter[parent_node.action_name] = state_list

    def export(self) -> Dict:
        """
        Exports the current action's configuration. This method should be implemented in derived classes.

        Raises:
            NotImplementedError: If the method is not implemented in a derived class.
        """
        raise NotImplementedError()

    def __add__(self, rhs_actions: Union['Actions', 'BaseAction']) -> 'Actions':
        """
        Supports addition of actions or combining actions into a more complex structure.

        Args:
            rhs_actions (Union['Actions', 'BaseAction']): The right-hand side actions or action to add.

        Returns:
            Actions: A new Actions instance representing the combination.
        """
        from .actions import Actions  # Lazy Import(to avoid circulare import)
        if isinstance(rhs_actions, Actions):
            new_actions = Actions(rhs_actions.is_root_actions)
            new_actions.append(self)
            stack = [(rhs_actions.root_node, None)]
            while stack:
                child, parent = stack.pop()
                new_child = child.clone()
                for next_node in child.next_nodes:
                    stack.append((next_node, new_child if not isinstance(new_child, SkeltonNode) else new_actions.last_update_node))
                if not isinstance(new_child, SkeltonNode):
                    new_actions.add_after(new_child, parent)
            return new_actions
        elif isinstance(rhs_actions, BaseAction):
            new_actions = Actions()
            new_actions.append(self.clone())
            new_actions.append(rhs_actions.clone())
            return new_actions

    def __repr__(self) -> str:
        """
        Provides a string representation of the action node.

        Returns:
            str: String representation of the action node.
        """
        return f"ActionNode:{self.action_name}({self.type})[id:{hex(id(self))}]"


class SkeltonNode(BaseAction):
    """
    A special class designed for use as the root node in the Actions class tree structure.
    Facilitates easier handling of the Actions tree structure.

    Attributes:
        Inherits all attributes from BaseAction.
    """

    def __init__(self, name: str):
        """
        Initializes the SkeltonNode with a specific name, primarily used as a root node.

        Args:
            name (str): The name of the skeleton node.
        """
        super().__init__(name)

    def export(self):
        """
        Exports the current skeleton node's configuration, always returns None for this node type.

        Returns:
            None
        """
        return None
