import requests
from bs4 import BeautifulSoup

class log_writer:
    def __init__(object):
        print()

    def log(self, elem):
        with open(r'C:\Users\Banerjea-PC\Documents\Python_saved\log.txt', 'a') as open_file:
            open_file.write(str(elem) + '\n')


url = "http://www.nytimes.com/"
r_html = requests.get(url).text
soup = BeautifulSoup(r_html, 'html.parser')
logger = log_writer()

for headline in soup.find_all(class_="css-1qwxefa esl82me0"):
    if headline.a:
        logger.log(headline.a.text.replace("\n", " ").strip())
    else:
        logger.log(headline.contents[0].text.strip())