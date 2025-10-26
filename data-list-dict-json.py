
items = input().split()
fruits = {
    "category": "fruits",
    "Country": items,
}

print(fruits)

print(type(fruits))

import json

json_data = json.dumps(fruits)
print(json_data)
print(type(json_data))

import requests

url = "__"
response = requests.post(url, json=fruits)