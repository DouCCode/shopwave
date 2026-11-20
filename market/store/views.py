from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from . models import Product

# Create your views here.

def index(request):
    return HttpResponse("index")


def product_list(request):
    products = Product.available_products.all()
    context = {
        'products': products,
    }

    return render(request, 'store/list.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product.available_products, id=id)
    context = {
            'product': product,
        }
    
    return render(request, 'store/detail.html', context)
