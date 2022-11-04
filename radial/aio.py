def _arequest_builder(method):
    def request(*args, **kwargs):
        def inner(func):
            async def replaced(self):
                res = await self._http._arequest(method, *args, **kwargs)
                return await func(self, res)

            return replaced

        return inner

    return request


get = _arequest_builder("GET")
options = _arequest_builder("OPTIONS")
head = _arequest_builder("HEAD")
post = _arequest_builder("POST")
put = _arequest_builder("PUT")
patch = _arequest_builder("PATCH")
delete = _arequest_builder("DELETE")
