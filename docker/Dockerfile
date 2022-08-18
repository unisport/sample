#
# Use poetry to build wheel and install dependencies into a virtual environment.
# This will store the dependencies during compile docker stage.
# In run stage copy the virtual environment to the final image. This will reduce the 
# image size.
#
# Install poetry using pip, to allow version pinning. Use --ignore-installed to avoid
# dependency conflicts with poetry.
#

ARG UNISPORT_PYTHON_VERSION=3.10

# ---------------------------------------------------------------------------------------

##
# base: Configure python environment and set workdir
##
FROM python:${UNISPORT_PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1 \
  PYTHONFAULTHANDLER=1 \
  PYTHONHASHSEED=random \
  PYTHONUNBUFFERED=1
  
WORKDIR /app

# configure user pyuser:
RUN useradd --user-group --create-home --no-log-init --shell /bin/bash pyuser && \
  chown pyuser /app


# ---------------------------------------------------------------------------------------

##
# compile:  Install dependencies from poetry exported requirements
#           Use poetry to build the wheel for the python package.
#           Install the wheel using pip.
##

FROM base as compile

ARG DEPLOY_ENV=development \
  POETRY_VERSION=1.1.7

# pip:
ENV PIP_DEFAULT_TIMEOUT=100 \
  PIP_DISABLE_PIP_VERSION_CHECK=1 \
  PIP_NO_CACHE_DIR=1

# system dependencies:
RUN apt-get update && \
  apt-get install -y --no-install-recommends \
  build-essential gcc && \
  apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false && \
  apt-get clean -y && \
  rm -rf /var/lib/apt/lists/*

# install poetry, ignoring installed dependencies
RUN pip install --ignore-installed "poetry==$POETRY_VERSION" 

# virtual environment:
RUN python -m venv /opt/venv
ENV VIRTUAL_ENV=/opt/venv 
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# install dependencies:
COPY pyproject.toml poetry.lock ./
RUN /opt/venv/bin/pip install --upgrade pip \
  && poetry install $(if [ "$DEPLOY_ENV" = 'production' ]; then echo '--no-dev'; fi) \
    --no-ansi \
    --no-interaction

# copy source:
COPY . .

# build and install wheel:
RUN poetry build && /opt/venv/bin/pip install dist/*.whl

# -------------------------------------------------------------------------------------------

##
# run:          Copy virtualenv from compile stage, to reduce final image size
#               Run the docker-entrypoint.sh script as pyuser
# 
#               This performs the following actions when the container starts:
#               - Make and run database migrations
#               - Collect static files
#               - Create the superuser
#               - Run wsgi app using gunicorn
#               
# port:         5000
#
# build args:   
#
#   GIT_HASH                    Git hash the docker image is derived from
#
# environment:
#
#   DJANGO_DEBUG                True if django debugging is enabled
#   DJANGO_SECRET_KEY           The secret key used for django server, defaults to secret
#   DJANGO_SUPERUSER_EMAIL      Django superuser email, default=myname@example.com
#   DJANGO_SUPERUSER_PASSWORD   Django superuser passwd, default=Pa55w0rd
#   DJANGO_SUPERUSER_USERNAME   Django superuser username, default=admin
##

FROM base as run

ARG GIT_HASH \
  UNISPORT_PYTHON_VERSION

ENV DJANGO_DEBUG=${DJANGO_DEBUG:-False}
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY:-secret}
ENV DJANGO_SETTINGS_MODULE=unisport.settings
ENV DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"myname@example.com"}
ENV DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD:-"Pa55w0rd"}
ENV DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME:-"admin"}
ENV DJANGO_CSRF_TRUSTED_ORIGINS=${DJANGO_CSRF_TRUSTED_ORIGINS:-"http://localhost:8000"}

ENV GIT_HASH=${GIT_HASH:-dev}
ENV UNISPORT_PYTHON_VERSION=${UNISPORT_PYTHON_VERSION}


# install virtualenv from compiled image
COPY --chown=pyuser:pyuser --from=compile /opt/venv /opt/venv

# set path for virtualenv and VIRTUAL_ENV to activate virtualenv
ENV VIRTUAL_ENV="/opt/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY --chown=pyuser:pyuser ./docker/docker-entrypoint.sh ./

USER pyuser

RUN mkdir -p "/opt/venv/lib/python${UNISPORT_PYTHON_VERSION}/site-packages/unisport/root"

EXPOSE 5000

ENTRYPOINT ["./docker-entrypoint.sh"]

