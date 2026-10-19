import json  # to pretty-print JSON responses
import os  # to read values from environment variables

import requests  # library that sends the HTTP requests
from dotenv import load_dotenv  # reads the .env file

# Load the .env file so os.getenv() can see MY_API_KEY, BASE_URL, etc.
load_dotenv()


class APIClient:
    """One place for everything needed to call the API: URL, headers and the HTTP methods."""

    def __init__(self):
        # __init__ runs automatically when you write APIClient() - it sets up the object.
        # "self" is the object being created; self.xxx stores a value on it for later use.

        # Base URL: taken from .env if BASE_URL is set, otherwise this default is used
        self.base_url = os.getenv("BASE_URL", "https://reqres.in/api/collections/products/records")
        # Project id sent as ?project_id=... on every request
        self.project_id = os.getenv("PROJECT_ID", "50550")
        # Seconds to wait for the server before giving up (prevents hanging forever)
        self.timeout = 10

        # Read the secret API key from .env
        api_key = os.getenv("MY_API_KEY")
        # Stop early with a clear message if the key is missing
        if not api_key:
            raise ValueError("MY_API_KEY is missing - add it to .env")

        # A Session reuses the connection and sends these headers on every request
        self.session = requests.Session()
        # Headers set here are added automatically to every get/post/put/delete call
        self.session.headers.update({
            "x-api-key": api_key,
            "Accept": "application/json",
        })

    def _request(self, method, path="", **kwargs):
        # The one method that actually sends requests; get/post/put/delete all call it.
        # The leading "_" means "internal helper" - tests should call get/post/put/delete instead.

        # Add the path to the base URL, e.g. ".../records/<id>"; with no path use the base URL as is
        url = f"{self.base_url}/{path}" if path else self.base_url

        # Take out any query params the caller passed (or start with an empty dict)
        params = kwargs.pop("params", {})
        # Add project_id unless the caller already gave one
        params.setdefault("project_id", self.project_id)  # added to every call automatically

        # Send the request; **kwargs passes along anything else, such as json=body
        resp = self.session.request(method, url, params=params, timeout=self.timeout, **kwargs)
        # Log the method, full URL and status code for every call
        print(f"\n{method} {resp.url} -> {resp.status_code}")
        # Return the response so the test can check status code and body
        return resp

    def get(self, path="", **kwargs):
        # GET: read data. api.get() = all records, api.get(record_id) = one record
        return self._request("GET", path, **kwargs)

    def post(self, path="", body=None, **kwargs):
        # POST: create a record. "body" is sent as JSON (json=body)
        return self._request("POST", path, json=body, **kwargs)

    def put(self, path="", body=None, **kwargs):
        # PUT: update the record at "path" (usually the record id) with "body"
        return self._request("PUT", path, json=body, **kwargs)

    def delete(self, path="", **kwargs):
        # DELETE: remove the record at "path" (the record id)
        return self._request("DELETE", path, **kwargs)

    @staticmethod
    def print_json(resp):
        # @staticmethod: doesn't need "self" because it only uses the response passed in
        if resp.content:  # DELETE returns 204 with no body
            # Print the JSON body with 4-space indentation
            print(json.dumps(resp.json(), indent=4))
