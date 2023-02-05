from models.search import *
from typing import List
import requests
from fastapi import HTTPException
from config.config import Settings
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class AuthService():

    @staticmethod
    async def is_paid(address: str):
        try:
            response = requests.get(Settings().SC_SERVICE + "/account/" +address)
            if response.status_code != 200:
                raise HTTPException(status_code=404, detail="Error payment verification" )
            else:
                return response.json()
        except Exception as e:  
            print("ERROR => auth service => is_paid : \n" + str(e))


