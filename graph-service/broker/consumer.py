from broker.broker import brokerStr, consumer_name
import time


# def consume_topics():

#     def process_message_broker(data_to_find):
#         print('data_to_find', data_to_find)

#     try:
#         brokerStr.consume_topic().subscribe([consumer_name])
#     except Exception as e:
#         raise f"Error while subscribing to Kafka consumer : {e}"

#     while True:
#         try:
#             raw_messages = brokerStr.consume_topic().poll(1000)
#             raw_messages = brokerStr.consume_topic().poll(100)
#             raw_messages = brokerStr.consume_topic().poll(100)

#             for topic_partition, messages in raw_messages.items():
#                 if consumer_name == topic_partition.topic:
#                     if messages[0]:
#                         pass
#                         # process_message_broker(messages[0].value)

#         except Exception as e:
#             raise f"Error while consuming topic kafka : {e}"
#         finally:
#             print('Waiting for data...')
#             time.sleep(3)

def consume_topics():
    return None
