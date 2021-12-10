FROM python:3.6
ENV PYTHONUNBUFFERED=1

ADD . /app
WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get install gcc && apt-get -qy install netcat

RUN pip install pip==9.0.1
RUN pip install setuptools==57.4.0
RUN pip install -r requirements.txt

COPY . /app

COPY ./wait-for /bin/wait-for
RUN chmod 777 -R /bin/wait-for


