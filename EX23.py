from url2file import url_to_file
from list_overlap import overlap

url = "http://www.practicepython.org/assets/primenumbers.txt"
filename = 'C:\\Users\\Banerjea-PC\\Documents\\Python_saved\\primenumbers.txt'
u2f = url_to_file(url, filename)
u2f.download()
a = []
with open(filename, 'r') as open_file:
    line = open_file.readline()
    while line:
        a.append(str(line).strip('\n'))
        line = open_file.readline()

url = "http://www.practicepython.org/assets/happynumbers.txt"
filename = "C:\\Users\\Banerjea-PC\\Documents\\Python_saved\\happynumbers.txt"
u2f = url_to_file(url, filename)
u2f.download()
b = []
with open(filename, 'r') as open_file:
    line = open_file.readline()
    while line:
        b.append(str(line).strip('\n'))
        line = open_file.readline()

overlapping = overlap(a, b)
c = overlapping.display()
print(c)
