from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', registration, name = 'reg'),
    path('login/', user_login, name = 'login'),
    path('home/', home, name = 'home')
]
