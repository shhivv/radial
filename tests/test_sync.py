from radial import radial, get


@radial("https://dog.ceo/api")
class Dog:
    @get("/breeds/image/random")
    def random(self, response):
        return response.json()

    def fetch_breed_random(self, breed):
        return self._http.get(f"/breed/{breed}/images/random").json()  # type: ignore


def test_simple():
    dog = Dog()
    random = dog.random()
    assert random["status"] == "success"


def test_manual():
    dog = Dog()
    hounds = dog.fetch_breed_random("hound")
    assert hounds["status"] == "success"
