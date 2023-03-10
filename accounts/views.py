from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignupForm
from django.contrib.auth.models import User

# Create your views here.
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Successfull login." )
                    return redirect('/')
                else:
                    messages.error(request, "Error. Username or password is not valid.")
    else:
        return redirect('/')
    return render(request,'account/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
    
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account successfully created.' )
                return redirect('/')
            else:
                messages.error(request, "Error. Something went wrong.")
        else:
            form = SignupForm()
        return render(request,'account/signup.html', {'form': form})
    else:
        return redirect('/')