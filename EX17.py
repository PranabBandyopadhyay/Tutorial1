import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/"
r_html = requests.get(url).text
soup = BeautifulSoup(r_html, 'html.parser')

for headline in soup.find_all(class_="css-1qwxefa esl82me0"):
    if headline.a:
        print(headline.a.text.replace("\n", " ").strip())
    else:
        print(headline.contents[0].text.strip())
