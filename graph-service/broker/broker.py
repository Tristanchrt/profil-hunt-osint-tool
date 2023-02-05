from kafka import KafkaProducer, KafkaConsumer
from config.config import Settings
from dataclasses import dataclass
from enum import Enum
from brokerstream import BrokerStreams

brokerStr = BrokerStreams(Settings().consume_topic_name, Settings().producer_topic_name, \
Settings().broker_url)


consumer_name = Settings().consume_topic_name
