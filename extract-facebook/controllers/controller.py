import os
import json
from config import Settings
import datetime
from service.driver import Driver
from service.crawler import Crawler
from service.scraper import Scraper
from copy import copy, deepcopy

class Controller():

    def __init__(self):
        self.driver = Driver(Settings().ACCOUNT_USERNAME,
                             Settings().ACCOUNT_PASSWORD)
        self.scraper = Scraper()
        self.crawler = Crawler(self.driver.get_driver(), self.scraper)

    def start_process(self, data_to_find):

        data_process = deepcopy(data_to_find)

        url_data = '%20'.join(data_process['params'])
        neighboor = 1

        url_search = "https://www.facebook.com/search/top?q="+url_data
        self.crawler.search_targets(url_search, neighboor)

        # self.write_file()
        
        print('DATA FROM SCRAPPING =>', self.scraper.get_data())
        data_process['data'] = self.scraper.get_data()
        return data_process

    def end_process(self):
        self.driver.close_driver()

    def write_file(self):
        filename = str(datetime.datetime.now()) + ".json"
        with open(filename, 'w') as outfile:
            json.dump(self.scraper.get_data(), outfile)

    def send_to_transform(self):
        pass


        