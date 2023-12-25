import json
from typing import List, Dict, Union
from copy import deepcopy
from .base import BaseAction, SkeltonNode
from .variable import InitVariableAction


class Actions:
    """
    A class that aggregates action nodes into a tree structure, corresponding to the 'Actions' field in a JSON schema.

    This class defines a tree structure with the following constraints:
    - The root node is always a SkeletonNode and is not included in exports.
    - All nodes, except for the root, must have exactly one parent node.
    - Nodes can have zero or more child nodes.

    Note:
    To manage variable initialization actions at the top of the chain in flows triggered by events, such actions are only allowed at the root level and must be executed in sequence before other actions.
    """

    def __init__(self, is_root: bool = False) -> None:
        self.root_node = SkeltonNode("root")
        self.last_update_node = self.root_node
        self.is_root_actions: bool = is_root
        self.nodes: Dict[str, BaseAction] = {"root": self.root_node}
        self.variable_init_nodes: List[BaseAction] = []

    def __validate_action(self, new_action: BaseAction, prev_action: BaseAction = None):
        """
        Validates a new action before adding it to the tree, ensuring it does not already exist, and checks parent-child constraints.

        Args:
            new_action (BaseAction): The action to be validated.
            prev_action (BaseAction): The previous action in the tree to which the new action would be linked.
        
        Raises:
            ValueError: If the action violates any constraints.
        """
        if new_action in self.nodes.values():
            raise ValueError(f"{new_action} already exists in Actions")
        if new_action.have_parent_node:
            raise ValueError(f"{new_action} already have a parent Actions.")
        if prev_action and prev_action not in self.nodes.values():
            raise ValueError(f"{prev_action} not in Actions")
        if not self.is_root_actions and isinstance(new_action, InitVariableAction):
            raise ValueError(f"{new_action} cannot be set into non-root Actions")

        original_name = new_action.action_name
        counter = 1
        while new_action.action_name in self.nodes:
            new_action.action_name = f"{original_name}_{counter}"
            counter += 1

    def add_top(self, new_action: BaseAction):
        """
        Adds a new action at the top of the tree under the root node.

        Args:
            new_action (BaseAction): The action to be added.
        """
        self.__validate_action(new_action)
        self.root_node.add_next_action(new_action)
        new_action.have_parent_node = True
        new_action.update_runafter(self.root_node)
        self.last_update_node = new_action
        self.nodes[new_action.action_name] = new_action

    def add_after(self, new_action: BaseAction, prev_action: BaseAction, force_exec: bool = False, exec_if_failed: bool = False):
        """
        Adds a new action immediately after a specified action in the tree.

        Args:
            new_action (BaseAction): The action to be added.
            prev_action (BaseAction): The action after which the new action should be added.
            force_exec (bool): If true, the new action will execute even if the previous action failed.
            exec_if_failed (bool): If true, the new action will execute only if the previous action failed.
        """
        self.__validate_action(new_action, prev_action)
        prev_action.add_next_action(new_action)
        new_action.have_parent_node = True
        new_action.update_runafter(prev_action, force_exec=force_exec, exec_if_failed=exec_if_failed)
        self.last_update_node = new_action
        self.nodes[new_action.action_name] = new_action

    def append(self, new_action: BaseAction, force_exec: bool = False, exec_if_failed: bool = False):
        """
        Appends a new action to the last updated node in the tree.

        Args:
            new_action (BaseAction): The action to be added.
            force_exec (bool): If true, the new action will execute regardless of the previous action's success.
            exec_if_failed (bool): If true, the new action will execute only if the previous action failed.
        """
        self.__validate_action(new_action)
        self.last_update_node.add_next_action(new_action)
        new_action.have_parent_node = True
        new_action.update_runafter(self.last_update_node, force_exec=force_exec, exec_if_failed=exec_if_failed)
        self.last_update_node = new_action
        self.nodes[new_action.action_name] = new_action

    def copy_nodes(self, original_node: BaseAction) -> BaseAction:
        """
        Recursively copies a node and all its children.

        Args:
            original_node (BaseAction): The root node from which the copy will begin.

        Returns:
            BaseAction: The root of the copied subtree.
        """
        new_node = original_node.clone()
        for child in original_node.next_nodes:
            new_child = self.copy_nodes(child)
            new_node.add_next_action(new_child)
        return new_node

    def __deepcopy__(self, memo) -> 'Actions':
        """
        Creates a deep copy of this Actions instance, including all nodes and their connections.

        Returns:
            Actions: A new Actions instance that is a deep copy of this instance.
        """
        new_root = self.copy_nodes(self.root_node)
        new_actions = Actions(self.is_root_actions)
        new_actions.root_node = new_root
        new_actions.nodes = {"root": new_root}
        stack = [(new_root, None)]
        while stack:
            child, parent = stack.pop()
            if parent:
                new_actions.add_after(child, parent)
            for next_node in child.next_nodes:
                stack.append((next_node, child))
        new_actions.last_update_node = new_actions.nodes[self.last_update_node.action_name]
        return new_actions

    def clone(self) -> 'Actions':
        """
        Creates a clone of this Actions instance using deep copy.

        Returns:
            Actions: A cloned instance of this Actions.
        """
        return deepcopy(self)

    def __add__(self, rhs_actions: Union['Actions', BaseAction]) -> 'Actions':
        """
        Supports the addition of another Actions instance or a BaseAction to this instance, combining their nodes appropriately.

        Args:
            rhs_actions (Union['Actions', BaseAction]): The right-hand side Actions instance or BaseAction to add.

        Returns:
            Actions: A new Actions instance resulting from the addition.

        Raises:
            TypeError: If the right-hand side is neither an Actions instance nor a BaseAction.
        """
        if isinstance(rhs_actions, Actions):
            new_actions = self.clone()
            new_actions.is_root_actions |= rhs_actions.is_root_actions
            stack = [(rhs_actions.root_node, None)]
            while stack:
                child, parent = stack.pop()
                new_child = child.clone()
                for next_node in child.next_nodes:
                    if isinstance(new_child, SkeltonNode):
                        stack.append((next_node, new_actions.last_update_node))
                    else:
                        stack.append((next_node, new_child))
                if not isinstance(new_child, SkeltonNode):
                    new_actions.add_after(new_child, parent)
            return new_actions
        elif isinstance(rhs_actions, BaseAction):
            new_actions = self.clone()
            new_actions.append(rhs_actions.clone())
            return new_actions
        raise TypeError("Both operand must be instance of the Actions class or BaseAction")

    def export(self) -> Dict:
        """
        Exports the Actions tree to a dictionary, excluding the root node.

        Returns:
            Dict: A dictionary representation of all actions except the root.
        """
        d = {}
        for node in self.nodes.values():
            if isinstance(node, SkeltonNode):
                continue
            d[node.action_name] = node.export()
        return d


class RawActions:
    """
    A class that behaves like the Actions class but takes exported data as input and re-validates it.

    Args:
        definition (Dict): A dictionary representation of actions.
    """

    def __init__(self, definition: Dict):
        self.definition: Dict = definition
    
    def validation(self) -> bool:
        """
        Validates the structure of the actions dictionary, ensuring each action has required properties and there are no duplicate names or unresolved dependencies.

        Returns:
            bool: True if the dictionary is valid, False otherwise.
        """
        if not self.definition:
            return False
        used_names = set()
        for action_name, node in self.definition.items():
            if action_name in used_names:
                return False
            used_names.add(action_name)
            if not isinstance(node, dict) or {"type", "inputs", "metadata"} - node.keys():
                return False
            if "runAfter" in node and any(name not in used_names for name in node["runAfter"]):
                return False
        return True

    def export(self) -> Dict:
        """
        Re-exports the actions dictionary if it passes validation, otherwise returns an empty dictionary.

        Returns:
            Dict: The validated actions dictionary, or an empty dictionary if validation fails.
        """
        return self.definition if self.validation() else {}
