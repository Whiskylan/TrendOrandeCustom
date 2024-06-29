from django.urls import path

from .views import login_user, logout_user, register

urlpatterns = [
    path('register', register, name='register'),
    path('login', login_user, name='login_user'),
    path('logout', logout_user, name='logout'),
]