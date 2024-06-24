from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm

# Creamos la funcion de Home para el HomePage
def home(request): 

    # llamamos de template el template creado llamado index.html 
    return render(request, 'webapp/index.html')

# Creamos la funcion de Register
def register(request):

    form = CreateUserForm()

    if request.method == "POST":

        form = CreateUserForm(request.POST) 

        if form.is_valid():

            form.save()

            # return redirect('')

    context = {'form': form}

    return render(request, 'webapp/register.html', context=context)
