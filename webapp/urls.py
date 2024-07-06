from django.urls import path
from . import views

urlpatterns = [

    # Path for the homepage, calls the home view
    path('', views.home, name="home"),

    # Path for the register page, calls the register view
    path('register', views.register, name='register'),

    # Path for the login page, calls the my_login view
    path('my_login', views.my_login, name="my-login"),

    # Path for logging out, calls the user_logout view
    path('user-logout', views.user_logout, name="user-logout"),

    # CRUD operations

    # Path for the dashboard page, calls the dashboard view
    path('dashboard', views.dashboard, name="dashboard"),

    # Path for creating a new record, calls the create_record view
    path('create-record', views.create_record, name="create_record"),

    # Path for updating an existing record, calls the update_record view
    path('update-record/<int:pk>', views.update_record, name='update-record'),
]
