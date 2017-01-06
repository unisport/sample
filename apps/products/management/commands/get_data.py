# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals

import json
import urllib3

from django.core.management.base import BaseCommand, CommandError

from apps.products.models import Product, Size


class Command(BaseCommand):
    """
    retrieve data from http://www.unisport.dk/api/sample/, parse it and store
    into database
    """
    URL = 'http://www.unisport.dk/api/sample/'

    def handle(self, *args, **options):
        http = urllib3.PoolManager()
        try:
            response = http.request('GET', self.URL)
        except Exception as err:
            self.stderr.write('error occurred:')
            self.stderr.write(err.message)
            return
        else:
            if response.status is not 200:
                self.stderr.write('can\'t reach server or other error occurred:')
                self.stderr.write(response.status)
                return
        body = response.data
        try:
            data = json.loads(body)
        except Exception as err:
            self.stderr.write(err.message)
            return

        for item in data.get('latest', []):
            sizes = self.get_sizes(item.get('sizes', ''))
            item.update({
                'price': item.get('price', '0').replace('.', '').replace(',', '.'),
                'price_old': item.get('price_old', '0').replace('.', '').replace(',', '.'),
                'free_porto': json.loads(item.get('free_porto').lower()),
            })
            item.pop('sizes', None)
            try:
                product = Product.objects.get(id=item.get('id'))
            except Product.DoesNotExist:
                product = Product(**item)
                product.save()
            else:
                for key, value in item.iteritems():
                    setattr(product, key, value)
                product.save()
            product.sizes.clear()
            for size in sizes:
                product.sizes.add(size)

        self.stdout.write('Done')

    @staticmethod
    def get_sizes(sizes_string):
        """
        construct list of Size instances
        :param sizes_string:
        :return: sizes
        """
        sizes_strings = sizes_string.split(',')
        sizes = list()
        for sizes_string in sizes_strings:
            # we get or create size, that guarantee that we don't create
            # new Size Instance with the same size measure
            size, created = Size.objects.get_or_create(size=sizes_string.strip())
            sizes.append(size.id)
        return sizes