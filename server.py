host = 'http://192.168.0.12:8080'
name = 'Raspberry Pi'
import requests

def alert(msg):
    res = requests.post(host + '/alert', data={
        'name': name,
         'message': msg
         })
    print(res)

if __name__ == "__main__":
    alert("something is not right")