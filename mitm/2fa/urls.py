from django.urls import path

from . import views

from .helper import startup

# Initialize session
startup()

urlpatterns = [
path('', views.index, name='index'),
# path('login', views.login, name='login'),
path('checkpoint/lg/login-submit', views.checkpoint_lg_login_submit, name='checkpoint_lg_login_submit'),
path('checkpoint/challenge/verify', views.checkpoint_challenge_verify, name='checkpoint_challenge_verify'),
# path('help/linkedin/answer/531/', views.help_linkedin_answer_531, name='help_linkedin_answer_531'),
]
