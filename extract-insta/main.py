# from broker.broker import brokerStr
# from brokerstream import Connectors, SearchType, DtoBk
from dump import *
from user import *
from auth import *
# from kafka import KafkaProducer, KafkaConsumer
from json import dumps, loads

def main():

    cl = login()
    profile = User("maxime_amerger", cl)

    # brokerStr.send_message(dump())

    # CONNECTORS = Connectors.INSTA.value
    # ALL_SEARCH = [e.value for e in SearchType]
    # CONNECTOR_NAME = 'EXTRACT'
    data = dump(profile)
    print("Dump finished")
    cl.logout()
    print("logout done")


    # try:
    #     brokerStr.consume_topic().subscribe([str(s)+'_'+str(CONNECTORS)+'_'+CONNECTOR_NAME for s in ALL_SEARCH])
    #     print([str(s)+'_'+str(CONNECTORS)+'_EXTRACT' for s in ALL_SEARCH])
    # except Exception as e:
    #     raise f"Error while subscribing to Kafka consumer : {e}"

    # while True:
    #     try:
    #         raw_messages = brokerStr.consume_topic().poll(
    #             timeout_ms=100, max_records=200
    #         )
    #         for topic_partition, messages in raw_messages.items():
    #             # if message topic is k_connectin_status
    #             if topic_partition.topic == 'FIRST_LAST_NAME_INSTA_EXTRACT':
    #                 # TODO YOUR FUNCTION FOR RUNNING EXTRACTOR
    #                 print('1', messages)
    #                 run_to_transform(topic_partition.topic)
    #     except Exception as e:
    #         raise f"Error while consuming topic kafka : {e}"


if __name__ == "__main__":
    main()
