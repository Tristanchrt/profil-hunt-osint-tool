from bs4 import BeautifulSoup
import time

class Scraper():

    def __init__(self):
        self.data = {
            'name_info': [],
            'friends': [],
            'pictures': [],
            "about_overview": [],
            "about_work_and_education": [],
            "about_places": [],
            "about_contact_and_basic_info": [],
            "about_family_and_relationships": [],
            "about_life_events": []
        }

    def soup_func(self, url):
        return BeautifulSoup(url, 'lxml')
    
    def get_friends(self, driver):
        soup = self.soup_func(driver.page_source)
        name = soup.find_all(
            'span', {'class': 'x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1tu3fi x3x7a5m x1lkfr7t x1lbecb7 x1s688f xzsf02u'})
        picture = soup.find_all(
            'img', {'class': 'x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 xl1xv1r'})
        for n, p in zip(name, picture):
            self.data['friends'].append({"name": n.get_text().strip(), "picture": p['src']})

    def get_pictures(self, driver):
        soup = self.soup_func(driver.page_source)
        containers = soup.find_all(
            'img', {'class': 'xzg4506 xycxndf xua58t2 x4xrfw5 x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 x5yr21d xl1xv1r xh8yej3'})
        for val in containers:
            self.data['pictures'].append(val['src'])

    def get_about(self, driver, category):
        soup = self.soup_func(driver.page_source)
        about = soup.find_all(
            'span', {'class': 'x193iq5w xeuugli x13faqbe x1vvkbs x10flsy6 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x4zkp8e x41vudc x6prxxf xvq8zen xo1l8bm xzsf02u'})
        for val in about:
            self.data[category].append(val.get_text())

    def get_name_info(self, driver):
        soup = self.soup_func(driver.page_source)
        name_info = soup.find_all(
            'h1', {'class': 'x1heor9g x1qlqyl8 x1pd3egz x1a2a7pz'})
        for val in name_info:
            self.data['name_info'].append(val.get_text())

    def get_data(self):
        return self.data
