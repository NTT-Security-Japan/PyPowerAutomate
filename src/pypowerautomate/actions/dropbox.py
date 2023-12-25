from typing import Dict
from .base import BaseAction


class DropboxCreateFileAction(BaseAction):
    """
    Defines an Action to create a new file in Dropbox.

    Args:
        name (str): The name of the action.
        folderPath (str): The path of the folder to create the file in.
        filename (str): The name of the file to create.
        body (str): The content to be written to the file.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "CreateFile"
    }

    def __init__(self, name: str, folderPath: str, filename: str, body: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.folderPath: str = folderPath
        self.filename: str = filename
        self.body: str = body

    def export(self) -> Dict:
        inputs = {}
        parameters = {}
        parameters["folderPath"] = self.folderPath
        parameters["name"] = self.filename
        parameters["body"] = self.body
        inputs["host"] = DropboxCreateFileAction.connection_host
        inputs["parameters"] = parameters
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs
        return d

class DropboxGetFileContentAction(BaseAction):
    """
    Defines an Action to retrieve the content of a file in Dropbox.

    Args:
        name (str): The name of the action.
        id (str): The ID of the file to retrieve.
        inferContentType (bool): Whether to infer the content type of the file. Defaults to True.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "GetFileContent"
    }

    def __init__(self, name: str, id: str, inferContentType: bool = True):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.id: str = id
        self.inferContentType: str = str(inferContentType)

    def export(self) -> Dict:
        inputs = {}
        parameters = {}
        parameters["id"] = self.id
        parameters["inferContentType"] = self.inferContentType
        inputs["host"] = DropboxGetFileContentAction.connection_host
        inputs["parameters"] = parameters
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs
        return d

class DropboxUpdateFileAction(BaseAction):
    """
    Defines an Action to update the content of a file in Dropbox.

    Args:
        name (str): The name of the action.
        id (str): The ID of the file to update.
        body (str): The new content to be written to the file.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "UpdateFile"
    }

    def __init__(self, name: str, id: str, body: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.id: str = id
        self.body: str = body

    def export(self) -> Dict:
        inputs = {}
        parameters = {}
        parameters["id"] = self.id
        parameters["body"] = self.body
        inputs["host"] = DropboxUpdateFileAction.connection_host
        inputs["parameters"] = parameters
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs
        return d

class DropboxListFilesInFolderAction(BaseAction):
    """
    Defines an Action to list the files in a Dropbox folder.

    Args:
        name (str): The name of the action.
        id (str): The ID of the folder to list files in.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "ListFolder"
    }

    def __init__(self, name: str, id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.id: str = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}
        parameters["id"] = self.id
        inputs["host"] = DropboxListFilesInFolderAction.connection_host
        inputs["parameters"] = parameters
        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs
        return d


class DropboxListFilesInRootFolderAction(BaseAction):
    """
    Defines an Action to list the files in the Dropbox root folder.

    Args:
        name (str): The name of the action.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "ListRootFolder"
    }

    def __init__(self, name: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        inputs["host"] = DropboxListFilesInRootFolderAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class DropboxCopyFileAction(BaseAction):
    """
    Defines an Action to copy a file in Dropbox.

    Args:
        name (str): The name of the action.
        source (str): The path of the source file to copy.
        destination (str): The path of the destination for the copied file.
        overwrite (bool): Whether to overwrite the destination file if it already exists. Defaults to False.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "CopyFile"
    }

    def __init__(self, name: str, source: str, destination: str, overwrite: bool = False):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.source: str = source
        self.destination: str = destination
        self.overwrite: str = str(overwrite)

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["source"] = self.source
        parameters["destination"] = self.destination
        parameters["overwrite"] = self.overwrite

        inputs["host"] = DropboxCopyFileAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class DropboxDeleteFileAction(BaseAction):
    """
    Defines an Action to delete a file in Dropbox.

    Args:
        name (str): The name of the action.
        id (str): The ID of the file to delete.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "DeleteFile"
    }

    def __init__(self, name: str, id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.id: str = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["id"] = self.id

        inputs["host"] = DropboxDeleteFileAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class DropboxGetFileMetadataAction(BaseAction):
    """
    Defines an Action to retrieve the metadata of a file in Dropbox.

    Args:
        name (str): The name of the action.
        id (str): The ID of the file to retrieve metadata for.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "GetFileMetadata"
    }

    def __init__(self, name: str, id: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.id: str = id

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["id"] = self.id

        inputs["host"] = DropboxGetFileMetadataAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class DropboxExtractArchiveToFolderAction(BaseAction):
    """
    Defines an Action to extract the contents of an archive file to a folder in Dropbox.

    Args:
        name (str): The name of the action.
        source (str): The path of the archive file to extract.
        destination (str): The path of the folder to extract the contents to.
        overwrite (bool): Whether to overwrite existing files in the destination folder. Defaults to False.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "ExtractFolderV2"
    }

    def __init__(self, name: str, source: str, destination: str, overwrite: bool = False):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.source: str = source
        self.destination: str = destination
        self.overwrite: str = str(overwrite)

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["source"] = self.source
        parameters["destination"] = self.destination
        parameters["overwrite"] = self.overwrite

        inputs["host"] = DropboxExtractArchiveToFolderAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class DropboxGetFileContentUsingPathAction(BaseAction):
    """
    Defines an Action to retrieve the content of a file in Dropbox using the file path.

    Args:
        name (str): The name of the action.
        path (str): The path of the file to retrieve the content for.
        inferContentType (bool): Whether to infer the content type of the file. Defaults to True.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "GetFileContentByPath"
    }

    def __init__(self, name: str, path: str, inferContentType: bool = True):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.path: str = path
        self.inferContentType: str = str(inferContentType)

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["path"] = self.path
        parameters["inferContentType"] = self.inferContentType

        inputs["host"] = DropboxGetFileContentUsingPathAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class DropboxGetFileMetadataUsingPathAction(BaseAction):
    """
    Defines an Action to retrieve the metadata of a file in Dropbox using the file path.

    Args:
        name (str): The name of the action.
        path (str): The path of the file to retrieve the metadata for.
    """

    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_dropbox",
        "connectionName": "shared_dropbox",
        "operationId": "GetFileMetadataByPath"
    }

    def __init__(self, name: str, path: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.path: str = path

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["path"] = self.path

        inputs["host"] = DropboxGetFileMetadataUsingPathAction.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d