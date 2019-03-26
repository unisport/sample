from django.core.management.base import BaseCommand, CommandError
from products.product_import import ProductImport


class Command(BaseCommand):
    help = 'Add products from http://www.unisport.dk/api/sample/'

    def handle(self, *args, **options):
        ProductImport.do_import()
        self.stdout.write("Done fetching products")
