![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

# **Extract Instagram**

This microservice is one of the data extraction methods used in the Profil'Hunt project. It uses the Instagram API to collect public informations of the target with the group project account.

## **Installation and using the application**

Create the network docker:
```
docker network create ph-test
```

## **Configuration**

```bash
nano .env > ACCOUNT_USERNAME=<your_instagram_account_login>
nano .env > ACCOUNT_PASSWORD=<your_instagram_account_password>
```

Make sure to update the settings before starting the microservice.

## **How to use**

1. Create and configure in the `.env` file.
2. docker-compose build
3. docker-compose up 

## **Additional resources**

- [API Graph Instagram](https://developers.facebook.com/docs/instagram-api/)

