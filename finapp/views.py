#from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
#from django.template import loader
#from django.views import generic
# Create your views here.

def index_view(request):
    return render(request, 'finapp/index.html')

def login_view(request):
    return render(request, 'finapp/login.html')

def register_view(request):
    return render(request, 'finapp/register.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})