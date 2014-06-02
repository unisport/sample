from django.core.management.base import BaseCommand, CommandError
from webapp.models import *
import urllib
import json

class Command(BaseCommand):
    help = 'Load the API into database'

    def handle(self, *args, **options):
        listofstrings = urllib.urlopen('http://www.unisport.dk/api/sample/').read()
        jsonload = json.loads(listofstrings)
        newlist = jsonload['latest']

        for num in range(0, newlist.__len__()):
            
            kids = newlist[num]["kids"] 
            
            name = newlist[num]["name"]
            
            sizes = newlist[num]["sizes"]
            
            kid_adult = newlist[num]["kid_adult"]
            
            free_porto = newlist[num]["free_porto"]
            if free_porto == "True":
                free_porto = True
            else:
                free_porto = False

             
            price = float(str(newlist[num]["price"]).replace(",","."))

            package = newlist[num]["package"]
            
            url = newlist[num]["url"]

            price_old = str(newlist[num]["price_old"]).replace(".","")
            price_old = float(price_old.replace(",",".")) 
            
            img_url = newlist[num]["img_url"]
            
            productID = newlist[num]["id"]
            
            women = newlist[num]["women"]

            p = Product.objects.create(kids=kids, 
                                    name=name,
                                    sizes=sizes,
                                    kid_adult=kid_adult,
                                    free_porto=free_porto,
                                    price=price,
                                    package=package,
                                    url=url,
                                    price_old=price_old,
                                    img_url=img_url,
                                    productID=productID,
                                    women=women
                                    )

        print "API has succesfully been loaded from http://www.unisport.dk/api/sample/"