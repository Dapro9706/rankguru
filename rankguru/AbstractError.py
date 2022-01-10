
class AbstractError(Exception):
    def __init__(self, msg:str):
        super().__init__("Rankguru: "+msg)