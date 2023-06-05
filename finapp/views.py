from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views import generic
# Create your views here.

def index_view(request):
    return render(request, 'finapp/index.html')

def login_view(request):
    return render(request, 'finapp/login.html')

def register_view(request):
    return render(request, 'finapp/register.html')