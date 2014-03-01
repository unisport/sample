#!/usr/bin/env python

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
  __tablename__ = 'item'
  id          = db.Column(db.Integer, primary_key=True)
  kids        = db.Column(db.Boolean)
  kid_adult   = db.Column(db.Boolean)
  women       = db.Column(db.Boolean)
  package     = db.Column(db.Boolean)
  free_porto  = db.Column(db.Boolean)
  name        = db.Column(db.String(200))
  url         = db.Column(db.String(200))
  img_url     = db.Column(db.String(200))
  sizes       = db.Column(db.String(100))
  delivery    = db.Column(db.String(50))
  price_old   = db.Column(db.Integer)
  price       = db.Column(db.Integer)
  
  def __init__(self,
               id, 
               kids, 
               kid_adult, 
               women, 
               package, 
               free_porto, 
               name, 
               url,
               img_url, 
               sizes, 
               delivery, 
               price_old, 
               price):
    self.id = id 
    self.kids = kids
    self.kid_adult = kid_adult
    self.women = women
    self.package = package
    self.free_porto = free_porto
    self.name = name
    self.url = url
    self.img_url = img_url
    self.sizes = sizes, 
    self.delivery = delivery
    self.price_old = price_old
    self.price = price

  def __repr__(self):
    return '<Item %r>' % self.name
