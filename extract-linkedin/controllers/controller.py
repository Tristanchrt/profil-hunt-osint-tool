import os
import time
import json

from config import Settings

from brokerstream import DtoBk
# from broker.broker import brokerStr

from service.auth import Auth
from service.crawler import Crawler
from service.scraper import Scraper

# def run_to_transform(job):
#     data_dto = DtoBk('None', ['fdfdfd'], ['fdfdfddffd'], {})
#     data = data_dto.get_dict()
#     brokerStr.send_message(data, 'LINKEDIN_TRANSFORM')

class Controller():

    def __init__(self, args):
        self.auth = Auth(Settings().ACCOUNT_USERNAME, Settings().ACCOUNT_PASSWORD)
        self.save_name = f'{Settings().ACCOUNT_USERNAME}_{int(time.time())}' if args.f == 'Y' else None
        
    def run_search(self, params):
        print('Starting process...')
        if self.auth.authentification:
            users_found = self.crawl_users(params)
            if users_found is not None:
                data = []
                for user_url in users_found:
                    res = self.scrape_info(user_url)
                    if res:
                        data.append(res)
                        if self.save_name is not None:
                            with open(f'{os.getcwd()}/output/{self.save_name}.json', 'w') as f:
                                json.dump(data, f)
                        return res
            else:
                print('No user url found')
                return None

    def crawl_users(self, search_data):
        crawler = Crawler(self.auth.driver, self.auth.driver.current_url)
        return crawler.search_target(search_data)

    def scrape_info(self, user_url):
        res = {}
        try:
            scraper = Scraper(self.auth.driver, user_url)
            tmp = {}
            tmp['profile'] = scraper.get_profile_info()
            tmp['profile']['education'] = scraper.get_profile_education()
            tmp['profile']['experience'] = scraper.get_profile_experience()
            tmp['profile']['relations'] = scraper.get_relations(user_url)
            res.update(tmp)
        except Exception as e:
            print('Scrapping has not been done.', e)
        return res

        
        