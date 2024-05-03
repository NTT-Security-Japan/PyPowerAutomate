from typing import Dict
from .base import BaseAction


class SharepointCopyFileAsyncAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "CopyFileAsync"
    }

    def __init__(self, name: str, dataset: str, sourceFileId: str, destinationDataset: str, destinationFolderPath: str, nameConflictBehavior: int):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.sourceFileId: str = sourceFileId
        self.destinationDataset: str = destinationDataset
        self.destinationFolderPath: str = destinationFolderPath
        self.nameConflictBehavior: int = nameConflictBehavior

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["parameters/sourceFileId"] = self.sourceFileId
        parameters["parameters/destinationDataset"] = self.destinationDataset
        parameters["parameters/destinationFolderPath"] = self.destinationFolderPath
        parameters["parameters/nameConflictBehavior"] = self.nameConflictBehavior

        inputs["host"] = SharepointCopyFileAsyncAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetFileItemAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetFileItem"
    }

    def __init__(self, name: str, dataset: str, table: str, id: int):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.table: str = table
        self.id: int = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["table"] = self.table
        parameters["id"] = self.id

        inputs["host"] = SharepointGetFileItemAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetItemChangesAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetItemChanges"
    }

    def __init__(self, name: str, dataset: str, table: str, id: int, since: str, includeDrafts: bool):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.table: str = table
        self.id: int = id
        self.since: str = since
        self.includeDrafts: bool = includeDrafts

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["table"] = self.table
        parameters["id"] = self.id
        parameters["since"] = self.since
        parameters["includeDrafts"] = self.includeDrafts

        inputs["host"] = SharepointGetItemChangesAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGrantAccessAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GrantAccess"
    }

    def __init__(self, name: str, dataset: str, table: str, id: int, recipients: str, roleValue: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.table: str = table
        self.id: int = id
        self.recipients: str = recipients
        self.roleValue: str = roleValue

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["table"] = self.table
        parameters["id"] = self.id
        parameters["parameter/recipients"] = self.recipients
        parameters["parameter/roleValue"] = self.roleValue

        inputs["host"] = SharepointGrantAccessAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointMoveFileAsyncAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "MoveFileAsync"
    }

    def __init__(self, name: str, dataset: str, sourceFileId: str, destinationDataset: str, destinationFolderPath: str, nameConflictBehavior: int):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.sourceFileId: str = sourceFileId
        self.destinationDataset: str = destinationDataset
        self.destinationFolderPath: str = destinationFolderPath
        self.nameConflictBehavior: int = nameConflictBehavior

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["parameters/sourceFileId"] = self.sourceFileId
        parameters["parameters/destinationDataset"] = self.destinationDataset
        parameters["parameters/destinationFolderPath"] = self.destinationFolderPath
        parameters["parameters/nameConflictBehavior"] = self.nameConflictBehavior

        inputs["host"] = SharepointMoveFileAsyncAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointCreateFileAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "CreateFile"
    }

    def __init__(self, name: str, dataset: str, folderPath: str, filename: str, body: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.folderPath: str = folderPath
        self.filename: str = filename
        self.body: str = body

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["folderPath"] = self.folderPath
        parameters["name"] = self.filename
        parameters["body"] = self.body

        inputs["host"] = SharepointCreateFileAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointCopyFolderAsyncAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "CopyFolderAsync"
    }

    def __init__(self, name: str, dataset: str, sourceFolderId: str, destinationDataset: str, destinationFolderPath: str, nameConflictBehavior: int):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.sourceFolderId: str = sourceFolderId
        self.destinationDataset: str = destinationDataset
        self.destinationFolderPath: str = destinationFolderPath
        self.nameConflictBehavior: int = nameConflictBehavior

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["parameters/sourceFolderId"] = self.sourceFolderId
        parameters["parameters/destinationDataset"] = self.destinationDataset
        parameters["parameters/destinationFolderPath"] = self.destinationFolderPath
        parameters["parameters/nameConflictBehavior"] = self.nameConflictBehavior

        inputs["host"] = SharepointCopyFolderAsyncAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointMoveFolderAsyncAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "MoveFolderAsync"
    }

    def __init__(self, name: str, dataset: str, sourceFolderId: str, destinationDataset: str, destinationFolderPath: str, nameConflictBehavior: int):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.sourceFolderId: str = sourceFolderId
        self.destinationDataset: str = destinationDataset
        self.destinationFolderPath: str = destinationFolderPath
        self.nameConflictBehavior: int = nameConflictBehavior

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["parameters/sourceFolderId"] = self.sourceFolderId
        parameters["parameters/destinationDataset"] = self.destinationDataset
        parameters["parameters/destinationFolderPath"] = self.destinationFolderPath
        parameters["parameters/nameConflictBehavior"] = self.nameConflictBehavior

        inputs["host"] = SharepointMoveFolderAsyncAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointListFolderAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "ListFolder"
    }

    def __init__(self, name: str, dataset: str, id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.id: str = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["id"] = self.id

        inputs["host"] = SharepointListFolderAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointCreateNewFolderAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "CreateNewFolder"
    }

    def __init__(self, name: str, dataset: str, table: str, path: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.table: str = table
        self.path: str = path

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["table"] = self.table
        parameters["parameters/path"] = self.path

        inputs["host"] = SharepointCreateNewFolderAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetFileContentByPathAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetFileContentByPath"
    }

    def __init__(self, name: str, dataset: str, path: str, inferContentType: bool):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.path: str = path
        self.inferContentType: bool = inferContentType

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["path"] = self.path
        parameters["inferContentType"] = self.inferContentType

        inputs["host"] = SharepointGetFileContentByPathAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetFileMetadataByPathAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetFileMetadataByPath"
    }

    def __init__(self, name: str, dataset: str, path: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.path: str = path

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["path"] = self.path

        inputs["host"] = SharepointGetFileMetadataByPathAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetFileContentAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetFileContent"
    }

    def __init__(self, name: str, dataset: str, id: str, inferContentType: bool):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.id: str = id
        self.inferContentType: bool = inferContentType

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["id"] = self.id
        parameters["inferContentType"] = self.inferContentType

        inputs["host"] = SharepointGetFileContentAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetFileMetadataAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetFileMetadata"
    }

    def __init__(self, name: str, dataset: str, id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.id: str = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["id"] = self.id

        inputs["host"] = SharepointGetFileMetadataAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointUpdateFileAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "UpdateFile"
    }

    def __init__(self, name: str, dataset: str, id: str, body: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.id: str = id
        self.body: str = body

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["id"] = self.id
        parameters["body"] = self.body

        inputs["host"] = SharepointUpdateFileAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointDeleteFileAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "DeleteFile"
    }

    def __init__(self, name: str, dataset: str, id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.id: str = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["id"] = self.id

        inputs["host"] = SharepointDeleteFileAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetFolderMetadataAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetFolderMetadata"
    }

    def __init__(self, name: str, dataset: str, id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.id: str = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["id"] = self.id

        inputs["host"] = SharepointGetFolderMetadataAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointGetTablesAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "GetTables"
    }

    def __init__(self, name: str, dataset: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset

        inputs["host"] = SharepointGetTablesAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointListRootFolderAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "ListRootFolder"
    }

    def __init__(self, name: str, dataset: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset

        inputs["host"] = SharepointListRootFolderAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointExtractFolderV2Action(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "ExtractFolderV2"
    }

    def __init__(self, name: str, dataset: str, source: str, destination: str, overwrite: bool):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset
        self.source: str = source
        self.destination: str = destination
        self.overwrite: bool = overwrite

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["dataset"] = self.dataset
        parameters["source"] = self.source
        parameters["destination"] = self.destination
        parameters["overwrite"] = self.overwrite

        inputs["host"] = SharepointExtractFolderV2Action.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d

METHODS = set(["GET", "PUT", "POST", "PATCH", "DELETE"])

class SharepointHTTPRequestAction(BaseAction):
    """
    Defines an action to send an HTTP request to Sharepoint. This is different to the other HTTP action as it does not require a premium license, but is only restricted to access Sharepoint sites.
    """

    connection_host = {
        "connectionName": "shared_sharepointonline",
        "operationId": "HttpRequest",
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline"
    }

    def __init__(self, name: str, dataset: str, method: str, uri: str, headers: dict = None, body: str = None):
        """
        Initializes a new Sharepoint HTTP Request with specified parameters.

        Args:
            name (str): The name of the action.
            dataset (str): The base URL of the Sharepoint site.
            method (str): The method of the HTTP request. Can be GET, PUT, POST, PATCH, or DELETE.
            uri (str): The second part of the URL.
            headers (dict, optional): The headers to be used with this HTTP request.
            body (str, optional): The body of the HTTP request.
        """
        
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.dataset: str = dataset

        if method not in METHODS:
            raise ValueError("Unsupported method type")

        self.method: str = method
        self.uri: str = uri
        self.headers: dict = headers
        self.body: str = body

    def export(self) -> Dict:
        """
        Exports the current state and configuration of the HTTP action in a dictionary format suitable for JSON serialization.

        Returns:
            Dict: A dictionary containing all the inputs and settings of the HTTP action.
        """

        inputs = {}
        parameters = {} 

        parameters["dataset"] = self.dataset
        parameters["parameters/method"] = self.method
        parameters["parameters/uri"] = self.uri
        if self.headers:
            parameters["parameters/headers"] = self.headers
        if self.body:
            parameters["parameters/body"] = self.body

        inputs["host"] = SharepointHTTPRequestAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d

class SharepointXxxxxxAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "xxxxxx"
    }

    def __init__(self, name: str, xxxxxx: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.xxxxxx: str = xxxxxx

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["xxxxxx"] = self.xxxxxx

        inputs["host"] = SharepointXxxxxxAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class SharepointXxxxxxAction(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_sharepointonline",
        "connectionName": "shared_sharepointonline",
        "operationId": "xxxxxx"
    }

    def __init__(self, name: str, xxxxxx: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

        self.xxxxxx: str = xxxxxx

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["xxxxxx"] = self.xxxxxx

        inputs["host"] = SharepointXxxxxxAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d
