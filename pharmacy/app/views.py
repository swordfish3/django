from django.shortcuts import render
from django.http import HttpResponse
import json
from urllib.request import urlopen


def index(request):
    return HttpResponse("hello there")


def all_products(request):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/?format=json').read().decode('utf-8')
    data = json.loads(web_data)
    context = {'data': data}
    return render(request, 'allproducts.html', context)
