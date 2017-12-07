import requests
import json

output = json.load( open("crawling.json", "r") )
headers = {"Accept":"application/json", \
    "Content-Type":"application/json"}
data = json.dumps(output)

print("LOG: Sending crawling json to server")

r = requests.post("http://localhost:8080/document", \
    data=data, headers=headers)
print(r.text)
