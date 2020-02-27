import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r_html = requests.get(url).text
soup = BeautifulSoup(r_html, 'html.parser')

for i in soup.find_all('p'):
    print(i.contents[0])