# FROM python:3.8

# WORKDIR /app

# COPY requirements.txt .


# RUN pip install -r requirements.txt

# ADD ./ /app


# CMD [ "python","-u", "./main.py" ]

FROM python:3.10

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD ./ /app

CMD [ "python","-u", "./main.py" ]