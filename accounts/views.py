from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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
    return render(request,'accounts/login.html')

# def logout_view(request):
#     return render(request,login.html)

def signup_view(request):
    return render(request,'accounts/signup.html')