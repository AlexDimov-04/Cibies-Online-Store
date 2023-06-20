from django.shortcuts import render, redirect
from cibies_store.products.forms import ProductCreateForm, ProductEditForm, ProductDeleteForm
from cibies_store.user_profile.models import Profile
from cibies_store.products.models import Product


def shopping_cart(request):
    profile = Profile.objects.first()
    products = Product.objects.all()

    context = {
        'profile': profile,
        'products': products
    }

    return render(request, 'shopping_cart/shopping_cart.html', context=context)

def create_product(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProductCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('shopping cart')
        
    else:
        form = ProductCreateForm()

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'products/create-product.html', context=context)

def details_product(request, pk):
    profile = Profile.objects.first()
    product = Product.objects.get(pk=pk)

    context = {
        'profile': profile,
        'product': product
    }

    return render(request, 'products/details-product.html', context=context)

def edit_product(request, pk):
    profile = Profile.objects.first()
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductEditForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('shopping cart')
    else:
        form = ProductEditForm(instance=product)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'products/edit-product.html', context=context)

def delete_product(request, pk):
    profile = Profile.objects.first()
    product = Product.objects.get(pk=pk)

    if request.method == 'POST':
        form = ProductDeleteForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('shopping cart')
        
    else:
        form = ProductDeleteForm(instance=product)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'products/delete-product.html', context=context)
