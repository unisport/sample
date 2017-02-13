from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


class Product(models.Model):

	name = models.CharField(_('Name'), max_length=150)
	is_customizable = models.IntegerField(_('customozable?'), default=0)
	delivery = models.CharField(_('Delivery'), max_length=50)
	kids = models.IntegerField(_('Kids'), defulat=0)
	kid_adult = models.IntegerField(_('kid adult'), defualt=0)
	product_id = models.IntegerField(_('product id'), editable=False)
	free_porto = models.IntegerField(_('free porto'))
	image = models.URLField(_('image'))
	package = models.IntegerField(_('package'))
	
