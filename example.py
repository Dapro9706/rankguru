from rankguru import RG, JSON_PROTOCOL
import json

with open ('header.json') as f:
    h = json.load (f)

API = RG (h)
print (API.get_tests ('1628253170787aef08c7516'))
