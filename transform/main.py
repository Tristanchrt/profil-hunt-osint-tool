import traceback
import sys
from time import sleep
from broker.broker import brokerStr, consumer_jobs, producer_job
# from brokerstream import Connectors, SearchType, DtoBk
from json import dumps, loads
from controllers.transform import Transform
import json
import asyncio
import time


async def send_data_next_step(data):
    print("send_data_next_step", data)
    brokerStr.send_message(data, "DATA")

async def process_message_broker(data, name_job):
    print('Process starting...')
    transform = Transform()
    data_transformed = await transform.send_data(data, name_job)
    await send_data_next_step(data_transformed)


async def main():
    try:
        brokerStr.consume_topic().subscribe(consumer_jobs)
    except Exception as e:
        raise f"Error while subscribing to Kafka consumer : {e}"

    """Prod | Dev"""
    while True:
        try:
            raw_messages = brokerStr.consume_topic().poll(
                timeout_ms=100, max_records=200
            )
            for topic_partition, messages in raw_messages.items():
                if consumer_jobs[0] == topic_partition.topic:
                    # Facebook
                    if messages[0]:
                        await process_message_broker(messages[0].value, "FACEBOOK")
                if consumer_jobs[1] == topic_partition.topic:
                    # Insta
                    if messages[0]:
                        await process_message_broker(messages[0].value, "INSTA")
                if consumer_jobs[2] == topic_partition.topic:
                    # LinkedIn
                    if messages[0]:
                        await process_message_broker(messages[0].value, "LINKEDIN")

        except Exception as e:
            raise f"Error while consuming topic kafka : {e}"
        print('Waiting for data...')
        time.sleep(2)


    """Test"""
    # mypath = os.getcwd() + '/input'
    # for file in [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]:
    #     if 'linkedin' in file:
    #         topic_name = 'LINKEDIN'
    #     elif 'insta' in file:
    #         topic_name = 'INSTA'
    #     elif 'facebook' in file:
    #         topic_name = 'FACEBOOK'
    #     else:
    #         break
    #     with open(f'{mypath}/{file}', 'r') as f:
    #         data = json.load(f)
    #     transform = Transform()
    #     await transform.send_data(data, topic_name)

    #     print('Job ended successfully')


if __name__ == "__main__":
    print('Transform starting...')
    asyncio.run(main())
