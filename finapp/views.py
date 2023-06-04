from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        # Handle login form submission
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Implement your login logic here

    return render(request, 'login.html')
