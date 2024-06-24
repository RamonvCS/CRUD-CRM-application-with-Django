from django.shortcuts import render

# Creamos la funcion de Home para el HomePage
def home(request): 

    # llamamos de template el template creado llamado index.html 
    return render(request, 'webapp/index.html')

