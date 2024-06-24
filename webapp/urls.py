from django.urls import path
from . import views

urlpatterns = [

    # Creamos el path para homepage "Views"
    path('', views.home, name=""),

]