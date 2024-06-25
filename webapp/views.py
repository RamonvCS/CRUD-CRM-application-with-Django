from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

from django.contrib.auth import authenticate, login as auth_login

# ----------- Creamos la función de Home para el HomePage
def home(request): 

    # llamamos de template el template creado llamado index.html 
    return render(request, 'webapp/index.html')

# ---------- Creamos la función de Register
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

                return redirect('my-login')

    context = {'form': form}

    return render(request, 'webapp/my-login.html', context=context)

#  ----------------------  User Logout

def user_logout(request):
    
    auth_logout(request)

    return redirect("my-login")