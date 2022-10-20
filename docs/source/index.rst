.. pyston documentation master file, created by
   sphinx-quickstart on Sun Oct  3 16:14:26 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Radial
=======
**The next-gen HTTP client library for Python**

Radial abstracts painful low-level request handling and presents a simple and intiutive interface to perform API requests in your application.

With **Radial**, old & ugly code that looked like this

.. code-block:: python3

    import request_library

    def fetch_image():
        res = request_library.get("https://example.com/image")
        if res.status == 200):
            return res["url"]
        raise Exception("Request did not return a 2xx")

becomes beautiful without compromising on any key feature

.. code-block:: python3

    import radial

    @radial("https://example.com")
    class Example:
        @get("/image", raise_on_error=True)
        def fetch_image(self, res):
            return res["url"]
 
Installation
--------------
**Stable** ::

    $ python -m pip install radial

**Development** ::

    $ python -m pip install https://github.com/shhivv/radial.git@master


Contents
----------

.. toctree::
   :maxdepth: 2

   reference
   