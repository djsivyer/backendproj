from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
# Create your views here.

def index_view(request):
    return render(request, 'finapp/index.html')

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Implement your login logic here

    return render(request, 'login.html')