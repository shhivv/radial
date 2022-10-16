<br>
<h1 align="center">
💫 Radial
</h1>
<p align="center">
An intiutive interface for your requests in seconds
</p>

***

**Radial abstracts painful low-level request handling and presents a simple and intiutive interface to handle requests for your application.**

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
