from django.urls import path
from . import views

urlpatterns = [

    # Creamos el path para homepage "Views"
    path('', views.home, name="home"),

    path('register', views.register, name='register'),

    path('my_login', views.my_login, name="my-login"),

    path('user-logout', views.user_logout, name="user-logout"),

    #  CRUD 

    path('dashboard', views.dashboard, name="dashboard"),

    path('create-record', views.create_record, name="create_record"),
]

# CRUD 
