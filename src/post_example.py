import requests
import json
#r = requests.head('https://httpbin.org/get')
#headers = {'Content-Type': 'application/json'}
r = requests.post("http://10.0.0.19:8899", json={'sentences': '안녕하세요. 저는 python에서 호출합니다.'})

data = json.loads(r.text)
print(data)
