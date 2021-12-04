import requests

class Req:
    "wrapper reqeust object, used for sending and receiving HTML request via \
    RequestManager object"
    def __init__(self, auth, cookies, params):
        self.auth = auth
        self.cookies = cookies
        self.params = params


class RequestManager:
    "request manager that wraps all functionality of requests"
    def __init__(self, home_url):
        self.home = home_url
        self.log = []

    def getHtml(self, site_url, output_file):
        "takes url and path to outfile, saves html of site to outfile"
        # url = input('Webpage: ')
        # html_output_name = input('Output file: ')
        output_file = str(output_file)
        req = requests.get(site_url)

        with open(output_file, 'w') as f:
            f.write(req.text)
            f.close()
        return


    def _logRequest(self, req:Req):
        "logs incoming and outgoing HTML requests"
        self.log.append(req)
        return


    def getRequest(self, req:Req, site):
        "send a get HTML request to a destination site, and log"
        pass


    def postRequest(self, req:Req, site):
        "send a post HTML request to a destination site"
        pass


    def cookieRequest(self, req:Req, site):
        "get all the cookies from the site"
        pass


