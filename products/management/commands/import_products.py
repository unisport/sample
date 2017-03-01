from django.core.management.base import BaseCommand
from ...models import Product
from pyunisport.models import UnisportAPI

unisport = UnisportAPI()

class Command(BaseCommand):
	help = """
	    Populate database with products from sample
	    api end point.
	"""

	def handle(self, *args, **options):

		products, status_code = unisport.get_all()


		for product in products["products"]:
			Product.objects.create(
				is_customizable=product["is_customizable"],
				delivery=product[u"delivery"],
				kids=product["kids"],
				name=product[u"name"],
				package=product["package"],
				kid_adult=product["kid_adult"],
				free_porto=product["free_porto"],
				image=product["image"],
				sizes=product["sizes"],
				price=product["price"].replace(".", "").replace(",", "."),
				url=product["url"],
				online=["online"],
				price_old=product["price_old"].replace(".", "").replace(",", "."),
				currency=["currency"],
				img_url=["img_url"],
				women=["women"])

		self.stdout.write(self.style.SUCCESS("Import successful!"))