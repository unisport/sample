FROM python:3.8
ENV PYTHONUNBUFFERD 1
RUN mkdir /app
WORKDIR /app

# Add tini
ENV TINI_VERSION v0.14.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# dockerize
RUN wget -qO - https://github.com/jwilder/dockerize/releases/download/v0.4.0/dockerize-linux-amd64-v0.4.0.tar.gz \
    | tar -xzC /usr/local/bin

COPY requirements.txt /app/
RUN pip install -r requirements.txt

COPY . /app/

ENTRYPOINT ["/tini", "/app/docker_startup.sh"]
