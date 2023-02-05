from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import requests
import time
from selenium.webdriver.common.action_chains import ActionChains
from service.scraper import Scraper

class Crawler():

    def __init__(self, driver, scraper: Scraper):
        self.driver = driver
        self.scraper = scraper
        self.prefix = ""
        self.base_url = ""

    def search_targets(self, url_targets, neighboor):
        for i in range(neighboor):
            try:
                self.driver.get(url_targets)
                time.sleep(3)
                replies = self.driver.find_elements(
                    "xpath", "//a[@class='x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz xt0b8zv xzsf02u x1s688f']")

                action = ActionChains(self.driver)
                action.move_to_element(replies[i]).double_click().perform()

                # Find all the data

                if ".php" in self.driver.current_url:
                    self.prefix = "&sk="
                else:
                    self.prefix = "/" 
                self.base_url = self.driver.current_url

                # self.get_target_name()
                # self.get_target_pictures()
                # self.get_target_about_overview()
                # self.get_target_friends()

                self.get_complete_analysis()

                time.sleep(3)
            except Exception as e:
                print('Error search_targets =>', e)

    def get_target_friends(self, url=None):
        self.get_base_url()
        src_to_friends = self.driver.current_url + self.prefix + "friends"
        try:
            self.driver.get(src_to_friends)
            self.scroll_page(self.scraper.get_friends, self.driver)
        except Exception as e:
            print('Error get_target_friends => ', e)
            return None       

    def get_target_pictures(self, url=None):
        self.get_base_url()
        src_to_pictures = self.driver.current_url + self.prefix + "photos"
        try:
            self.driver.get(src_to_pictures)
            self.scraper.get_pictures(self.driver)
        except Exception as e:
            print('Error get_target_pictures => ', e)
            return None        

    def get_target_name(self, url=None):
        self.get_base_url()
        src_to_name = self.driver.current_url
        try:
            time.sleep(5)
            self.driver.get(src_to_name)
            time.sleep(5)
            self.scraper.get_name_info(self.driver)
        except Exception as e:
            print('Error get_target_name => ', e)
            return None             

    def get_target_about_overview(self, url=None):
        urls = [
            "about_overview",
            "about_work_and_education",
            "about_places",
            "about_contact_and_basic_info",
            "about_family_and_relationships",
            "about_life_events",
        ]
        try:
            self.get_base_url()
            for u in urls:
                url_to_go = self.base_url + self.prefix + u
                self.driver.get(url_to_go)
                time.sleep(5)
                self.scraper.get_about(self.driver, u)
        except Exception as e:
            print('Error get_target_about_overview => ', e)
            return None             

    def get_complete_analysis(self):
        self.get_target_friends()
        time.sleep(2)
        self.get_target_pictures()
        time.sleep(2)
        self.get_target_about_overview()
        time.sleep(2)
        self.get_target_name()
        
    def scroll_page(self, function, param):
        try:
            initialScroll = 0
            finalScroll = 1000
            for _ in range(20):
                self.driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
                initialScroll = finalScroll
                finalScroll += 1000
                time.sleep(2)
        except Exception as e:
            print('Error scrolling', e)
        function(param)

    
    def get_base_url(self):
        self.driver.get(self.base_url)
        time.sleep(2)
        
            