import aiohttp


seedrApiUrl = "https://www.seedr.cc/oauth_test/resource.php"
HEROKU_HEADERS = {"Accept": "application/vnd.heroku+json; version=3.cedar-acm", "Content-Type": "application/json"}

class seedr(object):
    def __int__(self, username, password):
        self.username = username
        self.password = password
        
