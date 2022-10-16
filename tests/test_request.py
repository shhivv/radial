from radial import radial, get


@radial("https://dog.ceo/api")
class Dog:
    @get("/breeds/image/random")
    def random(self, response):
        return response.json()

    def fetch_breed(self, breed):
        return self._http.get(f"/breed/{breed}/images").json()


def test_simple():
    dog = Dog()
    random = dog.random()
    assert random["status"] == "success"


def test_manual():
    dog = Dog()
    hounds = dog.fetch_breed("hound")
    assert hounds["status"] == "success"
