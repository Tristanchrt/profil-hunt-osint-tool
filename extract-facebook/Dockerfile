FROM python:3.8

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

ADD ./ /app

CMD [ "python","-u", "./main.py" ]