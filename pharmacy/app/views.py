import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from urllib.request import urlopen
from .models import Product
from .forms import ProductForm
from cart.cart import Cart


def index(request):
    return HttpResponse("hello there")


def all_products(request):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/?format=json').read().decode('utf-8')
    alldata = json.loads(web_data)
    context = {'alldata': alldata}
    return render(request, 'allproducts.html', context)


def product_info(request, pharmacyid):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/' + str(pharmacyid) + "/?format=json").read().decode('utf-8')
    p_data = json.loads(web_data)
    context = {'pdata': p_data}
    return render(request, "product.html", context)


def add_to_cart(request, pharmacyid):
    web_data = urlopen('http://test.hua.gr:8000/pharmacy/' + str(pharmacyid) + "/?format=json").read().decode('utf-8')
    p_data = json.loads(web_data)
    product = Product.objects.create_product(p_data['id'], p_data['name'], p_data['barcode'])
    cart = Cart(request)
    cart.add(product, p_data['price_retail'], 1)


def remove_from_cart(request, name):
    product = Product.object.filter(name).latest(name)
    cart = Cart(request)
    cart.remove(product)


def get_cart(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'cart': cart}, )
