import uuid
from typing import List, Dict
from .base import BaseAction


class GetAllTeamsAction(BaseAction):
    """
    An action to retrieve the list of teams that the user is a member of in Microsoft Teams.

    Args:
        name (str): The name of the action.

    Attributes:
        connection_host (dict): A dictionary containing the API information for the Teams connection.
        type (str): The type of the action, which is "OpenApiConnection".
        inputs (dict): A dictionary containing the input parameters for the action.
        parameters (dict): A dictionary containing the parameters for the action.

    Methods:
        export() -> Dict:
            Exports the action as a dictionary.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_teams",
        "connectionName": "shared_teams",
        "operationId": "GetAllTeams"
    }

    def __init__(self, name: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = GetAllTeamsAction.connection_host
        self.inputs["parameters"] = {}

    def export(self) -> Dict:
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class GetTeamAction(BaseAction):
    """
    An action to retrieve information about a specific team in Microsoft Teams.

    Args:
        name (str): The name of the action.
        team_id (str): The ID of the team to retrieve information for.

    Attributes:
        connection_host (dict): A dictionary containing the API information for the Teams connection.
        type (str): The type of the action, which is "OpenApiConnection".
        inputs (dict): A dictionary containing the input parameters for the action.
        parameters (dict): A dictionary containing the parameters for the action.

    Methods:
        export() -> Dict:
            Exports the action as a dictionary.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_teams",
        "connectionName": "shared_teams",
        "operationId": "GetTeam"
    }

    def __init__(self, name: str, team_id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = GetTeamAction.connection_host
        self.inputs["parameters"] = {
            "teamId": team_id
        }

    def export(self) -> Dict:
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class GetChannelsForGroupAction(BaseAction):
    """
    An action to retrieve the list of channels for a specific team in Microsoft Teams.

    Args:
        name (str): The name of the action.
        group_id (str): The ID of the team to retrieve the channels for.

    Attributes:
        connection_host (dict): A dictionary containing the API information for the Teams connection.
        type (str): The type of the action, which is "OpenApiConnection".
        inputs (dict): A dictionary containing the input parameters for the action.
        parameters (dict): A dictionary containing the parameters for the action.

    Methods:
        export() -> Dict:
            Exports the action as a dictionary.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_teams",
        "connectionName": "shared_teams",
        "operationId": "GetChannelsForGroup"
    }

    def __init__(self, name: str, group_id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = GetChannelsForGroupAction.connection_host
        self.inputs["parameters"] = {"groupId": group_id}

    def export(self) -> Dict:
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class GetMessagesFromChannelAction(BaseAction):
    """
    An action to retrieve the messages from a specific channel in Microsoft Teams.

    Args:
        name (str): The name of the action.
        group_id (str): The ID of the team that the channel belongs to.
        channel_id (str): The ID of the channel to retrieve messages from.

    Attributes:
        connection_host (dict): A dictionary containing the API information for the Teams connection.
        type (str): The type of the action, which is "OpenApiConnection".
        inputs (dict): A dictionary containing the input parameters for the action.
        parameters (dict): A dictionary containing the parameters for the action.

    Methods:
        export() -> Dict:
            Exports the action as a dictionary.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_teams",
        "connectionName": "shared_teams",
        "operationId": "GetMessagesFromChannel"
    }

    def __init__(self, name: str, group_id: str, channel_id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = GetMessagesFromChannelAction.connection_host
        self.inputs["parameters"] = {
            "groupId": group_id,
            "channelId": channel_id
        }

    def export(self) -> Dict:
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class GetChatsAction(BaseAction):
    """
    An action to retrieve the list of chats in Microsoft Teams.

    Args:
        name (str): The name of the action.
        chat_type (str, optional): The type of chats to retrieve, can be "all", "group", "meeting", or "oneOnOne". Defaults to "all".
        topic (str, optional): The topic of the chats to retrieve, can be "all". Defaults to "all".

    Attributes:
        connection_host (dict): A dictionary containing the API information for the Teams connection.
        type (str): The type of the action, which is "OpenApiConnection".
        inputs (dict): A dictionary containing the input parameters for the action.
        parameters (dict): A dictionary containing the parameters for the action.

    Methods:
        export() -> Dict:
            Exports the action as a dictionary.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_teams",
        "connectionName": "shared_teams",
        "operationId": "GetChats"
    }

    def __init__(self, name: str, chat_type: str = "all", topic: str = "all"):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = GetChatsAction.connection_host
        self.inputs["parameters"] = {
            "chatType": chat_type,
            "topic": topic
        }

    def export(self) -> Dict:
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d


class ListMembersAction(BaseAction):
    """
    An action to retrieve the list of members in a Microsoft Teams chat.

    Args:
        name (str): The name of the action.
        id (str): The ID of the chat to retrieve members for.
        thread_type (str, optional): The type of the chat, which is "groupchat". Defaults to "groupchat".

    Attributes:
        connection_host (dict): A dictionary containing the API information for the Teams connection.
        type (str): The type of the action, which is "OpenApiConnection".
        inputs (dict): A dictionary containing the input parameters for the action.
        parameters (dict): A dictionary containing the parameters for the action.

    Methods:
        export() -> Dict:
            Exports the action as a dictionary.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_teams",
        "connectionName": "shared_teams",
        "operationId": "ListMembers"
    }

    def __init__(self, name: str, id: str, thread_type: str = "groupchat"):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.inputs = {}
        self.parameters = {}
        self.inputs["host"] = ListMembersAction.connection_host
        self.inputs["parameters"] = {
            "threadType": thread_type,
            "body/recipient": id
        }

    def export(self) -> Dict:
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = self.inputs
        return d