from .globals import PLACE_HOLDER
from requests import post

def handle_response(code):
    if code in [200,201]:
        return
    else:
        raise {401: Exception,500:ValueError}[code]

def get_header(scs, password):
    r=post(url="https://accounts.rankguru.com/auth/local",data={"email":f"scs{scs}","rememberMe":False,"hostname":"rankguru.com",
                "password":f"{password}","forceLogin":True}).json()
    
    del r["firstTimePasswordChanged"], r["redirectionLink"]

    r["Authorization"]=r["token"]
    r["accesscontroltoken"]=r["accessControlToken"]

    del r["token"],r["accessControlToken"]
    return r

def edit_header(API, header):
    API.handler.header = header