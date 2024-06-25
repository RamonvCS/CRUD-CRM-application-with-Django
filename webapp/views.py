from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth import authenticate, login as auth_login

from django.contrib.auth.decorators import login_required

# ----------- Creamos la función de HomePage
def home(request): 

    # llamamos de template el template creado llamado index.html 
    return render(request, 'webapp/index.html')

# ---------- Creamos la función de Register User
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST) 

        if form.is_valid():

            form.save()

            # return redirect('')

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

    return render(request, 'webapp/dashboard.html')





#  ----------------------  User Logout

def user_logout(request):
    
    auth.logout(request)

    return redirect("my-login")