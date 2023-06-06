#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterForm
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

def register_view(request):
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
            return redirect('finapp:homepage.html')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
        context = {'form': form}
        return render(request, 'finapp/register.html', context)

    return render(request, 'finapp/register.html', {})


def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('finapp:homepage.html')
    else:
          messages.error(request, "Unsuccessful login. Invalid information.")