import requests
import json
from pprint import pprint
base_api = "http://api.open-notify.org/"
astronauts = base_api + "astros.json"
passover = base_api + "iss-pass.json"

people = requests.get(astronauts)
# print(people.text)
info = json.loads(people.text)
pprint(info)
print('Number of people in space: ', info['number'])
for v in info['people']:
    print(v['name'])