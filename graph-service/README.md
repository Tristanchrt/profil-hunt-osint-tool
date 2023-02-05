# **Graph Service**

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

This microservice is one of the data extraction methods used in the Profil'Hunt project. It uses several external API such as **DeepFace** or **OpenAI** which help us to create new metrics to analyze.

## **Installation and using the application**

Create the network docker:
```
docker network create ph-test
```

## **Configuration**

This is a configuration file that contains all basics necessary configuration for running this service
```
DATABASE_URL_LOADED=mongodb://test:test123@ph_loaded:27017/testdb?authSource=admin&retryWrites=true&w=majority
DATABASE_URL_DATALAKE=mongodb://test:test123@ph_datalake:27017/testdb?authSource=admin&retryWrites=true&w=majority
broker_url=kafka:9092
consume_topic_name=useless
producer_topic_name=JOB_FINISHED

secret_key=1234
```

## **How to use**

1. Create and configure in the `.env` file.
2. docker-compose build
3. docker-compose up 

This will start the microservice and make it available to handle requests.

To test the microservice, you can use curl or any other tool you prefer to send a request to the endpoint and check the response.

## **Endpoints**

Access to documentation `http://localhost:8082/docs`.

## **Additional resources**

- [DeepFace](https://github.com/serengil/deepface)
- [OpenAI](https://beta.openai.com/docs/introduction)

