import json
import threading
import argparse
from controllers.controller import Controller
# from broker.broker import brokerStr, producer_name, consumer_name
import time


"""
DEV TEST
"""

controller_linkedin = Controller()
res = controller_linkedin.run_search({'data': {}, 'params': ['victor', 'durand', 'lyon']})
# send_data_next_step(res)


# def send_data_next_step(data):
# 	print("send_data_next_step", data)
# 	brokerStr.send_message(data, producer_name)


# def process_message_broker(data_to_find):
# 	if data_to_find is not None:
# 		print('data_to_find', data_to_find)
# 		time.sleep(3)
# 		controller_linkedin = Controller()
# 		res = controller_linkedin.run_search(data_to_find)
# 		send_data_next_step(res)

# try:
# 	brokerStr.consume_topic().subscribe([consumer_name])
# except Exception as e:
# 	raise f"Error while subscribing to Kafka consumer : {e}"

# threads = []
# maxthreads = 5
# while True:
# 	try:
# 		if threading.activeCount() <= maxthreads:
# 			raw_messages = brokerStr.consume_topic().poll(
# 				timeout_ms=100, max_records=200
# 			)
# 			for topic_partition, messages in raw_messages.items():
# 				if consumer_name == topic_partition.topic:
# 					if messages[0]:
# 						data = json.loads(messages[0].value)
# 						print('\nDATA FROM SEARCH :', data['params'])
# 						t = threading.Thread(target=process_message_broker, args=(data,))
# 						threads.append(t)
# 						t.start()

# 	except Exception as e:
# 		raise f"Error while consuming topic kafka : {e}"
# 	print('Waiting for data...')
# 	time.sleep(1)

