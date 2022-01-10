from requests.api import head
from .AbstractAPI import AbstractAPI
from .utils import handle_response

class UserAPI(AbstractAPI):
    
    def __init__(self, header):
        super().__init__(
            header,
            data="https://api.rankguru.com/graphql"
        )


    def get_data_raw(self, scs):
        user_data_query = {"query":"{ StudentById(studentId: \"SCS|\") {\
            studentName, studentId,hierarchyLevels,orientation}\
            }".replace("|",str(scs))
        }

        r = self.handler.make(
            "data", data=user_data_query
        )
        print(r.status_code)
        handle_response(r.status_code)
        # TODO: proper exception

        return r

    def get_data(self, scs):
        data = self.get_data_raw(scs).json()['data']['StudentById']

        if not data:
            raise Exception
            # TODO: PROPER EXCEPTIONS

        del data['hierarchyLevels']['L_6']
        data['data'] = " ".join([*data['hierarchyLevels'].values()])
        del data['hierarchyLevels']
        return data