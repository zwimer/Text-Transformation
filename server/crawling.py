import requests
import json

output = json.load( open("crawling.json", "r") )
headers = {"Content-Type":"application/json"}
data = json.dumps(output)

r = requests.post("http://teamz.cs.rpi.edu:8080/document", \
    data=data, headers=headers)
print(r.status_code, r.text)
