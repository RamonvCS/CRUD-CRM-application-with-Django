from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


from .models import Record

# ----------- Creamos la función de HomePage
def home(request): 
    return render(request, 'webapp/index.html')

# ---------- Creamos la función de Register User
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('my-login')
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)

# ---------- Login a user
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

# - Dashboard
@login_required(login_url='my-login')
def dashboard(request):

    my_records = Record.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)

#  ----------------------  User Logout
def user_logout(request):
    auth_logout(request)
    return redirect("my-login")

#  - CREATE A RECORD

@login_required(login_url='my-login')
def create_record(request):
    
    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("dashboard")
        
    context = {'form': form}

    return render(request, 'webaap/create-record.html', context=context)

