# Profil hunt search service
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
## FastAPI and MongoDB

FastAPI and MongoDB monitoring by Thundra apm

- https://fastapi.tiangolo.com/
- https://www.thundra.io/apm
- https://www.mongodb.com/fr-fr

## Installation and using the applicaiton

> Change /etc/hosts add
```
127.0.0.1 front.eola.local
127.0.0.1 eola.local
```
> Create the newtork docker
```
docker network create ph-test 
```

### How to use

1. Create and configure in the `.env` file  

2. docker-compose up search_service --build

3. Run on port 8081 on address [0.0.0.0](0.0.0.0:8081)

4. `http://ph.local/docs` access to the documentation

### Configuration of .env

This is a configuration file that contains all basics necessary configuration for running this service

```
DATABASE_URL=mongodb://test:test123@ph_search_data:27017/testdb?authSource=admin&retryWrites=true&w=majority
broker_url=kafka:9092
consume_topic_name=None
producer_topic_name=c.internal.extractor.facebook,c.internal.extractor.insta,c.internal.extractor.linkedin
SC_SERVICE=http://sc_api:3000/auth
```


# Kafka stream

## Presentation

>Apache **Kafka** is an open-source distributed event streaming platform used to build real-time data pipelines and streaming applications. It is horizontally scalable, fault-tolerant, and fast, making it an ideal choice for handling large amounts of data and enabling real-time data processing.

>Kafka works by allowing producers to send data to a topic, which is then divided into partitions and stored on multiple servers. **Consumers** can then read data from these partitions and process it in real-time. Kafka is often used to build data pipelines to move data between systems, or to build real-time streaming applications that react to data as it is produced.

Some of the key features of Kafka include:

- **High throughput**: Kafka is designed to handle high-throughput data streams, allowing it to process millions of events per second.

- **Durability**: Kafka stores all published records for a configurable amount of time, allowing consumers to read data that was produced even if they were not connected to the system at the time the data was produced.

- **Horizontal scalability**: Kafka can handle an increasing amount of data by adding more servers to the cluster, allowing it to scale horizontally.

- **Real-time processing**: Kafka allows consumers to read data as it is produced, enabling real-time data processing and analysis.

- **Publish-subscribe model**: Kafka uses a publish-subscribe model, allowing producers to send data to a topic and allowing consumers to subscribe to one or more topics to receive the data.

## Presentation

>Kafka kafka-ui is a tool for managing Apache Kafka. It provides a web-based interface for viewing and interacting with Kafka clusters, topics, and consumers. With Kafka kafka-ui, you can perform various tasks such as:

- View and modify the configuration of Kafka clusters and brokers.
- Monitor the status and performance of Kafka clusters.
- View and manage topics and consumers.
- Create and delete topics.
- Manually consume messages from a topic.
- Rebalance consumer groups.

>**Kafka kafka-ui** is particularly useful for large organizations that have multiple Kafka clusters, as it allows them to easily manage and monitor all of their clusters from a single, central location. It is also useful for developers who are working with Kafka, as it provides a convenient way to view and interact with **Kafka** topics and consumers.


## Run kafka interface management 

- ```http://localhost:8085/```
## Kafka docker

```yml
  kafka:
    image: 'bitnami/kafka:3.3.1'
    container_name: ph_kafka
    environment:
      - KAFKA_ENABLE_KRAFT=yes
      - KAFKA_CFG_PROCESS_ROLES=broker,controller
      - KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092
      - KAFKA_CFG_BROKER_ID=1
      - KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@kafka:9093
      - ALLOW_PLAINTEXT_LISTENER=yes
      - KAFKA_KRAFT_CLUSTER_ID=r4zt_wrqTRuT7W2NJsB_GA
    volumes:
      - kafka-volume:/bitnami/kafka
    networks:
      - ph-test

  kafka-ui:
    container_name: ph_kafka-ui
    image: 'provectuslabs/kafka-ui:latest'
    ports:
      - "8085:8080"
    environment:
      - KAFKA_CLUSTERS_0_BOOTSTRAP_SERVERS=kafka:9092
      - KAFKA_CLUSTERS_0_NAME=r4zt_wrqTRuT7W2NJsB_GA
    networks:
      - ph-test
```