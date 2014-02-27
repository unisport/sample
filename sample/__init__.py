#!/usr/bin/env python

import os

from flask import Flask

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app.config.update(dict(
  DEBUG=True,
  SECRET_KEY='development-key',
))
