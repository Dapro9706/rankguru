import json
from rankguru import RG


with open('header.json') as f:
    API = RG (json.load(f))
print (API.get_ans ('4bfd0110-318b-11ec-b7c7-2738e5f8eef2'))
