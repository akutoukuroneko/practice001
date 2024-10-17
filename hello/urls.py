from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='form'),
    path('next', views.next, name='next'),
]