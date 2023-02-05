import pandas as pd
import pprint


pp = pprint.PrettyPrinter(indent=2, compact=False)

class KeywordClassification():
    
    def __init__(self, data, topic_name):
        self.payload = data
        self.topic_name = topic_name
            
    def run_keyword_classification(self):
        match self.topic_name:
            case 'LINKEDIN':
                return self.run_linkedin_keyword_classification()
            case 'INSTA':
                return self.run_insta_keyword_classification()
            case 'FACEBOOK':
                return self.run_facebook_keyword_classification()                 
            case _:
                print('[Keyword Classification]Topic_name unknow:', self.topic_name)
                return None
                
    def run_linkedin_keyword_classification(self):
        return None
                
    def run_insta_keyword_classification(self):
        return None
        
    def run_facebook_keyword_classification(self):
        return None
