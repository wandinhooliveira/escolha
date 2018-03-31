from django.contrib import admin
from django.urls import path
from .views import home , slug , results

urlpatterns = [
    path('', home),
    path('resultados/', results),
    path('<slug>/',slug )
]