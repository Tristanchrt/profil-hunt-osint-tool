from instagrapi import Client
from config import Settings
from mail import *



def login(DOUBLE_FA_CODE=None):

    try:
        cl = Client()
        #--------------------Connection by user/pass -----------
        cl.login(
            Settings().ACCOUNT_USERNAME,
            Settings().ACCOUNT_PASSWORD,
        )
        #--------------------Connection by user/pass + 2fa-----------
        #cl.login(Settings().ACCOUNT_USERNAME, Settings().ACCOUNT_PASSWORD, VERIF_CODE)
        #--------------------Connection by session id------------
        # cl.login_by_sessionid("55660349985%3Aw5VpTAOIS0Fg6G%3A20%3AAYckNFRukN9qj6YEEXJqw_n5UyDkpSi0VXLD8o8sbQ")
        print("Auth sccess")
        return cl
    except ValueError:
        print("Auth fail :", ValueError)