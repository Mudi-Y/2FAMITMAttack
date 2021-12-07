from django.http import HttpResponse

import requests
from .helper import parse_html, display_view

# Phishing site for FB
def index(request):
    url = 'https://www.wechall.net/'
    return display_view(url)
