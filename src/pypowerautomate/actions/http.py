from typing import Dict
from urllib.parse import urlparse
from .base import BaseAction

METHODS = set(["GET", "POST"])


class HttpAction(BaseAction):
    """
    Defines an action for making HTTP requests. This class allows setting various aspects of an HTTP request including headers, body, cookies, and queries.

    Attributes:
        METHODS (set): Valid HTTP methods for the action.
    """
    # Todo: Cookie handling
    # Todo: HTTP response handling

    def __init__(self, name: str, uri: str, method: str):
        """
        Initializes a new HttpAction with specified parameters.

        Args:
            name (str): The name of the action.
            uri (str): The URI to which the HTTP request will be sent.
            method (str): The HTTP method to be used for the request. Must be either 'GET' or 'POST'.

        Raises:
            ValueError: If the method is not supported (not in METHODS).
        """
        super().__init__(name)
        self.type = "Http"
        if method not in METHODS:
            raise ValueError("Unsupported method type")
        self.method: str = method
        self.uri: str = uri
        self.queries: Dict[str, str] = None
        self.body: str = None
        self.headers: Dict[str, str] = None
        self.cookie: str = None

    def set_body(self, body: str):
        """
        Sets the request body for the HTTP action.

        Args:
            body (str): The request body to be sent.
        """
        self.body = body

    def set_headers(self, headers: Dict[str, str]):
        """
        Sets the request headers for the HTTP action.

        Args:
            headers (Dict[str, str]): A dictionary of headers to be sent.
        """
        self.headers = headers

    def set_cookie(self, cookie: str):
        """
        Sets the cookie for the HTTP action.

        Args:
            cookie (str): The cookie string to be sent with the request.
        """
        self.cookie = cookie

    def set_queries(self, queries: Dict[str, str]):
        """
        Sets the URL query parameters for the HTTP action.

        Args:
            queries (Dict[str, str]): A dictionary of query parameters to be appended to the URI.
        """
        self.queries = queries

    def export(self) -> Dict:
        """
        Exports the current state and configuration of the HTTP action in a dictionary format suitable for JSON serialization.

        Returns:
            Dict: A dictionary containing all the inputs and settings of the HTTP action.
        """
        d = {}
        inputs = {}

        inputs["method"] = self.method
        inputs["uri"] = self.uri
        if self.body:
            inputs["body"] = self.body
        if self.headers:
            inputs["headers"] = self.headers
        if self.cookie:
            inputs["cookie"] = self.cookie
        if self.queries:
            inputs["queries"] = self.queries
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d
