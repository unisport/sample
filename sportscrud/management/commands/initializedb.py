
from django.core.management.base import BaseCommand, CommandError

from sportscrud.initialize import DatabaseInitializer


class Command(BaseCommand):
	""" Just exposing the initialization of database a """

	help = 'Populate database with sample products'

	def handle(self, *args, **options):

		try:
			DatabaseInitializer.initialize()
		except RuntimeError as e:
			raise CommandError(e)