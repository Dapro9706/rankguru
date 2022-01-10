from .AbstractError import AbstractError


class AuthError (AbstractError):
    """
    Occurs when API header is invalid
    """

    def __init__(self):
        super().__init__('The given Auth has expired or is invalid')


class QPidError (AbstractError):

    """
    Occurs when entered QPid is invalid
    """

    def __init__(self):
        super().__init__('The given Question Paper ID is invalid')


class TBidError (AbstractError):

    """
    Occurs when entered TBid is invalid
    """

    def __init__(self):
        super().__init__('The given Text Book ID is invalid')


class UserDoesNotExist (AbstractError):
    """
    Occurs when the user mentioned doesnt exist
    """

    def __init__(self):
        super().__init__("The User doesnt exist")


class IncorrectPassword (AbstractError):
    """
    Occurs when the given password is incorrect
    """

    def __init__(self):
        super().__init__("The given password is inccorect")
