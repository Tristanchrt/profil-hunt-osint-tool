![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)
![forthebadge](https://forthebadge.com/images/badges/powered-by-black-magic.svg)

# **Extract LinkedIn**

This microservice is one of the data extraction methods used in the Profil'Hunt project. It uses **Selenium** to perform graphical interactions with the site and wait for the time needed to collect information with **BeautifulSoup4**.

## **Installation and using the application**

Create the network docker:
```
docker network create ph-test
```

## **Configuration**

The microservice requires some configuration before it can be run. This includes things like database connection details, API keys, and other settings. These configuration settings can be stored in a **.env** file. Let's add our informations to perform a search:

```bash
nano .env > ACCOUNT_USERNAME=<your_linkedin_account_login>
nano .env > ACCOUNT_PASSWORD=<your_linkedin_account_password>
```

Make sure to update the settings before starting the microservice.

## **How to use**

To start LinkedIn's extraction microservice, run:

```bash
docker-compose build
docker-compose up extract-linkedin
```

**Note**: The first time you run this command, it may be not work because the Selenium remote session has not been finished its initialization. Don't panic and run again `docker-compose up extract-linkedin`.

Now, open a web browser and go to : `localhost:4444`

You will be able to see yours Selenium remote sessions, and the first one should be the our LinkedIn's extraction. (The password to access to the session is `secret`)

### **Input**

The input for the microservice needs to be in JSON format and should include the following fields:

- topic name: Name of the current topic.
- parameters: List of the search parameters.
    - Example: `['victor', 'durand', 'lyon']`

### **Output**

The output of the microservice will be in JSON format and will include the following fields:

- data: Dictionnary with all the data found in the extraction.

## **Deployment**

The microservice can be deployed on any hosting platform that supports Python, such as Heroku, AWS, or Google Cloud. Make sure to update the configuration settings for the production environment and to set up proper monitoring and logging.

## **Additional resources**

- [Selenium](https://selenium-python.readthedocs.io/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
