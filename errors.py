class AuthError (Exception):
    def __init__(self):
        super ().__init__ ('The given Auth has expired or is invalid')
