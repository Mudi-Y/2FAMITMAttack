from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helper import display_view, login_post

def index(request):
    url = 'https://secure.its.yale.edu/cas/login?service=https%3A%2F%2Fyale.instructure.com%2Flogin%2Fcas'
    return display_view(url)

@csrf_exempt
def login(request):
    url = 'https://secure.its.yale.edu/cas/login?service=https%3A%2F%2Fyale.instructure.com%2Flogin%2Fcas'
    return login_post(url, request.POST)
