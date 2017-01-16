# coding=utf-8

from django.core.management.base import BaseCommand, CommandError

from requests.exceptions import Timeout

from product.utils import fetch_json_data, import_json_data


class Command(BaseCommand):
    help = 'Import products from Unisport'

    def handle(self, *args, **options):
        try:
            j_data = fetch_json_data()
        except Timeout:
            self.stdout.write('Cannot reach Unisport')

        res = import_json_data(j_data)

        self.stdout.write(
            'Successfully import {0} new products, update {1} products'.format(
                len(res['created']), len(res['updated'])))
