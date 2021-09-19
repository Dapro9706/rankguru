import json
from rankguru import RG


with open('header.json') as f:
    API = RG (json.load(f))
print (API.get_ans ('0a302f30-12c5-11ec-9034-69a2bb5de394'))
