from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helper import display_view, login_post

def index(request):
    url = 'https://secure.its.yale.edu/cas'
    ret = None
    if request.method == 'GET':
        ret = display_view(url)
    else:
        # data = {"username": request.POST.get("username"), "password": request.POST.get("password")}
        ret = login_post(url, request.POST)
    return ret

@csrf_exempt
def login(request):
    url = 'https://secure.its.yale.edu/cas/login'
    data = {"username": request.POST.get("username"), "password": request.POST.get("password")}
    print("Data: ", data)
    return login_post(url, request.POST)
