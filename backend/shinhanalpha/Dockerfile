FROM python:3.11.3

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install -r requirements.txt
RUN python manage.py migrate

USER root
EXPOSE 8000

CMD ["/bin/bash", "gunicorn_start"]