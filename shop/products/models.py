#!/usr/bin/env python
# -*- encoding: UTF-8 -*-
"""
Propose: Describe models
Author: 'yac'
"""

from django.db import models

class Product(models.Model):
    """ Product model """
    id_ext = models.TextField()
    kids = models.TextField()
    name = models.TextField()
    sizes = models.TextField()
    kid_adult = models.TextField()
    free_porto = models.TextField()
    price = models.TextField()
    package = models.TextField()
    delivery = models.TextField()
    url = models.TextField()
    price_old = models.TextField()
    img_url = models.TextField()
    women = models.TextField()

    def __unicode__(self):
        return u'%s' % self.name
