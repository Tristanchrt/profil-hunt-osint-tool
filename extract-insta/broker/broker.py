from brokerstream import BrokerStreams
from config import Settings

brokerStr = BrokerStreams(Settings().consume_topic_name, Settings().producer_topic_name, \
Settings().broker_url)