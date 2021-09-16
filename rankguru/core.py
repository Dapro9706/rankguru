from .errors import *
from .utils import *
from .globals import PLAIN_PY_PROTOCOL, JSON_PROTOCOL, PLACE_HOLDER


class RG:
    def __init__(self, header: dict, protocol=PLAIN_PY_PROTOCOL):
        self.HEADER = header
        if not verify_header (self.HEADER):
            raise AuthError ()

        self.protocol = protocol
        self.NOVA_SERVICE_URL = f'https://rest.rankguru.com/'
        self.TESTS_URL = f'tests?textbook={PLACE_HOLDER}'

        self.API_URL = 'https://api.rankguru.com/graphql'
        self.ANS_QUERY = '{ QuestionEvaluation(input: {questionPaperId: "' + PLACE_HOLDER + '" })' \
                                                                                            ' { evaluatedData { questionNo  key }  } }'

    @handle_protocol
    def get_ans(self, QUESTION_PAPER_ID):
        r = self.get_ans_raw (QUESTION_PAPER_ID)
        if self.protocol == JSON_PROTOCOL:
            r = r['PAYLOAD']

        r = r['data']['QuestionEvaluation']

        if not r:
            raise QPidError
        r = r['evaluatedData']
        ret = {}
        for i in r:
            ret[int (i['questionNo'])] = " ".join ([chr (ord (i) + 48) for i in i['key']])
        return ret

    @handle_protocol
    def get_ans_raw(self, QUESTION_PAPER_ID):
        r = make_post_request (self.HEADER, self.API_URL, com (self.ANS_QUERY, QUESTION_PAPER_ID))

        if r.status_code == 401:
            raise AuthError
        else:
            return r.json ()

    @handle_protocol
    def get_tests_raw(self, TEXT_BOOK_ID):
        r = make_get_request (self.HEADER, self.NOVA_SERVICE_URL + com (self.TESTS_URL, TEXT_BOOK_ID))
        if r.status_code == 401:
            raise AuthError
        else:
            return r.json ()

    @handle_protocol
    def get_tests(self, TEXT_BOOK_ID):
        r = self.get_tests_raw (TEXT_BOOK_ID)

        if self.protocol == JSON_PROTOCOL:
            r = r['PAYLOAD']

        if 'STATUS' in r.keys ():
            raise TBidError

        keys = [i for i in [*r.keys ()]]
        keys.reverse ()

        ret = {}
        for i in keys:
            test = r[i]

            ret[test['testName']] = test['questionPaperId']

        return ret
