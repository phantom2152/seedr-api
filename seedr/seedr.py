import json
import aiohttp


class Seedr:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


    async def postData(self, url, payload):
        """ Helps to post data"""

        headers = {'User-Agent': 'Mozilla/5.0'}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, data=payload) as response:
                res = (await response.text()).encode().decode()
                data = json.loads(res)
                return data


    async def requestData(self, url):
        """ Helps in getting http data"""

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response = (await response.text()).encode().decode()
                return json.loads(response)


    async def login(self):
        """ Logging to seedr account and generating access token"""

        payload = {'grant_type': 'password', 'client_id': 'seedr_chrome', 'type': 'login', 'username': self.username.strip(), 'password': self.password.strip()}
        response = await self.postData('https://www.seedr.cc/oauth_test/token.php', payload)

        if 'error_description' in response:
            print(f"Error while logging into your account due to {response['error_description']}")
            return False, response['error_description']
        self.token = response['access_token']
        return True, self.token


    async getDeviceCode(self):
        """ Generates device code"""

        dc = await self.requestData("https://www.seedr.cc/api/device/code?client_id=seedr_xbmc");
        self.devc = dc.data["device_code"];
        self.usc = dc.data["user_code"];
        print(f'Paste this code into Seedr {self.usc} || And here is your token {self.devc}')
        return self.usc, self.devc


    async getToken(self, devc):
        """ Getting token from device code"""
        token = await self.requestData("https://www.seedr.cc/api/device/authorize?device_code=" + devc + "&client_id=seedr_xbmc")
        self.token = token.data["access_token"];
        return self.token


    async def addToken(self, token):
        self.token = token


    async def addMagnet(self, magnet):
        """Adds the magent link to seedr"""

        data = {'access_token': self.token, 'func': 'add_torrent', 'torrent_magnet': magnet}
        response = await self.postData(url, data)
        return response


    async def getVideos(self):
        """Sends you the all videos available in the seedr account from every folder"""

        res = []
        data = await self.requestData(f"https://www.seedr.cc/api/folder?access_token={self.token}")
        for folder in data['folders']:
            response = await self.requestData(f"https://www.seedr.cc/api/folder/{folder['id']}?access_token={self.token}")
            for video in response['files']:
                if video["play_video"]:
                    res.append({'fid': folder['id'], 'id': video['folder_file_id'], 'name': video['name']})
        return res


    async def getFilesById(self, id=None):
        """ Get the all files and folders in a particular
        folder by the folder id
        You will get the homepage files if you didn't give id"""

        url = f'https://www.seedr.cc/api/folder/{id}?access_token={self.token}' if id else f'https://www.seedr.cc/api/folder?access_token={self.token}'
        data = await self.requestData(url)
        parent = data['parent'] if data['parent'] != -1 else None
        response = {'parentId': parent, 'name': data['name'], 'folderSize': 0, 'totalStorage': data['space_max'], 'usedStorage': data['space_used'], 'type': data['type'], 'activeTorrents': data['torrents'], 'files': []}
        for folder in data['folders']:
            response['files'].append({
                'id': folder['id'],
                'type': 'folder',
                'name': folder['name'], 
                'size': folder['size']
            })
            try:
                response['folderSize'] += int(folder['size'])
            except:
                pass
        for file in data['files']:
            response['files'].append({
                'id': file['folder_file_id'],
                'type': 'file',
                'name': file['name'],
                'size': file['size']
            })
            try:
                response['folderSize'] += int(folder['size'])
            except:
                pass
        return response


    async def getFile(self, id):
        """ Sends the details of the file by the file id"""

        data = {'access_token': self.token, 'func': 'fetch_file', 'folder_file_id': id}
        response = await self.postData('https://www.seedr.cc/oauth_test/resource.php', data)
        return response


    async def rename(self, id, newName):
        """ Helps in renaming the files in seedr account"""

        data = {'access_token': self.token, 'func': 'rename', 'rename_to': newName, 'file_id': id}
        response = await self.postData('https://www.seedr.cc/oauth_test/resource.php', data)
        return response


    async def deleteFolder(self, id):
        """ used to delete folders in seedr by folder id"""

        data = {'access_token': self.token, 'func': 'delete', 'delete_arr': [{'type': 'folder', 'id': id}]}
        response = await self.postData('https://www.seedr.cc/oauth_test/resource.php', data)
        return response
