# Profil hunt broker module
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## Python packet 
- https://pypi.org/

> This module allows services to communicate between each other with kafka

### Build and Deploy packet

```
rm -rf build
rm -rf dist
rm -rf brokerstream.egg-info
python3 setup.py sdist bdist_wheel
twine upload dist/*
```

- You need to change the version of the module inside **setup.py** before deploying
- This module is deployed in **pypi**

### How to use 

```py
# Import module and create object
from brokerstream import BrokerStreams
from log import logger

brokerStr = BrokerStreams(Settings().consume_topic_name, Settings().producer_topic_name, Settings().broker_url)
```

```py
# Provide message
brokerStr.send_message(data, topic_name)
```

```py
# Consume messages
brokerStr.consume_topic().subscribe([consumer_name])

while True:
    raw_messages = brokerStr.consume_topic().poll(
        timeout_ms=100, max_records=200
    )
    for topic_partition, messages in raw_messages.items():
        if consumer_name == topic_partition.topic:
            print('DATA FROM SEARCH :', messages[0])

```