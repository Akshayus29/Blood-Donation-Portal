from django.shortcuts import render, redirect, get_object_or_404
from .models import Donor
from .forms import DonorForm
from django.contrib import messages 

# donor_app/views.py

def home(request):
    return render(request, 'home.html') # 'home.html' 

def register(request):
    # Base query: taking all donors
    donors = Donor.objects.all()
    
    # taking search values from URL
    bg_query = request.GET.get('blood_group')
    loc_query = request.GET.get('location')

    # Filter Logic
    if bg_query:
        donors = donors.filter(blood_group__iexact=bg_query)
    
    if loc_query:
        donors = donors.filter(location__iexact=loc_query)

    # Registration Form handling
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            #add success message
            messages.success(request, "🎉 Registration Successful! Thank you for being a donor.")
            return redirect('register_page')
    else:
        form = DonorForm()
        
    # filtered donors list and form return to register.html
    return render(request, 'register.html', {
        'donors': donors, 
        'form': form
    })

