from typing import List, Dict
import uuid
import json
from os import makedirs, path, walk
import shutil
import zipfile
import tempfile
from random import randint
from datetime import datetime, timezone
from ..flow import Flow


def get_timestamp() -> str:
    """
    Generates a timestamp in ISO 8601 format appended with a random single digit, suitable for use in file naming or logging.
    
    Returns:
        str: The generated timestamp string in UTC.
    """
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%dT%H:%M:%S.%f") + str(randint(0, 9)) + "Z"


class Resource:
    """
    Manages a single resource defined in a manifest for PowerAutomate, encapsulating various properties including type,
    creation attributes, and dependencies among other resources.
    """

    def __init__(self, type: str, suggested_creation_type: str,
                 creation_type: str, configurable_by: str, hierarchy: str, display_name: str, icon_uri: str = None):
        """
        Initializes a new resource with specified attributes.
        
        Args:
            type (str): The type of the resource.
            suggested_creation_type (str): Suggested method for resource creation.
            creation_type (str): Specifies how the resource can be created.
            configurable_by (str): Indicates who can configure the resource.
            hierarchy (str): Hierarchical position of the resource relative to others.
            display_name (str): Display name of the resource.
            icon_uri (str, optional): URI to the resource's icon image.
        """
        self.uuid = uuid.uuid4().__str__()
        self.dependencies = []
        self.id = None
        self.name = None
        self.type = type
        self.suggested_creation_type = suggested_creation_type
        self.creation_type = creation_type
        self.configurable_by = configurable_by
        self.hierarchy = hierarchy
        self.display_name = display_name
        self.icon_uri = icon_uri

    def set_api_info(self, id: str, name: str):
        """
        Sets the API information for the resource.
        
        Args:
            id (str): The unique identifier of the API.
            name (str): The name of the API.
        """
        self.id = id
        self.name = name

    def set_dependencies(self, resources: List):
        """
        Sets dependencies of this resource to other resources.
        
        Args:
            resources (List[Resource]): A list of Resource instances that this resource depends on.
        """
        for resource in resources:
            self.dependencies.append(resource.uuid)
        self.dependencies = list(set(self.dependencies))

    def export(self) -> dict:
        """
        Exports the resource details as a dictionary suitable for serialization.
        
        Returns:
            dict: A dictionary containing all relevant details of the resource.
        """
        d = {}
        if self.id:
            d["id"] = self.id
        if self.name:
            d["name"] = self.name
        d["type"] = self.type
        d["suggestedCreationType"] = self.suggested_creation_type
        if self.creation_type:
            d["creationType"] = self.creation_type
        details = {}
        details["displayName"] = self.display_name
        if self.icon_uri:
            details["iconUri"] = self.icon_uri
        d["details"] = details
        d["configurableBy"] = self.configurable_by
        d["hierarchy"] = self.hierarchy
        d["dependsOn"] = self.dependencies
        return d

    def __eq__(self, __o: object) -> bool:
        """
        Compares this resource with another for equality based on UUID.
        
        Args:
            __o (object): The object to compare.
        
        Returns:
            bool: True if the objects are the same resource, False otherwise.
        """
        if isinstance(__o, Resource):
            return self.uuid == __o.uuid
        else:
            return False

    def __hash__(self):
        """
        Returns a hash based on the resource's UUID.
        
        Returns:
            int: The hash of the resource.
        """
        return hash(self.uuid)


class Package:
    """
    Manages the packaging of PowerAutomate flows into a deployable ZIP file format,
    encapsulating all necessary components like APIs, connections, and definitions.
    [Zip directory structure]
    .
    ├── Microsoft.Flow
    │   └── flows
    │       ├── {uuid}
    │       │   ├── apisMap.json
    │       │   ├── connectionsMap.json
    │       │   └── definition.json
    │       └── manifest.json
    └── manifest.json
    """

    def __init__(self, display_name: str, flow: Flow):
        """
        Initializes the package with a specific flow and a display name.

        Args:
            display_name (str): The name to display for the packaged flow.
            flow (Flow): The Flow object containing the workflow logic and configurations.
        """
        self.display_name = display_name
        self.__apis: List[Resource] = []
        self.__connections: List[Resource] = []
        self.__api_connection_map: Dict[Resource, Resource] = {}
        self.__exist_connections: dict = {}

        self.flow = flow
        self.__set_flow_resource()

    def __set_flow_resource(self):
        """
        Initializes the primary resource for the flow within the package.
        """
        self.__flow_resource = Resource(
            "Microsoft.Flow/flows", "New", "Existing, New, Update", "User", "Root", self.display_name)


    def set_flow_management_connector(self, connection_name: str = None):
        """
        Sets up a connector for the PowerAutomate Management API with optional connection naming.

        Args:
            connection_name (str, optional): The name to assign to the connection if it already exists.
        """
        # PowerAutomate Management APIの設定
        api = Resource("Microsoft.PowerApps/apis", "Existing", None, "System", "Child", "Flow Management",
                       "https://connectoricons-prod.azureedge.net/releases/v1.0.1650/1.0.1650.3374/flowmanagement/icon.png")
        api.set_api_info(
            "/providers/Microsoft.PowerApps/apis/shared_flowmanagement", "shared_flowmanagement")

        # PowerAutomate Management Connectionの設定
        connection = Resource("Microsoft.PowerApps/apis/connections", "Existing", "Existing", "User", "Child", "User",
                              "https://connectoricons-prod.azureedge.net/releases/v1.0.1644/1.0.1644.3342/flowmanagement/icon.png")

        # Connectionの依存APIの設定
        connection.set_dependencies([api])

        # 既存のconenction情報の設定
        if connection_name:
            self.__exist_connections["shared_flowmanagement"] = {
                "connectionName": connection_name,
                "source": "Invoker",
                "id": "/providers/Microsoft.PowerApps/apis/shared_flowmanagement",
                "tier": "NotSpecified"
            }
        self.__apis.append(api)
        self.__connections.append(connection)
        self.__api_connection_map[connection] = api

    def set_dropbox_connector(self, connection_name: str = None):
        """
        Sets up a connector for the Dropbox API with optional connection naming.

        Args:
            connection_name (str, optional): The name to assign to the connection if it already exists.
        """
        # Dropbox APIの設定
        api = Resource("Microsoft.PowerApps/apis", "Existing", None, "System", "Child", "Dropbox",
                       "https://connectoricons-prod.azureedge.net/releases/v1.0.1651/1.0.1651.3382/dropbox/icon.png")
        api.set_api_info(
            "/providers/Microsoft.PowerApps/apis/shared_dropbox", "shared_dropbox")

        # Dropbox Connectionの設定
        connection = Resource("Microsoft.PowerApps/apis/connections", "Existing", "Existing", "User", "Child",
                              "Dropbox", "https://connectoricons-prod.azureedge.net/releases/v1.0.1651/1.0.1651.3382/dropbox/icon.png")

        # Connectionの依存APIの設定
        connection.set_dependencies([api])

        # 既存のconenction情報の設定
        if connection_name:
            self.__exist_connections["shared_dropbox"] = {
                "connectionName": connection_name,
                "source": "Invoker",
                "id": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
                "tier": "NotSpecified"
            }
        self.__apis.append(api)
        self.__connections.append(connection)
        self.__api_connection_map[connection] = api

    def set_teams_connector(self, connection_name: str = None):
        """
        Sets up a connector for the Teams API with optional connection naming.

        Args:
            connection_name (str, optional): The name to assign to the connection if it already exists.
        """
        # Teams APIの設定
        api = Resource("Microsoft.PowerApps/apis", "Existing", None, "System", "Child", "Microsoft Teams",
                       "https://connectoricons-prod.azureedge.net/releases/v1.0.1657/1.0.1657.3443/teams/icon.png")
        api.set_api_info(
            "/providers/Microsoft.PowerApps/apis/shared_teams", "shared_teams")

        # Teams Connectionの設定
        connection = Resource("Microsoft.PowerApps/apis/connections", "Existing", "Existing", "User", "Child",
                              "Microsoft Teams", "https://connectoricons-prod.azureedge.net/releases/v1.0.1657/1.0.1657.3443/teams/icon.png")

        # Connectionの依存APIの設定
        connection.set_dependencies([api])

        # 既存のconenction情報の設定
        if connection_name:
            self.__exist_connections["shared_teams"] = {
                "connectionName": connection_name,
                "source": "Invoker",
                "id": "/providers/Microsoft.PowerApps/apis/shared_teams",
                "tier": "NotSpecified"
            }
        self.__apis.append(api)
        self.__connections.append(connection)
        self.__api_connection_map[connection] = api

    def set_sharepoint_connector(self, connection_name: str = None):
        """
        Sets up a connector for the Sharepoint API with optional connection naming.

        Args:
            connection_name (str, optional): The name to assign to the connection if it already exists.
        """
        # SharePoint APIの設定
        api = Resource("Microsoft.PowerApps/apis", "Existing", None, "System", "Child", "SharePoint",
                       "https://connectoricons-prod.azureedge.net/u/shgogna/globalperconnector-train1/1.0.1639.3312/sharepointonline/icon.png")
        api.set_api_info(
            "/providers/Microsoft.PowerApps/apis/shared_sharepointonline", "shared_sharepointonline")

        # SharePoint Connectionの設定
        connection = Resource("Microsoft.PowerApps/apis/connections", "Existing", "Existing", "User", "Child", "SharePoint",
                              "https://connectoricons-prod.azureedge.net/u/shgogna/globalperconnector-train1/1.0.1639.3312/sharepointonline/icon.png")

        # Connectionの依存APIの設定
        connection.set_dependencies([api])

        # 既存のconenction情報の設定
        if connection_name:
            self.__exist_connections["shared_sharepointonline"] = {
                "connectionName": connection_name,
                "source": "Invoker",
                "id": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
                "tier": "NotSpecified"
            }
        self.__apis.append(api)
        self.__connections.append(connection)
        self.__api_connection_map[connection] = api

    def set_outlook365_connector(self, connection_name: str = None):
        """
        Sets up a connector for the Outlook365 API with optional connection naming.

        Args:
            connection_name (str, optional): The name to assign to the connection if it already exists.
        """
        # Outlook 365 APIの設定
        api = Resource("Microsoft.PowerApps/apis", "Existing", None, "System", "Child", "Office 365 Outlook",
                       "https://connectoricons-prod.azureedge.net/u/laborbol/partial-builds/ase-v3/1.0.1653.3402/office365/icon.png")
        api.set_api_info(
            "/providers/Microsoft.PowerApps/apis/shared_office365", "shared_office365")

        # Outlook 365 Connectionの設定
        connection = Resource("Microsoft.PowerApps/apis/connections", "Existing", "Existing", "User", "Child", "Office 365 Outlook",
                              "https://connectoricons-prod.azureedge.net/u/laborbol/partial-builds/ase-v3/1.0.1653.3402/office365/icon.png")

        # Connectionの依存APIの設定
        connection.set_dependencies([api])

        # 既存のconenction情報の設定
        if connection_name:
            self.__exist_connections["shared_office365"] = {
                "connectionName": connection_name,
                "source": "Invoker",
                "id": "/providers/Microsoft.PowerApps/apis/shared_office365",
                "tier": "NotSpecified"
            }
        self.__apis.append(api)
        self.__connections.append(connection)
        self.__api_connection_map[connection] = api

    def export_solution_manifest(self) -> dict:
        """
        Generates the solution manifest file content for the package, detailing all included resources and metadata.

        Returns:
            dict: The manifest file content as a dictionary.
        """
        # update flow dependencies
        self.__flow_resource.set_dependencies(self.__apis)
        self.__flow_resource.set_dependencies(self.__connections)

        d = {}
        d["schema"] = "1.0"
        details = {}
        details["displayName"] = self.display_name
        details["description"] = ""
        details["createdTime"] = get_timestamp()
        details["packageTelemetryId"] = uuid.uuid4().__str__()
        details["creator"] = "N/A"
        details["sourceEnvironment"] = ""
        d["details"] = details

        resources = {}
        # Define flow resource
        resources[self.__flow_resource.uuid] = self.__flow_resource.export()
        # Define api resources
        for api in self.__apis:
            resources[api.uuid] = api.export()
        # Define connection resources
        for con in self.__connections:
            resources[con.uuid] = con.export()

        d["resources"] = resources
        return d

    def export_apis_map(self):
        d = {}
        for api in self.__apis:
            d[api.name] = api.uuid
        return d

    def export_connections_map(self):
        d = {}
        for connection in self.__connections:
            d[self.__api_connection_map[connection].name] = connection.uuid
        return d

    def export_package_manifest(self) -> dict:
        d = {}
        d["packageSchemaVersion"] = "1.0"
        d["flowAssets"] = {
            "assetPaths": [self.__flow_resource.uuid]
        }
        return d

    def export_definition(self):
        d = {}
        d["name"] = uuid.uuid4().__str__()
        d["id"] = "/providers/Microsoft.Flow/flows/" + d["name"]
        d["type"] = "Microsoft.Flow/flows"
        properties = {}
        properties["apiId"] = "/providers/Microsoft.PowerApps/apis/shared_logicflows"
        properties["displayName"] = self.display_name
        properties["definition"] = self.flow.export()
        properties["connectionReferences"] = self.__exist_connections
        properties["flowFailureAlertSubscribed"] = False
        properties["isManaged"] = False
        d["properties"] = properties
        return d

    def __write_json_file(self, path: str, content: dict):
        with open(path, 'w') as f:
            f.write(json.dumps(content))

    def export_zipfile(self, output_dir: str = ".") -> str:
        work_dir = tempfile.TemporaryDirectory().name
        definition_dir = path.join(
            work_dir, "Microsoft.Flow", "flows", self.__flow_resource.uuid)

        # ディレクトリ階層作成
        makedirs(definition_dir, exist_ok=True)

        # ./manifest.json
        self.__write_json_file(
            path.join(work_dir, "manifest.json"), self.export_solution_manifest())
        # ./Microsoft.Flow/flows/manifest.json
        self.__write_json_file(path.join(
            work_dir, "Microsoft.Flow", "flows", "manifest.json"), self.export_package_manifest())
        # ./Microsoft.Flow/flows/{uuid}/definition.json
        self.__write_json_file(
            path.join(definition_dir, "definition.json"), self.export_definition())
        # ./Microsoft.Flow/flows/{uuid}/apisMap.json
        self.__write_json_file(
            path.join(definition_dir, "apisMap.json"), self.export_apis_map())
        # ./Microsoft.Flow/flows/{uuid}/connectionsMap.json
        self.__write_json_file(path.join(
            definition_dir, "connectionsMap.json"), self.export_connections_map())

        # zipファイル作成
        filepath = path.join(output_dir, f"{self.display_name}.zip")
        zip_file = zipfile.ZipFile(filepath, "w", zipfile.ZIP_DEFLATED)
        for root, _, files in walk(work_dir):
            for file in files:
                zip_file.write(path.join(root, file), path.relpath(
                    path.join(root, file), work_dir))

        zip_file.comment = b'\xe2\xa0\x89\xe2\xa0\x97\xe2\xa0\x91\xe2\xa0\x81\xe2\xa0\x9e\xe2\xa0\x91\xe2\xa0\x99\xe2\xa0\x80\xe2\xa0\x83\xe2\xa0\xbd\xe2\xa0\x80\xe2\xa0\x9e\xe2\xa0\x91\xe2\xa0\x81\xe2\xa0\x8d\xe2\xa0\xa7'
        zip_file.close()

        # clean-up
        shutil.rmtree(work_dir)
        return path.abspath(filepath)
