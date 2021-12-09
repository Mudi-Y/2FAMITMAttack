from django.urls import path

from . import views

from .helper import startup

# Initialize session
startup()

urlpatterns = [
path('', views.index, name='index'),
path('login', views.login, name='login'),
]
