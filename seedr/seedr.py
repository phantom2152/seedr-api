import aiohttp
import asyncio

seedrApiUrl = "https://www.seedr.cc/oauth_test/resource.php"


async def postData(url, data):
    headers = {'User-Agent': 'Mozilla/5.0'}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, data=data) as response:
            data = await response.json()
            return data


class Seedr:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
    
    async def login(self):
        data = {'grant_type': 'password', 'client_id': 'seedr_chrome', 'type': 'login', 'username': self.username, 'password': self.password}
        response = await postData(seedrApiUrl, data)
        self.token = response['access_token']
        return self.token

    async def addMagnet(self, magnet):
        data = {'access_token': this.token, 'func': 'add_torrent', 'torrent_magnet': magnet}
        response = await postData(url, data)
        return response['data']

    async def getVideos():
        res = [];
        data = await postData(f"https://www.seedr.cc/api/folder?access_token={this.token}", None)
        print(data)
        """for folder in data.data.folders):
          res.push((await axios("https://www.seedr.cc/api/folder/" + folder.id + "?access_token=" + this.token)).data.files.filter(x => x["play_video"]).map(x => {
            return {
              fid: folder.id,
              id: x["folder_file_id"],
              name: x.name
            }"""

    #return res;
