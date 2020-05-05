"""import wordlist
generator = wordlist.Generator('charset')
for each in generator.generate(2, 5):
    print(each)


import nltk
from nltk.corpus import words
nltk.download('words')
word_list = words.words()
# prints 236736
print (len(word_list))

import random, string
x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
print(x) """
"""
import request

url = 'http://github.com'
r = request.GET(url)
r_html = r.text



from progress.bar import Bar

bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()"""
"""
import time
import progressbar

for i in progressbar.progressbar(range(100)):
    time.sleep(0.02)

    if __name__ == '__main__':
        u2f = url_to_file(url, filename)
        u2f.download()

length = 5
guessed = length*["_"]
print(guessed)"""
import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/"
r_html = requests.get(url).text
soup = BeautifulSoup(r_html, 'html.parser')

print(soup.prettify())