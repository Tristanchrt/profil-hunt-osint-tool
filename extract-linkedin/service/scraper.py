from bs4 import BeautifulSoup
import time

class Scraper():

    def __init__(self, driver, url):
        self.driver = driver
        self.url_page = url
        self.driver.get(url)
        time.sleep(5)
        self.src = self.driver.page_source
        self.profile_url = self.driver.current_url

    def __set_url(self, url):
        self.url_page = url
        self.driver.get(url)
        self.src = self.driver.page_source
        time.sleep(10)
    
    def __get_name_from_relations(self, container):
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
    
    def __get_place_from_relations(self, container):
        try:
            location_loc = container.find('div', {'class': 'entity-result__secondary-subtitle t-14 t-normal'})
            return location_loc.get_text().strip()
        except AttributeError:
                return None

    def __get_job_from_relations(self, container):
        try:
            job_loc = container.find('div', {'class': 'entity-result__primary-subtitle t-14 t-black t-normal'})
            return job_loc.get_text().strip()
        except AttributeError:
            return None

    def __get_info_from_overlay_profile(self):
        self.__set_url(self.url_page + 'overlay/contact-info/')
        soup = BeautifulSoup(self.src, 'lxml')
        try:
            links_loc = soup.find('li', {'class' : "pv-contact-info__ci-container link t-14"})
            links_loc = links_loc.find('a')
            link = links_loc.get_text().strip()
        except AttributeError:
            link = None

        try:
            num_loc = soup.find('span', {'class': 't-14 t-black t-normal'})
            num = num_loc.get_text().strip()
        except AttributeError:
            num = None

        try:
            mail_loc = soup.find('div', {'class' : 'pv-contact-info__ci-container t-14'})
            mail_loc = mail_loc.find('a')
            mail = mail_loc.get_text().strip()
        except AttributeError:
            mail = None

        try:
            birthday_loc = soup.find('span', {'class': 'pv-contact-info__contact-item t-14 t-black t-normal'})
            birthday = birthday_loc.get_text().strip()
        except AttributeError:
            birthday = None
        
        return link, num, mail, birthday
    
    def get_profile_info(self):
        soup = BeautifulSoup(self.src, 'lxml')
        intro = soup.find('div', {'class': 'pv-text-details__left-panel'})

        name_loc = intro.find("h1")
        name = name_loc.get_text().strip()
        
        works_at_loc = intro.find("div", {'class': 'text-body-medium'})
        works_at = works_at_loc.get_text().strip()

        link, num, mail, birthday = self.__get_info_from_overlay_profile()
        
        profile = {'name': name,
                    'company': works_at,
                    'link': link,
                    'num': num,
                    'mail': mail,
                    'birthday': birthday}
        return profile        

    def get_relations(self, user_url):
        user_url = user_url.split('?')[0]
        self.__set_url(user_url)
        soup = BeautifulSoup(self.src, 'lxml')
        link = ''
        time.sleep(10)
        try:
            for a in soup.find_all('a', href=True):
                if '/search/results/people/?network' in a['href'] or '/search/results/people/?connectionOf' in a['href']:
                    link = a['href']
                    break
            if link == '':
                raise Exception
        except Exception:
            print('No relation link found')
            return None
        index_page = 1
        relations = {}
        while True:
            url = f'https://www.linkedin.com{link}&page={index_page}'
            self.__set_url(url)
            soup = BeautifulSoup(self.src, 'lxml')
            containers = soup.find_all('li', {'class': 'reusable-search__result-container'})
            check = 0
            for container in containers:
                names = self.__get_name_from_relations(container)
                if names != []:
                    location = self.__get_place_from_relations(container)
                    job = self.__get_job_from_relations(container)
                    data = {'names': names,
                            'location': location,
                            'job': job
                            }
                    relations.update(data)
                else:
                    check += 1
            if check == len(containers):
                break
            index_page += 1
        return relations

    def get_profile_education(self):
        educations = []
        self.__set_url(self.profile_url + 'details/education/')
        time.sleep(5)
        soup = BeautifulSoup(self.src, 'lxml')
        containers = soup.find_all('li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated'})
        
        for div in containers:
            tmp = {}
            school_name = div.find('div', 'display-flex align-items-center').get_text().strip()
            school_name = school_name[:len(school_name)//2]
            info_school = div.find('span', 't-14 t-normal').get_text().strip()
            info_school = info_school[:len(info_school)//2]
            date = div.find('span', 't-14 t-normal t-black--light').get_text().strip()
            date = date[:len(date)//2]
            date_start = None
            date_end = None
            if '-' in date:
                date = date.split('-')
                date_start = date[0]
                date_end = date[1]
                
            tmp = {'school': school_name,
                    'info': info_school,
                    'date_start': date_start,
                    'date_end': date_end}
            educations.append(tmp)
        return educations
            
    def get_profile_experience(self):
        experiences = []
        self.__set_url(self.profile_url + 'details/experience/')
        time.sleep(5)
        soup = BeautifulSoup(self.src, 'lxml')
        containers = soup.find_all(
            'li', {'class': 'pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated '})
        
        for div in containers:
            tmp = {}
            job_name = div.find('div', 'display-flex align-items-center').get_text().strip()
            job_name = job_name[:len(job_name)//2]
            
            company_name = div.find('span', 't-14 t-normal').get_text().strip()
            company_name = company_name[:len(company_name)//2]
            contract = None
            if '\u00b7' in company_name:
                company = company_name.split('\u00b7')
                company_name = company[0]
                contract = company[1]
            
            date_area__info = div.find_all('span', {'class': 't-14 t-normal t-black--light'})
            date_start = None
            date_end = None
            try:
                date_info = date_area__info[0].get_text().strip()
                date_info = date_info[:len(date_info)//2]
                if '\u00b7' in date_info:
                    info = date_info.split('\u00b7')
                    info = info[0].split('-')
                    date_start = info[0]
                    date_end = info[1]
            except:
                print('No date info')
                
            area_info = None
            try:            
                area_info = date_area__info[1].get_text().strip()
                area_info = area_info[:len(area_info)//2]
            except:
                print('No area info')
            
            tmp = {'job': job_name,
                   'company': company_name,
                   'contract': contract,
                   'date_start': date_start,
                   'date_end': date_end,
                   'area_info': area_info
            }
            experiences.append(tmp)
        return experiences
            
            
            