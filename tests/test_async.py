#pyright: reportPytestUnraisableExceptionWarning=false

from radial import radial, aio
import pytest #type: ignore 

pytest_plugins = ('pytest_asyncio',)

@radial("https://dog.ceo/api")
class Dog:
    @aio.get("/breeds/image/random")
    async def random(self, response):
        return await response.json()

    async def fetch_breed_random(self, breed):
        resp =  await self._http.aio_get(f"/breed/{breed}/images/random") #type: ignore
        return await resp.json()

@pytest.mark.asyncio
async def test_simple():
    dog = Dog()
    random = await dog.random()
    assert random["status"] == "success"

@pytest.mark.asyncio
async def test_manual():
    dog = Dog()
    hounds = await dog.fetch_breed_random("hound")
    assert hounds["status"] == "success"
