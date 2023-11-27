import requests
import json
from pprint import pprint

word = input('What is your last name? ')
parameter = {"rel_rhy": str(word)}
datamuse = "https://api.datamuse.com/words"
rhyming = requests.get(datamuse, parameter)
info = json.loads(rhyming.text)
# pprint(info)ti    
for i in range(5):
    print(info[i]['word'])