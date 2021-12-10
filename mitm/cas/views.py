from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helper import display_view, login_post

def index(request):
    url = 'https://canvas.yale.edu/login'
    return display_view(url)

@csrf_exempt
def login(request):
    url = 'https://secure.its.yale.edu/cas/login'
    return login_post(url, request.POST)
