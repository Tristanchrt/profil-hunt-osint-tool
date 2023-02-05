from common.basic.format_revision import FormatRevision
from common.basic.identification import Identification
from common.basic.keyword_classification import KeywordClassification


class Basic:
    
    def __init__(self, topic_name):
        self.topic_name = topic_name
    
    def run_format_revision(self, data):
        try:
            format_revision = FormatRevision(data, self.topic_name)
            return format_revision.run_revision()
        except Exception:
            print(f'[{self.topic_name}]Format Revision failed')
            return data
            
    def run_identification(self, data):
        try:
            identification = Identification(data, self.topic_name)
            return identification.run_identification()
        except Exception:
            print(f'[{self.topic_name}]Identification failed')
            return data
            
    def run_keyword_classification(self, data):
        try:
            keyword_classification = KeywordClassification(data, self.topic_name)
            return keyword_classification.run_keyword_classification()
        except Exception:
            print(f'[{self.topic_name}]Keyword classification failed')
            return data
    

