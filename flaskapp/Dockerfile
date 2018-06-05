FROM ubuntu:16.04

MAINTAINER srujan
RUN apt-get update -y && apt-get install -y python3-pip python3-dev
COPY ./requirements.txt /flaskdock/requirements.txt
WORKDIR /flaskdock
RUN pip3 install -r requirements.txt
COPY . /flaskdock
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]