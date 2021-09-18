from .errors import *
from .utils import *
from .globals import PLACE_HOLDER


class RG:
    """
    The main API interface for the module
    
    Creates new RG object, raises ``AuthError`` if header is invalid

    :type header: dict
    :param header: Auth header obtained from rankguru

    """
    def __init__(self, header: dict):
        self.HEADER = header
        if not verify_header (self.HEADER):
            raise AuthError ()

        self.NOVA_SERVICE_URL = f'https://rest.rankguru.com/'
        self.TESTS_URL = f'tests?textbook={PLACE_HOLDER}'

        self.API_URL = 'https://api.rankguru.com/graphql'
        self.ANS_QUERY = '{ QuestionEvaluation(input: {questionPaperId: "' + PLACE_HOLDER + '" })' \
                                                                                            ' { evaluatedData { questionNo  key }  } }'

    def get_ans(self, QUESTION_PAPER_ID:str):
    
        """
        This function return a sorted dictionary of answers for the given Question Paper

        :param QUESTION_PAPER_ID: The Question Paper Id of the exam
        :type QUESTION_PAPER_ID: str

        :raises QPidError: If QPid is invalid

        :return: Returns a sorted dictionary of question number - answer pairs
        :rtype: dict
        """
        
        r = self.get_ans_raw (QUESTION_PAPER_ID)['data']['QuestionEvaluation']

        if not r:
            raise QPidError
        r = r['evaluatedData']
        ret = {}

        keys = [*r.keys()]
        keys.sort()

        for i in keys:
            ret[int (i['questionNo'])] = " ".join ([chr (ord (i) + 48) for i in i['key']])
        return ret

    def get_ans_raw(self, QUESTION_PAPER_ID:str):
        """
        Returns raw json output from API retrieval

        :param QUESTION_PAPER_ID: The Question Paper Id of the exam
        :type QUESTION_PAPER_ID: str
        :raises AuthError: If the header is invalid
        :return: Raw json as python dict
        :rtype: dict
        """

        r = make_post_request (self.HEADER, self.API_URL, com (self.ANS_QUERY, QUESTION_PAPER_ID))

        if r.status_code == 401:
            raise AuthError
        else:
            return r.json ()

    def get_tests_raw(self, TEXT_BOOK_ID:str):
        """
        Returns raw json output from API retrieval

        :param TEXT_BOOK_ID: The Textbook Id of the category
        :type TEXT_BOOK_ID: str
        :raises AuthError: If the header is invalid
        :return: Raw json as python dict
        :rtype: dict
        """

        r = make_get_request (self.HEADER, self.NOVA_SERVICE_URL + com (self.TESTS_URL, TEXT_BOOK_ID))
        if r.status_code == 401:
            raise AuthError
        else:
            return r.json ()

    def get_tests(self, TEXT_BOOK_ID:str, latest_first = True):
        """
        This function return a sorted dictionary of tests for the given Textbook

        :param TEXT_BOOK_ID: The Textbook Id of the exam
        :type TEXT_BOOK_ID: str
        :param latest_first: Toggle if to get earlier tests first, defaults to True
        :type latest_first: bool, optional
        

        :raises TBidError: If TBid is invalid

        :return: Returns a dictionary of test name - QPid pairs
        :rtype: dict
        """

        r = self.get_tests_raw (TEXT_BOOK_ID)

        if 'STATUS' in r.keys ():
            raise TBidError

        keys = [i for i in [*r.keys ()]]
        keys.reverse ()

        ret = {}
        for i in keys:
            test = r[i]

            ret[test['testName']] = test['questionPaperId']

        return ret
