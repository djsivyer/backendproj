from django.shortcuts import get_object_or_404, render, redirect
from finapp.forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from finapp.models import *

# Create your views here.

def index_view(request):
    return render(request, 'finapp/index.html')

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

def login_view(request):
    if request.user.is_authenticated:
        return redirect('finapp:homepage')
    if request.method == 'GET':
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
            return redirect('finapp:login')

def home_view(request):
    if request.user.is_authenticated:
        user_balance = TransactionsByUser.transactionsSum(request.user)
        context = {"user_balance" : user_balance}
        return render(request, 'finapp/homepage.html', context)
    else:
        return redirect('finapp:index')

def transactions_view(request):
    if request.method == 'POST':
        upload = Transactions(request.POST)
    if request.user.is_authenticated:
        user_transactions = TransactionsByUser.userTransactions(request.user)
        return render(request, 'finapp/transactions.html', {'user_transactions' : user_transactions})
    else:
        return redirect('finapp:index')

def logout_view(request):
    logout(request)
    return redirect('finapp:index')