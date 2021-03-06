from .AbstractAPI import AbstractAPI
from .errors import QPidError, TBidError
from .utils import handle_response
from .globals import PLACE_HOLDER


class RG(AbstractAPI):
    """
    The main API interface for the module
    
    Creates new RG object, raises ``AuthError`` if header is invalid

    :type header: dict
    :param header: Auth header obtained from rankguru

    """
    def __init__(self, header: dict):
        super().__init__(
            header,            
            nova = f'https://rest.rankguru.com/tests?textbook={PLACE_HOLDER}',
            graphql = 'https://api.rankguru.com/graphql'
        )

    def get_ans(self, QUESTION_PAPER_ID:str):
    
        """
        This function return a sorted dictionary of answers for the given Question Paper

        :param QUESTION_PAPER_ID: The Question Paper Id of the exam
        :type QUESTION_PAPER_ID: str

        :raises QPidError: If QPid is invalid
        :raises AuthError: If the header is invalid

        :return: Returns a sorted dictionary of question number - answer pairs
        :rtype: dict
        """
        
        r = self.get_ans_raw (QUESTION_PAPER_ID)['data']['QuestionEvaluation']

        if not r:
            raise QPidError
        r = r['evaluatedData']

        ret = {}

        for i in r:
            ret[int (i['questionNo'])] = " ".join ([chr (ord (i) + 48) for i in i['key']])

        keys = [*ret.keys()]
        keys.sort()

        return {i:ret[i] for i in keys}

    def get_ans_raw(self, QUESTION_PAPER_ID:str):
        """
        Returns raw json output from API retrieval

        :param QUESTION_PAPER_ID: The Question Paper Id of the exam
        :type QUESTION_PAPER_ID: str

        :raises AuthError: If the header is invalid
        
        :return: Raw json as python dict
        :rtype: dict
        """
        ANS_QUERY = '{ QuestionEvaluation(input: {questionPaperId: "'+QUESTION_PAPER_ID+'" }) \
                        { evaluatedData { questionNo  key }  } }'
        r = self.handler.make ("graphql", data={'query':ANS_QUERY})
        handle_response(r.status_code)
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

        r = self.handler.make ("nova", replace={PLACE_HOLDER:str(TEXT_BOOK_ID)},mode="get")
        handle_response(r.status_code)
        return r.json ()

    def get_tests(self, TEXT_BOOK_ID:str, latest_first = True):
        """
        This function return a sorted dictionary of tests for the given Textbook

        :param TEXT_BOOK_ID: The Textbook Id of the exam
        :type TEXT_BOOK_ID: str
        
        :param latest_first: Toggle it to get earlier tests first, defaults to True
        :type latest_first: bool, optional
        
        :raises TBidError: If TBid is invalid
        :raises AuthError: If the header is invalid

        :return: Returns a dictionary of test name - QPid pairs
        :rtype: dict
        """

        r = self.get_tests_raw (TEXT_BOOK_ID)

        if 'STATUS' in r.keys ():
            raise TBidError

        keys = [*r.keys ()]

        if latest_first:
            keys.reverse ()

        ret = {}
        for i in keys:
            test = r[i]

            ret[test['testName']] = test['questionPaperId']

        return ret
