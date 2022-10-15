import aiohttp


class BaseClient:
    def __init__(self, forward_url):
        self.forward_url = forward_url

    async def post(self, image_attached, image, prompt):
        raise NotImplementedError

    async def infer(self, json, **kwargs):
        raise NotImplementedError


class DefaultClient(BaseClient):
    async def post(self, json):
        async with aiohttp.ClientSession() as session:
            async with session.post(self.forward_url, json=json) as response:
                data = await response.json()
        return data

    async def infer(self, json, **kwargs):
        data = await self.post(json)
        return data
