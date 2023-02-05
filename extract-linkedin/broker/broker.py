from brokerstream import BrokerStreams
from config import Settings

try:

    brokerStr = BrokerStreams(Settings().consume_topic_name, Settings().producer_topic_name,
                            Settings().broker_url)

    producer_name = Settings().producer_topic_name
    consumer_name = Settings().consume_topic_name

except:
    producer_name = None
    consumer_name = None
    brokerStr = None
