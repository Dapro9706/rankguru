from .request_handler import handler


class AbstractAPI:
    def __init__(self, header, **args):
        self.handler:handler  = handler(**args)
        self.handler.headers = header
