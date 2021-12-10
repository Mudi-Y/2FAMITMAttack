import requests

class Req:
    "wrapper reqeust object, used for sending and receiving HTML request via \
    RequestManager object"
    def __init__(self, siteurl, auth=(), cookies={}, params={}, data={}):
        self.siteurl = siteurl
        self.auth = auth
        self.cookies = cookies
        self.params = params
        self.data = data


class RequestManager:
    "request manager that wraps all functionality of requests"
    def __init__(self, home_url=""):
        self.home = home_url
        self.log = []  # list containing all requests and responses sent/received by the manager object

    def getHtml(self, site_url, output_file="out.txt"):
        "takes url and path to outfile, saves html of site to outfile"
        # url = input('Webpage: ')
        # html_output_name = input('Output file: ')
        output_file = str(output_file)
        req = requests.get(site_url)

        with open(output_file, 'w') as f:
            f.write(req.text)
            f.close()
        return

    def logRequest(self, req:Req):
        "logs incoming and outgoing HTML requests"
        self.log.append(req)
        return

    def _print_request(self, req):
        return str('HTTP/1.1 {method} {url}\n{headers}\n\n{body}'.format(
            method=req.method,
            url=req.url,
            headers='\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
#             body=req.body,
            body = ""
        )) + "\n"

    def _print_response(self, res):
        return str('HTTP/1.1 {status_code}\n{headers}\n\n{body}'.format(
            status_code=res.status_code,
            headers='\n'.join('{}: {}'.format(k, v) for k, v in res.headers.items()),
#             body=res.content,
            body = ""
        )) + "\n"

    def showRequests(self, output_file="requestLog.txt"):
        "prints all logged requests to specified outfile path. default is requestLog.txt"
        spacerRequest = "\n==========[ Request ]==========\n"
        spacerResponse = "\n==========[ Response ]==========\n"

        with open(output_file, 'a') as f:
            f.write('\n')
            for req in self.log:
                # formatting if req is a Response
                if isinstance(req, requests.models.PreparedRequest):
                    f.write(spacerRequest)
                    val = self._print_request(req)
                    f.write(val)
                # formatting if request is a PreparedRequest
                else:
                    f.write(spacerResponse)
                    val = self._print_response(req)
                    f.write(val)
            f.close()
        return

    def getRequest(self, req:Req):
        "send a get HTML request to a destination site, and log request and response. \
        returns response"
        r = requests.get(req.siteurl, auth=req.auth, cookies=req.cookies, params=req.params)
        self.logRequest(r.request)
        self.logRequest(r)
        return r


    def postRequest(self, req:Req):
        "send a post HTML request to a destination site, and log request and response. \
        returns response"
        r = requests.post(req.siteurl, auth=req.auth, cookies=req.cookies, params=req.params, data=req.data)
        self.logRequest(r.request)
        self.logRequest(r)
        return r


    def cookieRequest(self, req:Req):
        "get all the cookies from the site, and log request and response. \
        returns cookies"
        r = requests.get(req.siteurl, auth=req.auth, cookies=req.cookies, params=req.params)
        self.logRequest(r.request)
        self.logRequest(r)
        return r.cookies

