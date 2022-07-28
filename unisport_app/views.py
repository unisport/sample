import requests
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponseRedirect('/products')


def products(request):
    return HttpResponse('<h1>Products page</h1>')


def product_detail(request):
    return HttpResponse('<h1>Product detail</h1>')
