from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import socket
import sys


class Driver():

    def __init__(self, id, pwd):
        sys.setrecursionlimit(1000)
        op = webdriver.ChromeOptions()

        """"Params webdriver"""
        op.add_argument("--no-sandbox")
        op.add_argument("--disable-notifications")
        # op.add_argument('--no-sandbox')
        # op.add_argument('--window-size=1920,1080')
        # # op.add_argument('--headless')
        # op.add_argument('--disable-gpu')

        """Remote driver""" 
        self.driver = webdriver.Remote(
            "http://selenium:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME, options=op)

        """Local driver"""
        # self.driver = webdriver.Chrome('/usr/bin/chromedriver', options=op)

        self.id = str(id)
        self.pwd = str(pwd)
        
        self.authentification = self.authenticate() if self.check_internet() else False

    def check_internet(self):
        IPaddress = socket.gethostbyname(socket.gethostname())
        if IPaddress == "127.0.0.1":
            # print("No internet, your localhost is " + IPaddress)
            return False
        else:
            # print("Connected, with the IP address: " + IPaddress)
            return True
        
    def authenticate(self):
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/login")
        time.sleep(5)
        self.driver.find_element(
             "xpath", "//button[@data-testid='cookie-policy-manage-dialog-accept-button']").click()
        time.sleep(3)
        username = self.driver.find_element("id", "email")
        username.send_keys(self.id) 
    
        pword = self.driver.find_element("id", "pass")
        pword.send_keys(self.pwd)       
        time.sleep(5)
        self.driver.find_element("xpath", "//button[@id='loginbutton']").click()

        time.sleep(10)
    
    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.close()
        self.driver.quit()
