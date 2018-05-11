from django.urls import path
from basic_app import views
#template taggin
app_name = 'basic_app'

urlpatterns = [
    path('', views.relative, name='relative'),
    path('other', views.other, name='other'),
]
