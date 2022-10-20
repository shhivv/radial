<br>
<h1 align="center">
🚀 Radial
</h1>

<div align="centeR">
<strong>The next-gen HTTP client library for Python</strong>

Radial abstracts painful low-level request handling and presents a simple and intiutive interface to perform API requests in your application.
</div>

***
<br>

With **Radial**, old & ugly code that looked like this
```py
import request_library

def fetch_image():
    res = request_library.get("https://example.com/image")
    if res.status == 200):
        return res["url"]
    raise Exception("Request did not return a 2xx")
``` 
becomes beautiful without compromising on any key feature
```py
import radial

@radial("https://example.com")
class Example:
    @get("/image", raise_on_error=True)
    def fetch_image(self, res):
        return res["url"] 
```
## Installation

**Stable**
```
$ python -m pip install radial 
```

**Development**
```
$ python -m pip install https://github.com/shhivv/radial.git@master
```

## [Documentation and API reference](https://radialhttp.readthedocs.io/en/latest/)