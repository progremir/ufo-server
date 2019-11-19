FROM python:3.8-alpine3.10
ENV PYTHONUNBUFFERED 1
ARG PORT=5000

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk update \
# install psycopg2 dependencies
    && apk add --no-cache postgresql-libs \
        zlib-dev \
        jpeg-dev \
    && apk add --no-cache --virtual .requirements-build-deps \
        gcc \
        musl-dev \
        postgresql-dev \
        libffi-dev \
        libxml2-dev \
        libxslt-dev \
# install requirements
    && pip install --no-cache-dir -r requirements.txt \
    && rm requirements.txt \
    && apk del .requirements-build-deps

COPY . .

ENTRYPOINT [ "/app/entrypoint.sh" ]
EXPOSE $PORT