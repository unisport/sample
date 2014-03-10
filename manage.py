#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests, json

from sample import app, manager

from flask.ext.migrate import MigrateCommand

@manager.command
def seed():
  """ Fetch data and and put in database.
  """
  from sample.models import Item, db

  all_items = Item.query.order_by(Item.id).all()

  if all_items:
    for item in all_items:
      db.session.delete(item)
    db.session.commit()

  url = 'http://www.unisport.dk/api/sample/'

  r = requests.get(url)
  data = r.json()

  for key, value in data.items():
    for item in value:
      i = Item(**item)
      db.session.add(i)

    db.session.commit()


manager.add_command('db', MigrateCommand)

app.debug = True

manager.run()
