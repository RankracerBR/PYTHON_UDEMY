import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html,'html.parser')

if parsed_html.title is not None:
    print(parsed_html.title.text)