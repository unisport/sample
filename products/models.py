from django.db import models
import json, urllib2

class Get(models.Model):
	""" A sample model for fetching data.
		In this sample, the data is read from url given
		then stored in the instance.

		In a live enviroment, this data should be stored locally, 
		read from a database, or in an otherwise more effective way.
		Also, it should be tested, not trusted, to be in the right format. 
	"""
	def __init__(self, source):
		super(Get, self).__init__()
		
		# Grabbing the url from source, blindly assuming it's in jason format
		data = urllib2.urlopen(source).read()

		# Converting data to python list, and returning it
		self.json_data = json.loads(data)

	""" Returns the actual data as a python dict.
	"""
	def read(self):
		return self.json_data