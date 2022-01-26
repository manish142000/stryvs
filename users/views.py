import datetime
from itertools import product
from math import prod
from pyexpat.errors import messages
from threading import currentThread
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from stryvs import settings
from . forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, AppointmentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from store.models import Product
from django.contrib.auth.models import User
from .models import Appointments, Profile, Transactions

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your Account has been created! Login here')
            user = authenticate(username=form.cleaned_data.get(
                'username'), password=form.cleaned_data.get('password'))
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})



@login_required
def Profile_(request, owner_id, product_id):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST)
        p_form = ProfileUpdateForm(request.POST) 

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save() 
            messages.success(request, f'Your account has been updated') 
            return redirect('profile')
    else:
        if request.user.id == owner_id:
            u_form = UserUpdateForm() 
            p_form = ProfileUpdateForm()      
        else:
            obj = User.objects.filter(id = owner_id)
            profile = None
            for x in Profile.objects.all().iterator():
                if x.user.id == obj[0].id:
                    profile = x
                    break

            return render(request, 'profile.html', { 'product_id': product_id, 'owner_id': owner_id, 'profile' : profile, 'logged_in' : request.user  })

    
    u_form = UserUpdateForm() 
    p_form = ProfileUpdateForm() 
    obj = User.objects.get(id = owner_id)
    print(obj.username)
    profile = None
    for x in Profile.objects.all().iterator():
        if x.user.id == obj.id:
            profile = x
            break
    print(profile)       
    return render(request, 'profile.html', { 'product_id': product_id, 'owner_id': owner_id, 'profile' : profile, 'u_form': u_form, 'p_form': p_form })  



@login_required
def transactions(request, product_id = "-1"):

    transaxns = Transactions.objects.all()
    date_of_transaction = datetime.date.today()

    if product_id == "-1":
        return render(request, 'transaction.html', { 'transaxns': transaxns, 'date_of_transaction': date_of_transaction }) 

    product = Product.objects.get(id = product_id)
    user = User.objects.get(id = request.user.id)
    
    transaxn = Transactions.objects.create(user = user, product = product)
    transaxn.save() 
    
    messages.success('Your transaction for {} is successful'.format(product.name))
    return redirect('trans_actions', product_id="-1")




@login_required
def make_appointment(request, product_id):

    if request.method == 'POST':
        print("POST")
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print("is valid")
            appointment = form.save(commit = False)
            product = Product.objects.get(id = product_id)
            
            appointment.product = product 
            appointment.appointment_maker = request.user

            owner_id = product.owner_id
            accepter =  User.objects.get(id = owner_id)

            appointment.appointment_date = form.cleaned_data.get('appointment_date')
            appointment.appointment_time = form.cleaned_data.get('appointment_time')
            appointment.appointment_subject = form.cleaned_data.get('appointment_subject')
            appointment.appointment_accepter = accepter
            appointment.save()

            messages.success(request, 'Your appointment has been requested!')
            return redirect('manage-appointments', 'frombase', 1)
    

    form = AppointmentForm()    
    return render(request, 'appointmentform.html', { 'form': form} )

@login_required
def manage_appointments(request, flag, appointment_id):
    
    context = {
        'appointments': Appointments.objects.all(),
    }

    if flag == 'frombase':
        print(flag)
        return render(request, 'appointments.html', context)

    #print("APPOINTMENT ID is", appointment_id)
    appointment = Appointments.objects.get(id = appointment_id)

    if flag == "-1":
        appointment.status = True
        appointment.save() 
    elif flag == '-2':
        appointment.delete() 

    
    return render(request, 'appointments.html', context)


        
