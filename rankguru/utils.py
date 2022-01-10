from .globals import PLACE_HOLDER

def handle_response(code):
    if code in [200,201]:
        return
    else:
        raise {401: Exception,500:ValueError}[code]