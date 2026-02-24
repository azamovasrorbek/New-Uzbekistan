from django.urls import path
from .views import home, main

urlpatterns = [
    path('',main, name='main'),
    path('home/', home, name='home')

]