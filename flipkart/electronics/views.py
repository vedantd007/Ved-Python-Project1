from django.shortcuts import render,redirect, get_object_or_404 # type: ignore
from .models import Product
from .forms import ProductForm

# Create your views here.



def product_detail(request):
    prod = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProductForm()
    return render (request, 'electronics/product_detail.html' , {"prod": prod , "form":form})

def update_product(request, id):
    prod = get_object_or_404(Product, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=prod)
        if form.is_valid():
            
            form.save()
            return redirect('product_detail1')
    
    else:
        form = ProductForm(instance=prod)

    return render(request, 'electronics/product_form.html', {'form': form})


def delete_product(request, id):
    prod = get_object_or_404(Product, id = id)
    prod.delete()
    return redirect('product_detail1')