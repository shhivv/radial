__title__ = "Radial"
__description__ = "An intiutive interface for your requests in seconds"
__version__ = "0.1.0"
__author__ = "Shiv"
__license__ = "MIT"

from .http_client import HTTP


def radial(url, **config):
    def inner(cls):
        class Wrapped(cls):
            def __init__(self, *args, **kwargs):
                cls.__init__(self, *args, **kwargs)
                self._http = HTTP(url, **config)

        return Wrapped

    return inner


def _request_builder(method):
    def request(*args, **kwargs):
        def inner(func):
            def replaced(self):
                res = self._http._request(method, *args, **kwargs)
                return func(self, res)

            return replaced

        return inner

    return request


get = _request_builder("get")
post = _request_builder("post")
