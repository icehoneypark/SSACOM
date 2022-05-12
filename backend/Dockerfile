From python:3.8.10

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/docker-server
ADD . /srv/docker-server

WORKDIR /srv/docker-server

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8004
CMD ["python", "manage.py", "runserver", "0.0.0.0:8004"]