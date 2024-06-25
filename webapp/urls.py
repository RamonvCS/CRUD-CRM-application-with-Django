from django.urls import path
from . import views

urlpatterns = [

    # Creamos el path para homepage "Views"
    path('', views.home, name=""),

    path('register', views.register, name='register' ),

    path('my_login', views.my_login, name="my-login" ),

    path('user-logout', views.user_logout, name="user-logout"),
    
    path('dashboard', views.dashbaord, name="dashboard"),

    


]