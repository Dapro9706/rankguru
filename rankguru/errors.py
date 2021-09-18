class AuthError (Exception):
    """
    Occurs when API header is invalid
    """
    def __init__(self):
        super ().__init__ ('The given Auth has expired or is invalid')

class QPidError (Exception):

    """
    Occurs when entered QPid is invalid
    """
    def __init__(self):
        super ().__init__ ('The given Question Paper ID is invalid')

class TBidError (Exception):

    """
    Occurs when entered TBid is invalid
    """
    def __init__(self):
        super ().__init__ ('The given Text Book ID is invalid')
