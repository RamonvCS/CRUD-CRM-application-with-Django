from django.urls import path
from . import views

urlpatterns = [

    # Creamos el path para homepage "Views"
    path('', views.home, name=""),

    path('register', views.register, name='register' ),

    path('my_login', views.my_login, name="my-login" ),

]