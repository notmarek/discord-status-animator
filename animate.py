import requests
from time import sleep
from config import token, status

headers = {
    'accept':'*/*',
    'authorization': token,
    'content-type':'application/json',
    'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.18 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
    'x-super-properties':'eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkRpc2NvcmQgQ2xpZW50IiwicmVsZWFzZV9jaGFubmVsIjoicHRiIiwiY2xpZW50X3ZlcnNpb24iOiIwLjAuMTgiLCJvc192ZXJzaW9uIjoiNS41LjctMS1NQU5KQVJPIiwib3NfYXJjaCI6Ing2NCIsIndpbmRvd19tYW5hZ2VyIjoiS0RFLHVua25vd24iLCJkaXN0cm8iOiJcIk1hbmphcm8gTGludXhcIiIsImNsaWVudF9idWlsZF9udW1iZXIiOjU1NzEyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=='
}
while True:
    for x in range(0, len(status)+1):
        data = {
            'custom_status': {'text': status[:x],
                              'emoji_name': '⭐'}
        }
        requests.patch('https://ptb.discordapp.com/api/v6/users/@me/settings', headers=headers, json=data)
        sleep(1)
