import json
from rankguru import UserAPI, RG
from rankguru.utils import get_header

with open('header.json') as f:
    h = json.load(f)
    API = UserAPI(h)
    API_ = RG(h)

print(API.get_data(678522)['studentName'])
print(API_.get_ans('481614e0-444d-11ec-a9e1-6f563121fe53'))

print(get_header(678522,1234))

