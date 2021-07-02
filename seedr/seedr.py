import json
import aiohttp


class Seedr:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    async def postData(self, url, payload):
        headers = {'User-Agent': 'Mozilla/5.0'}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=payload) as response:
                return await response.json()

    async def requestData(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = (await response.text()).encode().decode()
                return json.loads(response)

    async def login(self):
        payload = {'grant_type': 'password', 'client_id': 'seedr_chrome', 'type': 'login', 'username': self.username, 'password': self.password}
        response = await self.postData('https://www.seedr.cc/oauth_test/token.php', payload)
        self.token = response['access_token']
        return self.token

    async def addMagnet(self, magnet):
        data = {'access_token': this.token, 'func': 'add_torrent', 'torrent_magnet': magnet}
        response = await self.postData(url, data)
        return response['data']

    async def getVideos(self):
        res = []
        data = await self.requestData(f"https://www.seedr.cc/api/folder?access_token={self.token}")
        for folder in data['data']['folders']:
            response = await self.requestData(f"https://www.seedr.cc/api/folder/{folder['id']}?access_token={self.token}")
            for video in response['data']['files']:
                print(video["play_video"])
                if video["play_video"]:
                    res.append({fid: folder['id'], id: video['folder_file_id'], name: video['name']})
        return res
