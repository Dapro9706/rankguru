class AuthError (Exception):
    def __init__(self):
        super ().__init__ ('The given Auth has expired or is invalid')

class QPidError (Exception):
    def __init__(self):
        super ().__init__ ('The given Question Paper ID is invalid')

class TBidError (Exception):
    def __init__(self):
        super ().__init__ ('The given Text Book ID is invalid')
