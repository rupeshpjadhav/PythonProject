import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()


class APIClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL", "https://reqres.in/api/collections/products/records")
        self.project_id = os.getenv("PROJECT_ID", "50550")
        self.timeout = 10

        api_key = os.getenv("MY_API_KEY")
        if not api_key:
            raise ValueError("MY_API_KEY is missing - add it to .env")

        # A Session reuses the connection and sends these headers on every request
        self.session = requests.Session()
        self.session.headers.update({
            "x-api-key": api_key,
            "Accept": "application/json",
        })

    def _request(self, method, path="", **kwargs):
        url = f"{self.base_url}/{path}" if path else self.base_url
        params = kwargs.pop("params", {})
        params.setdefault("project_id", self.project_id)  # added to every call automatically

        resp = self.session.request(method, url, params=params, timeout=self.timeout, **kwargs)
        print(f"\n{method} {resp.url} -> {resp.status_code}")
        return resp

    def get(self, path="", **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path="", body=None, **kwargs):
        return self._request("POST", path, json=body, **kwargs)

    def put(self, path="", body=None, **kwargs):
        return self._request("PUT", path, json=body, **kwargs)

    def delete(self, path="", **kwargs):
        return self._request("DELETE", path, **kwargs)

    @staticmethod
    def print_json(resp):
        if resp.content:  # DELETE returns 204 with no body
            print(json.dumps(resp.json(), indent=4))
