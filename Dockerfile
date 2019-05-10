FROM python:2.7.16-alpine

ARG DJANGO_SETTINGS_MODULE
ARG HEROKU_DEPLOY=False

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN \
 apk add --no-cache curl && \
 apk add --no-cache gettext && \
 apk add --no-cache libffi-dev && \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc jpeg-dev zlib-dev musl-dev postgresql-dev && \
 pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

COPY . /code/

RUN ls -l
RUN sudo chown root:root ./heroku-release-tasks.sh
RUN sudo chmod 700 ./heroku-release-tasks.sh

RUN if [ "$HEROKU_DEPLOY" = "False" ] ; then \
        python manage.py makemessages -l es ; \
        python manage.py compilemessages ; \
    fi
