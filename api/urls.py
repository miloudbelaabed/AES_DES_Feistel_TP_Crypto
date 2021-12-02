
from django.urls import path, include
from django.http import HttpResponse
from .views import main

urlpatterns = [
    path('', main),
    
]
