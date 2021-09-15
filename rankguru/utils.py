import requests
from .globals import PLACE_HOLDER


def make_get_request(header, url, query=None):
    if query:
        return requests.get (url, headers=header, json={'query': query})
    else:
        return requests.get (url, headers=header)


def make_post_request(header, url, query=None):
    if query:
        return requests.post (url, headers=header, json={'query': query})
    else:
        return requests.post (url, headers=header)


def verify_header(header):
    return make_get_request (header, 'https://rest.rankguru.com/tests?textbook=1').status_code != 401


def com(a: str, b):
    return a.replace (PLACE_HOLDER, str (b))
