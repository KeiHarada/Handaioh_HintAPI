#FROM kstromeiraos/django-rest-framework
FROM python:3-alpine
MAINTAINER Harada <harada.kei@ist.osaka-u.ac.jp>

RUN apk add --update && \
    pip install --upgrade pip
    pip install django && \
    pip install djangorestframework && \
    pip install markdown # Markdown support for the browsable API. && \
    pip install django-filter && \
    && rm -rf /var/cache/apk/*

RUN mkdir /app
WORKDIR /app
EXPOSE 80
COPY docker-entrypoint.sh
RUN chmod 755 /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
