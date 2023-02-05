from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys

import time

class Crawler():

    def __init__(self, driver, url):
        self.driver = driver
        self.url_page = url
        self.profile_url = url
        self.driver.get(url)
        self.src = self.driver.page_source

    def __set_url(self, url):
        self.url_page = url
        self.driver.get(url)
        self.src = self.driver.page_source
        time.sleep(10)

    def search_target(self, search_data):
        search_bar = self.driver.find_element("xpath",'//*[@id="global-nav-typeahead"]/input')
        for param in search_data:
            search_bar.send_keys(f'{param} ')

        search_bar.send_keys(Keys.ENTER)
        time.sleep(2)
        user_founds = []
        if self.driver.current_url != 'https://www.linkedin.com/feed/':
            self.__set_url(self.driver.current_url)
            soup = BeautifulSoup(self.src, 'lxml')
            for a in soup.find_all('a', href=True):
                if 'https://www.linkedin.com/search/results/people/?keyword' in a['href']:
                    user_founds = self.get_users_found(a['href'], search_data)
                    print(f'Found {len(user_founds)} users')
                    return user_founds
                elif f'https://www.linkedin.com/in/{search_data[0].lower()}-{search_data[1].lower()}' in a['href']:
                    user_founds.append(a['href'])
                    return user_founds
                elif f'https://www.linkedin.com/in/{search_data[1].lower()}-{search_data[0].lower()}' in a['href']:
                    user_founds.append(a['href'])
                    return user_founds
        else:
            print('No several users found')
            return None
    
    def get_users_found(self, url, search_data):
        self.__set_url(url)
        soup = BeautifulSoup(self.src, 'lxml')
        data = [search_data[0], search_data[1]]
        res = []
        for div in soup.find_all('div', 'entity-result__item'):
            names = self.__get_name_from_users(div)
            if names == data:
                for a in div.find_all('a', href=True):
                    url = f'https://www.linkedin.com/in/{search_data[0].lower()}-{search_data[1].lower()}'
                    print(url , a['href'])
                    if url in a['href']:
                        if a['href'] not in res:
                            res.append(a['href'])
        return res           
        
    def __get_name_from_users(self, container):
        name_loc = container.find('span', {'class': 'entity-result__title-text t-16'})
        name = name_loc.get_text().strip()
        prob_name = []
        for elt in name.split():
            for char in list(elt):
                if char.isupper():
                    elt = elt.replace('Voir', '')
                    prob_name.append(elt)

        names = list(set([i for i in prob_name if prob_name.count(i) >= 2]))
        return names



        
            