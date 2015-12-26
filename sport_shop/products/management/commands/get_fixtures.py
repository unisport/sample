from django.core.management.base import BaseCommand, CommandError
import requests

FIXTURE_URL = 'https://www.unisport.dk/api/sample/'

def download_json(url=FIXTURE_URL):
    response = requests.get(url)
    return response.json()

class Command(BaseCommand):
    help = 'Downloads product fixtures.'

    def handle(self, *args, **options):
        data = download_json()
        print data