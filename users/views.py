from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    """ View for registering new users if request method is post get data and display for else display empty form"""
    if register.method == 'POST':
        form = UserCreationForm(request.POST)
        # Check for valid form. If valid redirect to home 
        if form.is_valid():
            username = form.cleaned_data.get('username')
            # Flash success message if succeful
            messages.success(reguest, f'Account created for {username}!')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})    
