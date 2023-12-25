from . import connectors
import re
import json

uuid4_pattern = r"-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}"


def truncate_string(input_str, max_length=20):
    if len(input_str) > max_length:
        return input_str[:max_length]
    else:
        return input_str


class Connections:
    """
    Manages information about APIs connected through PowerAutomate.
    This class is especially useful when creating new workflows with the CreateFlowAction.
    It expects connection strings to be added in the following formats:
    
    Example connection strings:
    - "shared-flowmanagemen-282bc0cf-2475-4655-8262-a6938ff6b179"
    - "ce9f7496f45f46649d94019c8f65693f"
    """

    def __init__(self):
        """
        Initializes the Connections class with an empty list of connections.
        """
        self.connections = []

    def set_connections_from_dict(self, data: dict) -> int:
        """
        Populates the connections list from a dictionary containing API connection data.
        
        Args:
            data (dict): A dictionary containing 'value' as a key, which is a list of
                         connection information dictionaries, each containing 'properties'
                         and 'apiId'.
        
        Returns:
            int: The number of connections added to the list.
        """
        self.connections = []
        if "value" not in data.keys():
            return 0
        user_id = ""
        for item in data["value"]:
            id = item["properties"]["apiId"]
            if "shared_flowmanagement" in id:
                user_id = item["properties"]["createdBy"]["id"]
                break

        for item in data["value"]:
            connection = {}
            connection["connectionName"] = item["name"]
            connection["id"] = item["properties"]["apiId"]
            creator_id = item["properties"]["createdBy"]["id"]
            properties = item.get("properties", {})
            if properties:
                statuses = properties.get("statuses", [])
                if statuses:
                    status = statuses[0].get("status", "Error")
                    if status == "Connected" and creator_id == user_id:
                        self.connections.append(connection)
        return len(self.connections)

    def set_connections_from_json_file(self, path: str) -> int:
        """
        Loads connection data from a JSON file and uses it to populate the connections list.
        
        Args:
            path (str): The file path to a JSON file containing connection data.
        
        Returns:
            int: The number of connections added to the list.
        """
        data = {}
        with open(path, "r") as f:
            data = json.load(f)
        return self.set_connections_from_dict(data)

    def add_connection(self, connection_name: str, id: str = None):
        """
        Adds a single connection to the list using the specified connection name and optional ID.
        
        Args:
            connection_name (str): The name of the connection.
            id (str, optional): The unique identifier for the API. If not provided,
                                the API name is used to look up the ID from a predefined list.
        
        Raises:
            ValueError: If the API name is not found and no ID is provided.
        """
        d = {}
        apiname = re.sub(uuid4_pattern, "", connection_name)
        apiname = truncate_string(apiname).replace("-", "_")

        d["connectionName"] = connection_name

        if not id:
            if apiname not in connectors.CONNECTORS:
                raise ValueError("API not found. Set id name to add_connection().")
            d["id"] = connectors.CONNECTORS[apiname]
        else:
            d["id"] = id

        self.connections.append(d)

    def export(self):
        """
        Exports the current list of connections.
        
        Returns:
            list: A list of dictionaries, each representing a connection.
        """
        return self.connections
