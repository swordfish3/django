from django.shortcuts import render
from django.http import HttpResponse
import json
from urllib.request import urlopen


def index(request):
    return HttpResponse("hello there")


def all_products(request):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/?format=json').read().decode('utf-8')
    alldata = json.loads(web_data)
    context = {'alldata': alldata}
    return render(request, 'allproducts.html', context)


def product_info(request, pharmacyid):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/'+str(pharmacyid)+"/?format=json").read().decode('utf-8')
    p_data = json.loads(web_data)
    context = {'pdata': p_data}
    return render(request, "product.html", context)
