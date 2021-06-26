import aiohttp


seedrApiUrl = "https://www.seedr.cc/oauth_test/resource.php"
HEROKU_HEADERS = {"Accept": "application/json"; version=3.cedar-acm", "Content-Type": "application/json"}


class seedr(object):
    def __int__(self, username, password):
        self.username = username
        self.password = password

    def postData(self, url, params):
        async with aiohttp.ClientSession() as session:
            async with session.post(url, params=params, raise_for_status=True) as response:
                data = await response.json()
                return data["shortenedUrl"]

