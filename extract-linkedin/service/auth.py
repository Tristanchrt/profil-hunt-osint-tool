from selenium import webdriver
import time
import socket
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Auth():

    def __init__(self, id, pwd):
        op = webdriver.ChromeOptions()

        # op.add_argument('--headless')
        # op.add_argument('--no-sandbox')
        # op.add_argument("--disable-setuid-sandbox")
        # op.add_argument('--disable-dev-shm-usage')

        op.add_argument("--no-sandbox")
        op.add_argument("--disable-notifications")

        """Local driver"""
        # self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=op)

        """Remote driver"""
        self.driver = webdriver.Remote(
            "http://selenium:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME, options=op)

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
        self.driver.get("https://linkedin.com/uas/login")
        time.sleep(5)
        
        username = self.driver.find_element("id", "username")
        username.send_keys(self.id) 
        
        pword = self.driver.find_element("id", "password")
        pword.send_keys(self.pwd)       
        
        self.driver.find_element("xpath", "//button[@type='submit']").click()

        time.sleep(10)
        if self.driver.current_url == 'https://www.linkedin.com/feed/':
            print('Authentication successed')
            return True
        else:
            print('Authentication failed')
            return False

    def close_driver(self):
        self.driver.close()
        self.driver.quit()

        