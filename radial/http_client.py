from typing import Any, Mapping
from urllib.parse import urlencode
import requests


class Route:
    def __init__(self, base: str):
        self.base = base.rstrip("/")

    def create(self, *, endpoint: str, params: Mapping[Any, Any]):
        return f"{self.base}/{endpoint.lstrip('/')}?{urlencode(params)}"


class HTTP:
    def __init__(self, url: str, **config) -> None:
        self.route = Route(url)
        self.config = config

    def get(self, *args, **kwargs):
        return self._request("GET", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._request("POST", *args, **kwargs)

    def _request(self, method, endpoint, params={}, headers={}):
        gheaders = self.config.get("headers", {})
        res = requests.request(
            method,
            self.route.create(endpoint=endpoint, params=params),
            headers={**gheaders, **headers},
        )

        return res
