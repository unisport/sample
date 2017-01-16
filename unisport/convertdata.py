#!/usr/bin/env python

"""
Small script for fetching the sample data, and converting it into a fixture that
can be loaded into a django model.
"""

import json
import sys
from urllib2 import Request, urlopen, URLError, HTTPError
import subprocess

if __name__=='__main__':
    try:
        url = 'http://unisport.dk/api/sample'
        request = Request(url)
        response = urlopen(url)
        data = response.read()
    except URLError, HTTPError:
        sys.exit(1)

    data = json.loads(data.strip())
    with open("convdata.json","w+") as convdata:
        # write the initial data for the JSON file
        convdata.write("[\n")

        last = len(data["latest"])
        i = 1

        for jsonobj in data["latest"]:
            name = jsonobj["name"].encode('ascii', errors='ignore')
            kids = int(jsonobj["kids"])
            price = float(jsonobj["price"].replace(",","."))
            sizes = jsonobj["sizes"].encode('ascii', errors='ignore')
            url = jsonobj["url"].encode('ascii', errors='ignore')
            free_porto = int(jsonobj["free_porto"])
            package = jsonobj["package"].encode('ascii', errors='ignore')
            delivery = jsonobj["delivery"].encode('ascii', errors='ignore')
            kid_adult = int(jsonobj["kid_adult"])
            price_old = float(jsonobj["price_old"].replace(",","."))
            img_url = jsonobj["img_url"].encode('ascii', errors='ignore')
            id = int(jsonobj["id"])
            women = int(jsonobj["women"])

            jsondata = "{ \"pk\": " + str(id) + ",\n"
            jsondata += " \"model\": \"products.item\" ,\n"
            jsondata += "\t\"fields\": {\n"
            jsondata += "\t\"name\": \"" + str(name) + "\",\n"
            jsondata += "\t\"delivery\": \"" + str(delivery) + "\",\n"
            jsondata += "\t\"package\": " + str(package) + ",\n"
            jsondata += "\t\"sizes\": \"" + str(sizes) + "\",\n"
            jsondata += "\t\"women\": " + str(women) + ",\n"
            jsondata += "\t\"img_url\": \"" + str(img_url) + "\",\n"
            jsondata += "\t\"url\": \"" + str(url) + "\",\n"
            jsondata += "\t\"free_porto\": " + str(free_porto) + ",\n"
            jsondata += "\t\"kid_adult\": " + str(kid_adult) + ",\n"
            jsondata += "\t\"price\": " + str(price) + ",\n"
            jsondata += "\t\"price_old\": " + str(price_old) + ",\n"
            jsondata += "\t\"kids\": " + str(kids) + "\n"
            if i != last:
                jsondata += "\t}\n},\n"
            else:
                jsondata += "\t}\n}\n"

            i += 1

            convdata.write(jsondata)

        convdata.write("]")

    # call the django-admin.py  loaddata convdata.
    subprocess.Popen(['python', 'manage.py', 'loaddata', 'convdata.json'])
