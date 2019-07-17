import requests
from os import environ
import json

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