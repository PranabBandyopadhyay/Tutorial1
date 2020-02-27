import requests
from bs4 import BeautifulSoup


class url_to_file:
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    def download(self):
        r = requests.get(self.url).text
        r_html = BeautifulSoup(r, 'html.parser')

        with open(self.filename, 'a') as open_file:
            open_file.write(str(r_html.string))

