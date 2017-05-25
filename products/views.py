# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def products(request):
	return HttpResponse("List of products here")
	
def products_kids(request):
	return HttpResponse("List of kids products here")

def product_id(rquest):
	return HttpResponse("Individual product here")