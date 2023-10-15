FROM ubuntu:latest

WORKDIR /meditations

RUN apt-get update && apt-get install -y nginx uwsgi pip python3 \
uwsgi-plugin-python3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN mkdir -p /run/uwsgi

COPY python .
COPY --chmod=0755 entrypoint.sh entrypoint.sh
COPY etc /etc
RUN rm /etc/nginx/sites-enabled/default
ENTRYPOINT /meditations/entrypoint.sh
