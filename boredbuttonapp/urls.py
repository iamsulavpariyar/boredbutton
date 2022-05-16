from re import template
from django.urls import path
from . import views
from django.views.generic import TemplateView
from .views import *

urlpatterns =[
    path('' , home , name="home"),
    path('games', views.games, name='games'),
    path('contact', views.contact, name='contact'),
    path('<str:slug>', views.base, name='base'),
    
    
    
]
