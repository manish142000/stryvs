from datetime import datetime
from itertools import product
from pyexpat.errors import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from stryvs import settings
from . forms import ProductRegistrationForm, ProductRentingForm, ProductUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product
import datetime as dt
from dateutil.relativedelta import relativedelta
from users.models import Transactions
# Create your views here.


@login_required
def product_register(request):
    if request.method == 'POST':
        form = ProductRegistrationForm(request.POST, request.FILES or None)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.owner = request.user
            prod.save()
            messages.success(
                request, f'Your product has been registered! Check here.')
            return redirect('home')
    else:
        print('Post nahi ho rha')
        form = ProductRegistrationForm()

    return render(request, 'product_register.html', {'form': form})


def store(request, id, transaction, action):

    if transaction == 'True':
        obj = Product.objects.filter(id=id)
        if action == 'Buy':
            # delete the product from database if product has been purchased
            obj.delete()
            products = {
                'products': Product.objects.all()
            }
        else:
            # These products are rented by some users so those are not available
            # Display only those products which are available
            obj.is_rented = True
            products = {
                'products': Product.objects.exclude(id=id)
            }
    else:
        for product in Product.objects.all():
            if product.is_rented:
                if datetime(product.tenure_end) >= dt.now():
                    product.is_rented = False
                    product.save()
                    break
        
            
    products = {
                'products' : Product.objects.all()
            }

    return render(request, 'store.html', products)


@login_required
def details(request, product_id=1, action="Buy"):
    product = Product.objects.get(id=product_id)
    owner_id = product.owner.id
    return render(request, 'product_details.html', {'product': product, 'action': action, 'owner_id': owner_id})


@login_required
def Rent(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductRentingForm(request.POST)
        if form.is_valid():
            tenure_end = dt.date.today() + relativedelta(months = form.cleaned_data.get('tenure_in_months'))
            print("THIS IS TENURE END", tenure_end)
            product.tenure_end = tenure_end
            product.is_rented = True
            product.save()
            transaction = Transactions(user = request.user, product=product)
            transaction.save() 
            messages.success(request, 'Congratulations You have rented - {}'.format(product.name))
            return redirect('home')
    else:
        form = ProductRentingForm()
    
    return render(request, 'ProductRent.html', {'form': form})

        

@login_required
def UpdateProduct(request, product_id, action):
    if request.method == 'POST':
        product = Product.objects.get(id = product_id)
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            print(form.cleaned_data.get('name'))
            messages.success(request, 'Your form has been Updated ')
            return redirect('product-details', product_id = product_id, action = action)
    else:
        form = ProductUpdateForm()

    return render(request, 'product_update.html', { 'form' : form })