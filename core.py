from .errors import AuthError
from .utils import *
from .globals import PLAIN_PY_PROTOCOL, JSON_PROTOCOL, PLACE_HOLDER


def hand(func):
    def inner(self, *args, **kwargs):
        if self.protocol == JSON_PROTOCOL:
            try:
                r = func (self, *args, **kwargs)
                return r
            except Exception as e:
                return {
                    'STATUS': 'ERROR',
                    'ERROR': type (e).__name__,
                    'MESSAGE': str (e),
                    'LOCATION': func.__name__
                }
        else:
            func (self, *args, **kwargs)

    return inner


class RG:
    def __init__(self, header: dict, protocol=PLAIN_PY_PROTOCOL):
        self.HEADER = header
        if not verify_header (self.HEADER):
            raise AuthError ()

        self.protocol = protocol
        self.NOVA_SERVICE_URL = f'https://rest.rankguru.com/tests?textbook={PLACE_HOLDER}'

        self.API_URL = 'https://api.rankguru.com/graphql'
        self.ANS_QUERY = '{ QuestionEvaluation(input: {questionPaperId: "' + PLACE_HOLDER + '" })' \
                                                       ' { evaluatedData { questionNo  key }  } }'

    @hand
    def get_ans(self, QUESTION_PAPER_ID):
        return make_post_request(self.HEADER,self.API_URL,com(self.ANS_QUERY,QUESTION_PAPER_ID))

