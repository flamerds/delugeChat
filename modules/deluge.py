import requests
from os import environ
import json
import asyncio
import base64

class deluge():
    def __init__(self):
        self.password = "whyNot"
        self.cookies = None
        self.requestId = 0
        self.ipAddress = 'http://192.168.1.253:8112/json'

        assert self.send_request('auth.login', [self.password]), 'Unable to log in. Check password.'

    def send_request(self,method, params=None):

        self.requestId += 1
        try:
            response = requests.post(
                self.ipAddress,
                json={'id': self.requestId, 'method': method, 'params': params or []},
                cookies=self.cookies)

        except requests.exceptions.ConnectionError:
            raise Exception('WebUI seems to be unavailable. Run deluge-web or enable WebUI plugin using other thin client.')

        data = response.json()

        error = data.get('error')

        if error:
            print(error)
            msg = error['message']

            if msg == 'Unknown method':
                msg += '. Check WebAPI is enabled.'

            raise Exception('API response: %s' % msg)

        self.cookies = response.cookies

        return data['result']

    async def send_request_async(self,method, params=None):

        self.requestId += 1
        try:
            response = requests.post(
                self.ipAddress,
                json={'id': self.requestId, 'method': method, 'params': params or []},
                cookies=self.cookies)

        except requests.exceptions.ConnectionError:
            raise Exception('WebUI seems to be unavailable. Run deluge-web or enable WebUI plugin using other thin client.')

        data = response.json()

        error = data.get('error')

        if error:
            print(error)
            msg = error['message']

            if msg == 'Unknown method':
                msg += '. Check WebAPI is enabled.'

            raise Exception('API response: %s' % msg)

        self.cookies = response.cookies

        return data['result']


    async def _add_magnet_torrent(self,torrent):
        version_number = await self.send_request_async('core.add_torrent_magnet', [torrent,{"add_paused":False,"remove_at_ratio":False}])

        print('WebAPI version: %s' % version_number)

    async def _add_torrent_file(self,torrent):
        data = base64.b64encode(open(torrent,'rb').read()).decode('utf-8')

        version_number = await self.send_request_async('core.add_torrent_file', [torrent,data,{"add_paused":False,"remove_at_ratio":False}])

        print('WebAPI version: %s' % version_number)

    async def send_torrents(self,filename):
        pass

        