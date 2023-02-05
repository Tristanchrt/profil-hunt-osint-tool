from brokerstream import BrokerStreams
from config.config import Settings

try:
    brokerStr = None
    consumer_jobs = None
    producer_job = None

    brokerStr = BrokerStreams('consumer_jobs', Settings().producer_topic_name, Settings().broker_url)
    producer_job = Settings().producer_topic_name 
    consumer_jobs = Settings().consume_topic_name.split(",") 

except:
    print('=============================================\n')
    print('[Error] : No broker avaialble on the cluster\n')
    print('=============================================\n')
