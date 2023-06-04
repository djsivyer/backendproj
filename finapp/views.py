from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.views import generic
# Create your views here.

def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Implement your login logic here

    return render(request, 'login.html')