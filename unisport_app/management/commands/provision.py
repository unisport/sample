# import requests
# import random
from django.core.management.base import BaseCommand
# from unisport_app.models import Product, Stock, Price, Currency
from django.contrib.auth.models import User
from unisport_app.models import Currency


class Command(BaseCommand):

    def handle(self, **options):
        print('Creating admin user...')
        # Add admin user
        admin_user = User.objects.create_user(
            username='unisport', password='unisport', is_superuser=True, is_staff=True)
        print(f'Admin user: {admin_user}')

        # Add currencies
        print('Adding Currencies...')
        currency_dkk_obj, created_dkk = Currency.objects.get_or_create(
            currency_code='DKK')
        currency_eur_obj, created_eur = Currency.objects.get_or_create(
            currency_code='EUR')
        currency_nok_obj, created_nok = Currency.objects.get_or_create(
            currency_code='NOK')
        currency_sek_obj, created_sek = Currency.objects.get_or_create(
            currency_code='SEK')

        print(f'*** DKK - Created: {created_dkk}, {currency_dkk_obj}')
        print(f'*** EUR - Created: {created_eur}, {currency_eur_obj}')
        print(f'*** NOK - Created: {created_nok}, {currency_nok_obj}')
        print(f'*** SEK - Created: {created_sek}, {currency_sek_obj}')
