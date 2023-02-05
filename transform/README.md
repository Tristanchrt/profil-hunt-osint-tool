# **Data Basic Transformation**

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

This microservice is one of the data extraction methods used in the Profil'Hunt project. It uses several external API such as **DeepFace** or **OpenAI** which help us to create new metrics to analyze.

## **Installation and using the application**

Create the network docker:
```
docker network create ph-test
```

## **How to use**

1. Create and configure in the `.env` file.
2. docker-compose build
3. docker-compose up 

## **Configuration**

This is a configuration file that contains all basics necessary configuration for running this service
```
broker_url=kafka:9092
consume_topic_name=p.internal.transform.facebook,p.internal.transform.insta,p.internal.transform.linkedin
producer_topic_name=p.internal.graph.create
DATABASE_URL=mongodb://test:test123@ph_datalake:27017/testdb?authSource=admin&retryWrites=true&w=majority
```

## **Additional resources**

- [DeepFace](https://github.com/serengil/deepface)
