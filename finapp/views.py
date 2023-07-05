from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from finapp.forms import RegisterForm
from finapp.models import *
import csv

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
    #need to add checks for duplicate data
    #Should probably move it into a function of upload so its not within the view?
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Invalid file format. Please upload a CSV file.')
        
        else:
            # Read the CSV file
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            
            # Check if the file has headers
            if not csv.Sniffer().has_header(decoded_file[0]):
                messages.error(request, 'CSV file is missing headers.')
                return render(request, 'transactions.html')
            
            # Verify the header row
            header_row = next(reader)
            expected_headers = ['date', 'time', 'vendor', 'amount']
            
            if header_row != expected_headers:
                messages.error(request, 'Incorrect CSV header format.')
                return render(request, 'transactions.html')
            
            # Process the data rows
            for row in reader:
                date = row[0]
                time = row[1]
                vendor = row[2]
                amount = row[3]
                
                # Assuming the logged-in user's transactions model has fields: date, time, vendor, amount
                transaction = Transactions(user=request.user, date=date, time=time, vendor=vendor, amount=amount)
                transaction.save()
                
            messages.success(request, 'Transactions uploaded successfully.')
        user_transactions = TransactionsByUser.userTransactions(request.user)
        return render(request, 'finapp/transactions.html', {'user_transactions' : user_transactions})

    if request.user.is_authenticated:
        user_transactions = TransactionsByUser.userTransactions(request.user)
        return render(request, 'finapp/transactions.html', {'user_transactions' : user_transactions})
    else:
        return redirect('finapp:index')

def logout_view(request):
    logout(request)
    return redirect('finapp:index')