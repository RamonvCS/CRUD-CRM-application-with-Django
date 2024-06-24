
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Creamos la rutas (path) y llamamos los URLs de webapp (ejemplo webapp.urls)
    path('', include('webapp.urls'))
]
