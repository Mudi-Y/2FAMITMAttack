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
def help_getting_help_canvas(request):
    url = 'https://canvas.yale.edu/loginhelp/getting-help-canvas'
    return display_view(url)
def terms_use(request):
    url = 'https://canvas.yale.edu/loginterms-use'
    return display_view(url)
def tips_good_practices_canvas(request):
    url = 'https://canvas.yale.edu/logintips-good-practices-canvas'
    return display_view(url)
def calendar(request):
    url = 'https://secure.its.yale.edu/cas/login?service=https%3A%2F%2Fyale.instructure.com%2Flogin%2Fcascalendar'
    return display_view(url)
def conversations(request):
    url = 'https://secure.its.yale.edu/cas/login?service=https%3A%2F%2Fyale.instructure.com%2Flogin%2Fcasconversations'
    return display_view(url)
