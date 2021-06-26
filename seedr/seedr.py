import aiohttp
import asyncio

seedrApiUrl = "https://www.seedr.cc/oauth_test/resource.php"


async def postData(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, data=data) as response:
            data = await response.json()
            return data


class Seedr:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        data = {
           'grant_type': 'password',
           'client_id': 'seedr_chrome',
           'action': 'login',
           'username': self.username,
           'password': self.password
        }
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(postData(seedrApiUrl, data))
        loop.close()
        print(response)
