#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
#from django.template import loader
#from django.views import generic

# Create your views here.

def index_view(request):
    return render(request, 'finapp/index.html')

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'finapp/homepage.html')
    else:
        return redirect('finapp:index')

def login_view(request):
    if request.method == 'GET':
        # Add session check to see if logged in already, if so login
        return render(request, 'finapp/login.html')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('finapp:homepage')
        else:
            messages.error(request, "Unsuccessful login. Invalid information.")

def register_view(request):
    if request.user.is_authenticated:
        return redirect('finapp:homepage')
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'finapp/register.html', context)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('finapp:homepage')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'finapp/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('finapp:index')