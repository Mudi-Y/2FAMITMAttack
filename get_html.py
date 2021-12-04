import requests


class RequestManager:
    def __init__(self, home_url):
        self.home = home_url

    def getHtlm(self, site_url, output_file):
        # url = input('Webpage: ')
        # html_output_name = input('Output file: ')
        output_file = str(output_file)
        req = requests.get(site_url)

        with open(output_file, 'w') as f:
            f.write(req.text)
            f.close()