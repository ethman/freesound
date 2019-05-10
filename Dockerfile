FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    git

RUN apt-get update && apt-get install libarchive-zip-perl
#RUN apt-get install postgresql-9.5
#RUN apt-get update && apt-get install libav-tools -y --force-yes
#USER postgres
#RUN psql -c 'create database freesound;' -U postgres

WORKDIR /usr/src/app

ADD . /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN pwd
RUN ls

CMD [ "python", "manage.py", "runserver 0.0.0.0:8000" ]