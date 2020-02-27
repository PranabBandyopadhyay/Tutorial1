import requests
from bs4 import BeautifulSoup
import progressbar

url = "http://www.practicepython.org/assets/Training_01.txt"
r = requests.get(url).text
r_html = BeautifulSoup(r, 'html.parser')

with open(r'C:\Users\Banerjea-PC\Documents\Python_saved\sundb.txt','a') as open_file:
    open_file.write(str(r_html.string) )

num_lines = sum(1 for line in open(r'C:\Users\Banerjea-PC\Documents\Python_saved\sundb.txt'))
print("Total Line : " + str(num_lines))
catagory = {}
line_count = 0
with progressbar.ProgressBar(max_value=num_lines) as bar:
    with open(r'C:\Users\Banerjea-PC\Documents\Python_saved\sundb.txt','r') as open_file:
        line = open_file.readline()
        while line:
            line_obj = str(line).split("/")
            bar.update(line_count)
            if line_obj[2] in catagory:
                catagory[line_obj[2]] += 1
            else:
                catagory[line_obj[2]] = 1
            line = open_file.readline()
            line_count += 1

open_file = open(r'C:\Users\Banerjea-PC\Documents\Python_saved\sundb.txt','w')
open_file.close()
bar.finish()
print(catagory)