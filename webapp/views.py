from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Record

# ----------- Function to render the HomePage
def home(request): 
    return render(request, 'webapp/index.html')

# ----------- Function to register a new user
def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my-login')

    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)

# ----------- Function to log in a user
def my_login(request):

    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')

    context = {'form': form}

    return render(request, 'webapp/my-login.html', context=context)

# ----------- Function to render the Dashboard, requires login
@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)

# ----------- Function to log out a user
def user_logout(request):

    auth_logout(request)

    return redirect("my-login")

# ----------- Function to create a new record, requires login
@login_required(login_url='my-login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)

# ----------- Function to update an existing record, requires login
@login_required(login_url='my-login')
def update_record(request, pk):
    
    record = Record.objects.get(id=pk)
    
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()  # Save the changes to the record
            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/update-record.html', context=context)

#  - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = Record.objects.get(id=pk)

    context = {'record': all_records}

    return render(request, 'webapp/view-record.html', context=context)

# -------  Delete a Record 

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = Record.objects.get(id.pk)

    record.delete()

    return redirect("dashboard")
