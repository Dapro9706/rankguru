import requests
from .globals import PLACE_HOLDER, JSON_PROTOCOL


def handle_protocol(func):
    def inner(self, *args, **kwargs):
        if self.protocol == JSON_PROTOCOL:
            try:
                r = func (self, *args, **kwargs)
                return {'STATUS': 'SUCESS', 'PAYLOAD': r}
            except Exception as e:
                return {
                    'STATUS': 'ERROR',
                    'ERROR': type (e).__name__,
                    'MESSAGE': str (e),
                    'LOCATION': func.__name__
                }
        else:
            return func (self, *args, **kwargs)

    return inner


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
