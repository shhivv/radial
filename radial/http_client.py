from typing import Any, Mapping
from urllib.parse import urlencode
import httpx


class Route:
    def __init__(self, base: str):
        self.base = base.rstrip("/")

    def create(self, *, endpoint: str, params: Mapping[Any, Any]):
        return f"{self.base}/{endpoint.lstrip('/')}?{urlencode(params)}"


class HTTP:
    def __init__(self, url: str, **config) -> None:
        self.route = Route(url)
        self.config = config
        self.sync_client = None
        self.aio_client = None

    def get(self, *args, **kwargs):
        return self._request("GET", *args, **kwargs)

    def options(self, *args, **kwargs):
        return self._request("OPTIONS", *args, **kwargs)

    def head(self, *args, **kwargs):
        return self._request("HEAD", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._request("POST", *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._request("PUT", *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self._request("PATCH", *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._request("DELETE", *args, **kwargs)

    async def aio_get(self, *args, **kwargs):
        return await self._arequest("GET", *args, **kwargs)

    async def aio_options(self, *args, **kwargs):
        return await self._arequest("OPTIONS", *args, **kwargs)

    async def aio_head(self, *args, **kwargs):
        return await self._arequest("HEAD", *args, **kwargs)

    async def aio_post(self, *args, **kwargs):
        return await self._arequest("POST", *args, **kwargs)

    async def aio_put(self, *args, **kwargs):
        return await self._arequest("PUT", *args, **kwargs)

    async def aio_patch(self, *args, **kwargs):
        return await self._arequest("PATCH", *args, **kwargs)

    async def aio_delete(self, *args, **kwargs):
        return await self._arequest("DELETE", *args, **kwargs)

    def _request(self, method, endpoint, params={}, headers={}):
        gheaders = self.config.get("headers", {})

        if not self.sync_client:
            self.sync_client = httpx.Client()

        res = self.sync_client.request(
            method,
            self.route.create(endpoint=endpoint, params=params),
            headers={**gheaders, **headers},
        )

        return res

    async def _arequest(self, method, endpoint, params={}, headers={}):
        gheaders = self.config.get("headers", {})

        if not self.aio_client:
            self.aio_client = httpx.AsyncClient()

        async with self.aio_client as client:
            return await client.request(
                method,
                self.route.create(endpoint=endpoint, params=params),
                headers={**headers, **gheaders},
            )
