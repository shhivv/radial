<br>
<h1 align="center">
🚀 Radial
</h1>
<p align="center">
The next-gen HTTP client library for Python
</p>

***

<<<<<<< HEAD
**Radial abstracts painful low-levels request handling and presents a simple and intiutive interface to perform API requests in your application.**
=======
**Radial abstracts painful low-level request handling and presents a simple and intiutive interface to handle requests for your application.**
>>>>>>> 5f8d90e1887f6f81dabf4d56e14b8abf42c5cfda

## Installation

**Stable**
```
$ pip install radial
```

**Development**
```
$ pip install https://github.com/shhivv/radial.git@master
```
## Example
```py
@radial("https://dog.ceo/api")
class Dog:
    @get("/breeds/image/random")
    def random(self, response):
        return response.json()

dog = Dog()
random = dog.random()
print(random)
```

Currently work in progress
