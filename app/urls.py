from django.urls import path
from .views import home, main, add_comment

urlpatterns = [
    path('', main, name='main'),
    path('home/', home, name='home'),
    path('add-comment/', add_comment, name='add_comment'),
]