import pandas as pd
import os
import json
import re

import time
import random as rd

class FormatRevision():
    
    def __init__(self, data, topic_name):
        self.payload = data
        self.topic_name = topic_name
        self.emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
        
        with open(f'{os.getcwd()}/resource/world-cities.json') as f:
            self.world_cities = json.load(f)
        
    def run_revision(self):
        match self.topic_name:
            case 'LINKEDIN':
                return self.run_linkedin_revision()
            case 'INSTA':
                return self.run_insta_revision()
            case 'FACEBOOK':
                return self.run_facebook_revision()                    
            case _:
                print('Topic_name unknow:', self.topic_name)
                return None
        
    def run_linkedin_revision(self):
        profile_dict = {}
        education_dict = []
        experience_dict = []
        relations_dict = []
        
        df_profile = pd.json_normalize(self.payload['profile'])
        profile_dict.update({"name": df_profile['name'][0]})
        profile_dict.update({"company": df_profile['company'][0]})
        profile_dict.update({"link": df_profile['link'][0]})
        profile_dict.update({"num": df_profile['num'][0]})
        profile_dict.update({"mail": df_profile['mail'][0]})
        profile_dict.update({"birthday": df_profile['birthday'][0]})

        df_education = pd.json_normalize(self.payload['profile']['education'])
        # Translate french mouth name in english
        # df_education['date_start'] = pd.to_datetime(df_education['date_start'])
        # df_education['date_end'] = pd.to_datetime(df_education['date_end'])
        for _, school in df_education.iterrows():
            tmp = {}
            tmp.update({"school": school['school']})
            tmp.update({"info": school['info']})
            tmp.update({"date_start": school['date_start']})
            tmp.update({"date_end": school['date_end']})
            education_dict.append(tmp)
        
        df_experience = pd.json_normalize(self.payload['profile']['experience'])
        # Translate necessary french mouth name in english
        # df_experience['date_start'] = pd.to_datetime(df_experience['date_start'])
        # df_experience['date_end'] = pd.to_datetime(df_experience['date_end'])
        for _, job in df_experience.iterrows():
            tmp = {}
            tmp.update({"job": job['job']})
            tmp.update({"company": job['company']})
            tmp.update({"contract": job['contract']})
            tmp.update({"date_start": job['date_start']})
            tmp.update({"date_end": job['date_end']}) 
            location = job['area_info']
            if location != None:
                for word in re.split(', ', location):
                    for city_info in self.world_cities:
                        if word.lower() == city_info[0].lower():
                            tmp.update({"city": city_info[0]})    
                            tmp.update({"country": city_info[1]})
                            tmp.update({"state": city_info[2]})
            tmp.update({"area_info": job['area_info']})
            experience_dict.append(tmp)
        
        df_relations = pd.json_normalize(self.payload['profile']['relations'])
        for _, relation in df_relations.iterrows():
            tmp = {}
            tmp.update({"names": relation['names']})
            tmp.update({"job_description": self.emoji_pattern.sub(r'', relation['job'])})
            for city_info in self.world_cities:
                if relation['location'].lower() == city_info[0].lower():
                    tmp.update({"city": city_info[0]})    
                    tmp.update({"country": city_info[1]})
                    tmp.update({"state": city_info[2]})
            relations_dict.append(tmp)
        
        return {"profile": profile_dict, "education": education_dict, "experience": experience_dict, "relations": relations_dict}
            
    def run_insta_revision(self):
        profile_dict = {}
        relations_dict = []
        media_dict = []     
        
        pseudo = list(self.payload.keys())[0]
        profile_dict.update({"pseudo": pseudo})
        profile = self.payload[pseudo]
        
        # Description analyze
        description = (self.emoji_pattern.sub(r'', profile['description']))
        for word in re.split(' |\n', description):
            for city_info in self.world_cities:
                if word.lower() == city_info[0].lower():
                    profile_dict.update({"city": city_info[0]})    
                    profile_dict.update({"country": city_info[1]})
                    profile_dict.update({"state": city_info[2]})
                    break
                    
        # Followers analyze
        df_followers = pd.json_normalize(profile['followers'])
        df_followers.drop_duplicates(inplace=True)
        for _, follower in df_followers.iterrows():
            tmp = {}
            tmp.update({"username": follower['username']})
            tmp.update({"full_name": self.emoji_pattern.sub(r'', follower['full_name'])})
            tmp.update({"pic_url": follower['pic_url']})
            tmp.update({"insta_follower": True})
            tmp.update({"insta_following": False})
            if len(tmp) == 5:
                relations_dict.append(tmp)

        # Following analyze
        df_following = pd.json_normalize(profile['following'])
        df_following.drop_duplicates(inplace=True)
        for _, follower in df_following.iterrows():
            tmp = {}
            if follower['username'] not in [val.get('username') for val in relations_dict if val.get('username')]:
                tmp.update({"username": follower['username']})
                tmp.update({"full_name": self.emoji_pattern.sub(r'', follower['full_name'])})
                tmp.update({"pic_url": follower['pic_url']})
                tmp.update({"insta_follower": False})
            else:
                tmp = [val for val in relations_dict if val.get('username') == follower['username']][0]
            tmp.update({"insta_following": True})
            if len(tmp) == 5:
                relations_dict.append(tmp)

        df_medias = pd.json_normalize(profile['media'])
        df_medias.drop_duplicates(inplace=True)
        for _, media in df_medias.iterrows():
            tmp = {}
            if media['img_url'] not in [val.get('img_url') for val in media_dict if val.get('img_url')]:
                tmp.update({"img_url": media['img_url']})
                tmp.update({"caption_text": self.emoji_pattern.sub(r'', media['caption_text'])})
                tmp.update({"user_taged": media['user_taged']})
            media_dict.append(tmp)
                
        return {"profile": profile_dict, "relations": relations_dict, "medias": media_dict}
        
        
    def run_facebook_revision(self):
        profile_dict = {}
        relations_dict = []
        media_dict = []     
        
        # Profile
        profile_dict.update({"about_overview": self.payload['about_overview']})
        profile_dict.update({"about_work_and_education": self.payload['about_work_and_education']})
        profile_dict.update({"about_places": self.payload['about_places']})
        profile_dict.update({"about_contact_and_basic_info": self.payload['about_contact_and_basic_info']})
        profile_dict.update({"about_family_and_relationships": self.payload['about_family_and_relationships']})
        profile_dict.update({"about_life_events": self.payload['about_life_events']})
                    
        # Relations
        df_followers = pd.json_normalize(self.payload['friends'])
        df_followers.drop_duplicates(inplace=True)
        for _, follower in df_followers.iterrows():
            tmp = {}
            tmp.update({"name": follower['name']})
            tmp.update({"pic_url": follower['picture']})
            relations_dict.append(tmp)

        # Media
        id_media = 0
        for url_media in self.payload['pictures']:
            tmp = {}
            tmp.update({f"picture_{str(id_media)}": url_media})
            tmp.update({"pic_url": url_media})
            id_media += 1
            media_dict.append(tmp)
                
        return {"profile": profile_dict, "relations": relations_dict, "medias": media_dict}
        