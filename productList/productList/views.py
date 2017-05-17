from django.shortcuts import render
from django.http      import HttpResponse
from django.views     import generic

def home(request):
    return render(request, 'productList/index.html')

def documentation(request):
    return render(request, 'productList/documentation.html')
