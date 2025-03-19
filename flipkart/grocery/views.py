from django.shortcuts import render
from .models import Product

# Create your views here.

def home(request):
    return render(request,'grocery/home.html')


def product_detail(request):
    prod = Product.objects.all()
    return render (request, 'grocery/product_detail.html' , {"prod":prod})