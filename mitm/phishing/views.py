from django.http import HttpResponse
import requests

# Phishing site for FB
def index(request):
    req = requests.get('https://www.facebook.com/')
    return HttpResponse(req.text)