import random, string
import nltk
from nltk.corpus import words


def randstring(num):
    x = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=num))
    return x

def string_select(length):
    l = string.ascii_lowercase
    return " ".join(random.choice(l) for i in length)

def main():
    complexity = int(input("Enter your password complexity (1-10): "))

    if complexity == 1:
        nltk.download('words')
        word_list = words.words()
        return word_list[random.randint(1,236736)]

    elif complexity >=2 and complexity <=4:
        nltk.download('words')
        word_list = words.words()
        return  word_list[random.randint(1,236736)] + "@" + randstring(complexity)

    else:
        return randstring(complexity*2)


print(main())