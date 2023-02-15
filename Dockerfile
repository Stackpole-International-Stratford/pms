FROM python:3.9-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --no-cache mariadb-connector-c
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers mariadb-connector-c-dev
RUN python -m pip install --upgrade pip
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /app
COPY ./app /app
COPY ./common_static /app/common_static
WORKDIR /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

CMD [ "entrypoint.sh" ]
