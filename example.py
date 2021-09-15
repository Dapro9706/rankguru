from rankguru import RG, JSON_PROTOCOL
from rankguru.utils import verify_header
import json

with open ('header.json') as f:
    h = json.load (f)

API = RG (h, JSON_PROTOCOL)
print (API.get_tests ('1628253170787aef08c7516'))
