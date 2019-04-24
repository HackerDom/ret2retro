FROM python:3.7-alpine3.9

WORKDIR /opt/ret2retro/
COPY setup.py /opt/ret2retro/


RUN apk add --no-cache make gcc g++ python3-dev && \
    pip install -e .

COPY ./ret2retro /opt/ret2retro/ret2retro
COPY ./static /opt/ret2retro/static

EXPOSE 80

CMD ["python", "-m", "ret2retro"]
