#!/usr/bin/env python

import os

from flask import Flask

from flask.ext.script import Manager
from flask.ext.migrate import Migrate

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config.update(dict(
  SQLALCHEMY_DATABASE_URI='sqlite:////tmp/sample.db',
  DEBUG=True,
  SECRET_KEY='development-key',
))

from sample.models import db

db.app = app
db.init_app(app)

migrate = Migrate(app, db)
manager = Manager(app)

from sample import models, routes
