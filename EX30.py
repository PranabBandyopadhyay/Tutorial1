from url2file import url_to_file
import random

def guess_a_word():
    filename  = "C:\\Users\\Banerjea-PC\\Documents\\Python_saved\\sowpods.txt"
    url = "http://norvig.com/ngrams/sowpods.txt"
    a = url_to_file(url, filename)
    a.download()

    count = sum(1 for line in open(filename, 'r'))


    wordpos = random.randint(1, count)
    counter = 1
    with open(filename, 'r') as open_file:
        line  = open_file.readline()
        while line:
            if counter == wordpos:
                return line.strip()
                break
            counter += 1
            line = open_file.readline()

    with open(filename, 'w') as open_file:
        pass

