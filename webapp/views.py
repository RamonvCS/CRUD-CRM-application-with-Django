from django.shortcuts import render

# Creamos el Http response
from django.http import HttpResponse

# Creamos la funcion de Home para el HomePage
def home(request):

    # return HttpResponse('Hello World')

    return render(request, 'webapp/index.html')