import requests
import json

with open('config/server.json', 'r') as f:
    cfg = json.load(f)
host = cfg['host']
name = cfg['name']

def alert(msg):
    res = requests.post(host + '/alert', data={
        'name': name,
         'message': msg
         })
    print(res)

if __name__ == "__main__":
    alert("something is not right")