from django.shortcuts import render, redirect
from cibies_store.products.models import Product
from cibies_store.user_profile.forms import ProfileCreateForm, \
    ProfileEditForm, ProfileDeleteForm
from cibies_store.user_profile.models import Profile

def index(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile
    }

    return render(request, 'home/index.html', context=context)

def create_profile(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = ProfileCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('shopping cart') 
    else:
        form = ProfileCreateForm()

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profile/create-profile.html', context=context)

def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProfileDeleteForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = ProfileDeleteForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'profile/delete-profile.html', context)

def details_profile(request):
    profile = Profile.objects.first()
    products_count = Product.objects.count()

    context = {
        'profile': profile,
        'products_count': products_count
    }

    return render(request, 'profile/details-profile.html', context=context)

def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('details profile')
    else:
        form = ProfileEditForm(instance=profile)

    context = {
        'profile': profile,
        'form': form,
    }

    return render(request, 'profile/edit-profile.html', context=context)