from django.urls import path
from firstApp import views

urlpatterns = [
    path('', views.index, name='index')
]
