# Offline file for parsing through JSON data

import json

with open('Sunglass_Hut.json') as file:
    file = file.read()

data = json.loads(file)

for item in data['plpView']['products']['products']['product']: 
    name = item['name']
    print(name)