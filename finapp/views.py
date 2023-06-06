#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
#from django.template import loader
#from django.views import generic
# Create your views here.

def index_view(request):
    return render(request, 'finapp/index.html')

def login_view(request):
    if request.method == 'GET':
    	return render(request, 'finapp/login.html')
    if request.method == 'POST':
        return redirect('homepage')

def register_view(request):
    if request.method == 'GET':
          return render(request, 'finapp/register.html')
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('homepage')
        messages.error(request, "Unsuccessful registration. Invalid information.")
        form = NewUserForm()
    return render (request, 'finapp/login.html')

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('homepage')
    else:
          messages.error(request, "Unsuccessful login. Invalid information.")