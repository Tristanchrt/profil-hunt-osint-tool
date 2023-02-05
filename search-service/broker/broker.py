from kafka import KafkaProducer, KafkaConsumer
from config.config import Settings
from dataclasses import dataclass
from enum import Enum
from brokerstream import BrokerStreams
from log import logger

brokerStr = None
producer_job = None

try:
    brokerStr = BrokerStreams(Settings().consume_topic_name, Settings().producer_topic_name, \
    Settings().broker_url)
    producer_job = Settings().producer_topic_name.split(",")
except:
    logger.debug('=============================================')
    logger.debug('[Error] : No broker avaialble on the cluster')
    logger.debug('=============================================')
