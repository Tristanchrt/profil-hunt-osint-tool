from fastapi import Body
from time import sleep
from services.auth import AuthService
from log import logger
import time

async def is_search_paid(data = Body(...)):
    return True
    try:
        isPaid = False
        user_address = data['user_address']
        for _ in range(40):
            isPaid = await AuthService().is_paid(user_address)
            if isPaid['body']['isValide'] == True:
                return isPaid['body']
            time.sleep(2)
        raise isPaid['body']
    except Exception as e:
        print('Error from the middlware verification payment :', e)
        return False


