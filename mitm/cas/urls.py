from django.urls import path
from . import views

from .helper import startup

# Initialize session
startup()

urlpatterns = [
path('', views.index, name='index'),
path('login', views.login, name='login'),
path('help/getting-help-canvas/', views.help_getting_help_canvas, name='help_getting_help_canvas'),
path('terms-use/', views.terms_use, name='terms_use'),
path('tips-good-practices-canvas/', views.tips_good_practices_canvas, name='tips_good_practices_canvas'),
path('calendar/', views.calendar, name='calendar'),
path('conversations/', views.conversations, name='conversations'),
]
