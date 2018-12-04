import json

with open('location.json', 'r') as f:
    for eachname in f:
        print(eachname)

json.dump('location.json', 'w', indent=4)
