from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Transaction
from django.contrib.auth.models import User

def register(request):
    """ View for registering new users if request method is post get data and display for else display empty form"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # Check for valid form. If valid redirect to home 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # Flash success message if successful
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})    

# login_required decorator to ensure login is required to access profile
@login_required
def profile(request):
    
    reqUser = User.objects.get(username=request.user.username)
    querySet = Transaction.objects.filter(buyer=reqUser) | Transaction.objects.filter(seller=reqUser)
    context = {
        'queries' : querySet
    }
    return render(request, 'users/profile.html', context)