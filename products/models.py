from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

BOOL_CHOICES = (("1", "True"), ("0", "False"))

@python_2_unicode_compatible
class Product(models.Model):
    """Product model that mirrors the unisport sample
    api data."""

    name = models.CharField(_("name"), max_length=254)
    is_customizable = models.CharField(
        _('customizable?'), default="0",
        max_length = 1, choices=BOOL_CHOICES)
    delivery = models.CharField(_("delivery"), max_length=50)
    kids = models.CharField(_("kids"), default="0", max_length = 1,
        choices=BOOL_CHOICES)
    kid_adult = models.CharField(_("kid adult"),
        default="0", max_length = 1,
        choices=BOOL_CHOICES)
    free_porto = models.CharField(_("free porto"),
        default="0", max_length = 1,
        choices=BOOL_CHOICES)
    image = models.URLField(_('image'), blank=True, null=True)
    package = models.CharField(_('package'),
        default="0", max_length = 1,
        choices=BOOL_CHOICES)
    url = models.URLField(_("url"), blank=True, null=True)
    sizes = models.TextField(_("Sizes"), default="One Size")
    online = models.CharField(_("online"), default="0", max_length = 1,
        choices=BOOL_CHOICES)
    img_url = models.URLField(_("image URL"), blank=True, null=True)
    women = models.CharField(_("women"), default="0", max_length = 1,
        choices=BOOL_CHOICES)
    price = models.DecimalField(
        _("price"), max_digits=7, decimal_places=2)
    price_old = models.DecimalField(
        _("old price"), max_digits=7, decimal_places=2)
    currency = models.CharField(_("currency"), max_length=50)

    class Meta:
        ordering = ("price", "name")
    
    def __str__(self):
        return self.name
