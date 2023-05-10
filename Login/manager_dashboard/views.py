from django.contrib.auth import authenticate, login,  logout
from django.shortcuts import render, redirect
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('manager_dashboard:dashboard')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'manager_dashboard/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('manager_dashboard:login')


def home(request):
    # Add logic to fetch and display the required data
    return render(request, 'manager_dashboard/home.html')

from django.shortcuts import render

def menu(request):
    # Your code for displaying menu goes here
    return render(request, 'manager_dashboard/menu.html')

def dashboard(request):
    # Your code for displaying menu goes here
    return render(request, 'manager_dashboard/dashboard.html')




