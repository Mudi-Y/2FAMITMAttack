import requests

url = input('Webpage: ')
html_output_name = input('Output file: ')

req = requests.get(url)

with open(html_output_name, 'w') as f:
    f.write(req.text)
    f.close()