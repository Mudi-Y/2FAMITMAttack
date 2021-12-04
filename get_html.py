import requests


class RequestManager:
    "request manager that wraps all functionality of requests"
    def __init__(self, home_url):
        self.home = home_url

    def getHtml(self, site_url, output_file):
        "takes url and path to outfile, saves html of site to outfile"
        # url = input('Webpage: ')
        # html_output_name = input('Output file: ')
        output_file = str(output_file)
        req = requests.get(site_url)

        with open(output_file, 'w') as f:
            f.write(req.text)
            f.close()