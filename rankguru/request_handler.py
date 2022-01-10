from requests import post, get
from .errors import AuthError


def verify_header(header):
    return get ('https://rest.rankguru.com/tests?textbook=1', headers=header).status_code != 401


class handler:
    def __init__(self, **args):
        self.headers = {}
        self.urls = args

    def set_header(self,header):
        self.headers = header
        if not verify_header (header):
            raise AuthError ()

    def make(self, url_key, data={}, params={}, replace={}, mode='post'):
        url = self.urls[url_key]
        for i in replace:
            url = url.replace(i, replace[i])

        return {
            'post': post,
            'get': get
        }[mode](url, headers=self.headers,
                data=data, params=params)
