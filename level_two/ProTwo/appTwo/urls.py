from django.urls import path
from appTwo import views

urlpatterns = [
    path('', views.users, name='users'),
    path('signup', views.signup, name='signup')
]
